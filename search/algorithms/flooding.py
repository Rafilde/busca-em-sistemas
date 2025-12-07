from ..base import SearchAlgorithm

class FloodingSearch(SearchAlgorithm):

    def run(self, start_node_id, target_resource, ttl):
        msgs_count = 0
        nodes_involved = set()

        queue = [(start_node_id, ttl)]
        visited = {start_node_id}
        nodes_involved.add(start_node_id)

        while queue:
            current_id, current_ttl = queue.pop(0)
            
            node_obj = self.network.get_node(current_id)
            if not node_obj: continue

            if node_obj.has_resource(target_resource):
                return {
                    "success": True,
                    "msgs": msgs_count,
                    "nodes": len(nodes_involved),
                    "final_node": current_id
                }

            if current_ttl <= 0:
                continue

            for neighbor_id in node_obj.neighbors:
                if neighbor_id not in visited:
                    msgs_count += 1
                    visited.add(neighbor_id)
                    nodes_involved.add(neighbor_id)
                    queue.append((neighbor_id, current_ttl - 1))

        return {"success": False, "msgs": msgs_count, "nodes": len(nodes_involved)}