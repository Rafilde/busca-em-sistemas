from ..base import SearchAlgorithm

class FloodingSearch(SearchAlgorithm):

    def run(self, start_node, target_resource, ttl):
        msgs_count = 0
        nodes_involved = set()

        queue = [(start_node, ttl)]
        visited = {start_node}
        nodes_involved.add(start_node)

        while queue:
            current_node, current_ttl = queue.pop(0)

            if target_resource in self.graph.nodes[current_node]['resources']:
                return {
                    "success": True,
                    "msgs": msgs_count,
                    "nodes": len(nodes_involved),
                    "final_node": current_node
                }

            if current_ttl <= 0:
                continue

            for neighbor in self.graph.neighbors(current_node):
                if neighbor not in visited:
                    msgs_count += 1
                    visited.add(neighbor)
                    nodes_involved.add(neighbor)
                    queue.append((neighbor, current_ttl - 1))

        return {"success": False, "msgs": msgs_count, "nodes": len(nodes_involved)}
