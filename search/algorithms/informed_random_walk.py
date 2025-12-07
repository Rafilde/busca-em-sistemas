import random
from ..base import SearchAlgorithm

class InformedRandomWalkSearch(SearchAlgorithm):

    def run(self, start_node_id, target_resource, ttl):
        msgs_count = 0
        nodes_involved = set()
        
        queue = [(start_node_id, ttl, [start_node_id])]
        nodes_involved.add(start_node_id)

        while queue:
            current_id, current_ttl, current_path = queue.pop(0)

            node_obj = self.network.get_node(current_id)
            if not node_obj: continue

            cached_location = node_obj.get_cache(target_resource)
            if cached_location:
                cached_node_obj = self.network.get_node(cached_location)
                if cached_node_obj and cached_node_obj.has_resource(target_resource):
                    self._update_path_cache(current_path, target_resource, cached_location)
                    return {
                        "success": True, "msgs": msgs_count, "nodes": len(nodes_involved),
                        "final_node": cached_location, "source": "cache"
                    }

            if node_obj.has_resource(target_resource):
                self._update_path_cache(current_path, target_resource, current_id)
                return {
                    "success": True, "msgs": msgs_count, "nodes": len(nodes_involved),
                    "final_node": current_id
                }

            if current_ttl <= 0: continue

            neighbors = list(node_obj.neighbors)
            if neighbors:
                next_node_id = random.choice(neighbors)
                
                msgs_count += 1
                nodes_involved.add(next_node_id)
                new_path = current_path + [next_node_id]
                queue.append((next_node_id, current_ttl - 1, new_path))

        return {"success": False, "msgs": msgs_count, "nodes": len(nodes_involved)}

    def _update_path_cache(self, path_ids, resource, location_id):
        for nid in path_ids:
            node = self.network.get_node(nid)
            if node:
                node.update_cache(resource, location_id)