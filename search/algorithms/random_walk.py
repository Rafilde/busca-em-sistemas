import random
from ..base import SearchAlgorithm

class RandomWalkSearch(SearchAlgorithm):

    def run(self, start_node_id, target_resource, ttl):
        msgs_count = 0
        nodes_involved = set()

        queue = [(start_node_id, ttl)]
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

            neighbors = list(node_obj.neighbors)
            
            if neighbors:
                next_node_id = random.choice(neighbors)
                msgs_count += 1
                nodes_involved.add(next_node_id)
                queue.append((next_node_id, current_ttl - 1))

        return {"success": False, "msgs": msgs_count, "nodes": len(nodes_involved)}