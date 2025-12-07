import random

from search.base import SearchAlgorithm

class InformedRandomWalkSearch(SearchAlgorithm):

    def run(self, start_node, target_resource, ttl):
        msgs_count = 0
        nodes_involved = set()
        
        queue = [(start_node, ttl, [start_node])]
        
        nodes_involved.add(start_node)

        while queue:
            current_node, current_ttl, current_path = queue.pop(0)

            node_cache = self.graph.nodes[current_node].get('cache', {})
            cached_location = node_cache.get(target_resource)
            
            if cached_location:
                if (self.graph.has_node(cached_location) and 
                    target_resource in self.graph.nodes[cached_location]['resources']):
                    
                    self._update_path_cache(current_path, target_resource, cached_location)
                    
                    return {
                        "success": True, "msgs": msgs_count, "nodes": len(nodes_involved),
                        "final_node": cached_location, "source": "cache"
                    }

            if target_resource in self.graph.nodes[current_node]['resources']:
                self._update_path_cache(current_path, target_resource, current_node)
                
                return {
                    "success": True, "msgs": msgs_count, "nodes": len(nodes_involved),
                    "final_node": current_node
                }

            if current_ttl <= 0:
                continue

            neighbors = list(self.graph.neighbors(current_node))
            if neighbors:
                next_node = random.choice(neighbors)
                
                msgs_count += 1
                nodes_involved.add(next_node)
                
                new_path = current_path + [next_node]
                queue.append((next_node, current_ttl - 1, new_path))

        return {"success": False, "msgs": msgs_count, "nodes": len(nodes_involved)}

    def _update_path_cache(self, path, resource, location):
        """Função auxiliar para ensinar o caminho onde o arquivo está"""
        for node in path:
            if 'cache' not in self.graph.nodes[node]:
                self.graph.nodes[node]['cache'] = {}
            self.graph.nodes[node]['cache'][resource] = location