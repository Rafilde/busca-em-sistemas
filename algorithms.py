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
        pass

    def _informed_flooding(self, start_node, target_resource, ttl):
        pass

    def _random_walk(self, start_node, target_resource, ttl):
        pass

    def _informed_random_walk(self, start_node, target_resource, ttl):
        pass