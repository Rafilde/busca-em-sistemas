import random

class SearchEngine:
    def __init__(self, network_graph):
        self.graph = network_graph

    def run_search(self, start_node, target_resource, ttl, algo):
        print(f"\n--- Iniciando busca por '{target_resource}' (Algo={algo}, TTL={ttl}) ---")
        
        if algo == 'flooding':
            return self._flooding(start_node, target_resource, ttl)
        elif algo == 'informed_flooding':
            return self._informed_flooding(start_node, target_resource, ttl)
        elif algo == 'random_walk':
            return self._random_walk(start_node, target_resource, ttl)
        elif algo == 'informed_random_walk':
            return self._informed_random_walk(start_node, target_resource, ttl)
        else:
            print("Algoritmo desconhecido.")
            return None

    def _flooding(self, start_node, target_resource, ttl):
        msgs_count = 0
        nodes_involved = set()
        
        queue = [(start_node, ttl)]
        visited = {start_node}
        nodes_involved.add(start_node)

        while queue:
            current_node, current_ttl = queue.pop(0)
            
            if target_resource in self.graph.nodes[current_node]['resources']:
                print(f"!!! ENCONTRADO no nó {current_node} !!!")
                return {
                    "success": True,
                    "msgs": msgs_count,
                    "nodes": len(nodes_involved),
                    "final_node": current_node
                }

            if current_ttl <= 0:
                continue

            neighbors = list(self.graph.neighbors(current_node))
            for neighbor in neighbors:
                if neighbor not in visited:
                    msgs_count += 1
                    visited.add(neighbor)
                    nodes_involved.add(neighbor)
                    queue.append((neighbor, current_ttl - 1))

        print("XXX Não encontrado XXX")
        return {"success": False, "msgs": msgs_count, "nodes": len(nodes_involved)}

    def _random_walk(self, start_node, target_resource, ttl):
        msgs_count = 0
        nodes_involved = set()
        
        queue = [(start_node, ttl)]
        
        nodes_involved.add(start_node)

        while queue:
            current_node, current_ttl = queue.pop(0)
            
            if target_resource in self.graph.nodes[current_node]['resources']:
                print(f"!!! ENCONTRADO no nó {current_node} !!!")
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
                next_node = random.choice(neighbors)
                
                msgs_count += 1
                nodes_involved.add(next_node)
                
                queue.append((next_node, current_ttl - 1))

        print("XXX Não encontrado (TTL acabou ou beco sem saída) XXX")
        return {"success": False, "msgs": msgs_count, "nodes": len(nodes_involved)}

    # Bom validar esse antes
    def _informed_random_walk(self, start_node, target_resource, ttl):
        msgs_count = 0
        nodes_involved = set()
        
        queue = [(start_node, ttl, None)]
        
        nodes_involved.add(start_node)

        while queue:
            current_node, current_ttl, previous_node = queue.pop(0)

            print(f"-> Visitando: {current_node} (TTL: {current_ttl}, Veio de: {previous_node})")
            
            if target_resource in self.graph.nodes[current_node]['resources']:
                print(f"!!! ENCONTRADO no nó {current_node} !!!")
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
                
                best_neighbor = None

                if novos_vizinhos:
                    random.shuffle(novos_vizinhos) 
                    best_neighbor = max(novos_vizinhos, key=lambda n: len(list(self.graph.neighbors(n))))
                
                else:
                    best_neighbor = previous_node
                
                if best_neighbor:
                    msgs_count += 1
                    nodes_involved.add(best_neighbor)
                    
                    queue.append((best_neighbor, current_ttl - 1, current_node))
                
        print("XXX Não encontrado (TTL acabou) XXX")
        return {"success": False, "msgs": msgs_count, "nodes": len(nodes_involved)}

    def _informed_flooding(self, start_node, target_resource, ttl):
        pass