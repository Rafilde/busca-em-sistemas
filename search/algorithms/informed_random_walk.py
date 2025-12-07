import random
from ..base import SearchAlgorithm

class InformedRandomWalkSearch(SearchAlgorithm):

    def run(self, start_node, target_resource, ttl):
        msgs_count = 0
        nodes_involved = set()

        queue = [(start_node, ttl, None)]
        nodes_involved.add(start_node)

        while queue:
            current_node, current_ttl, previous_node = queue.pop(0)

            if target_resource in self.graph.nodes[current_node]['resources']:
                return {
                    "success": True,
                    "msgs": msgs_count,
                    "nodes": len(nodes_involved),
                    "final_node": current_node
                }

            if current_ttl <= 0:
                continue

            neighbors = list(self.graph.neighbors(current_node))
            if neighbors:
                novos_vizinhos = [n for n in neighbors if n != previous_node]

                if novos_vizinhos:
                    random.shuffle(novos_vizinhos)
                    best = max(novos_vizinhos, key=lambda n: len(list(self.graph.neighbors(n))))
                else:
                    best = previous_node

                if best:
                    msgs_count += 1
                    nodes_involved.add(best)
                    queue.append((best, current_ttl - 1, current_node))

        return {"success": False, "msgs": msgs_count, "nodes": len(nodes_involved)}
