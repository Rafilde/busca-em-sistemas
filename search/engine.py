from .algorithms.flooding import FloodingSearch
from .algorithms.informed_flooding import InformedFloodingSearch
from .algorithms.informed_random_walk import InformedRandomWalkSearch
from .algorithms.random_walk import RandomWalkSearch

class SearchEngine:
    def __init__(self, network): 
        self.network = network
        self.algorithms = {
            "flooding": FloodingSearch(network),
            "informed_flooding": InformedFloodingSearch(network),
            "random_walk": RandomWalkSearch(network),
            "informed_random_walk": InformedRandomWalkSearch(network),
        }

    def run_search(self, algo, start_node, target_resource, ttl):
        if algo not in self.algorithms:
            raise ValueError(f"Algoritmo '{algo}' inválido.")

        algorithm_instance = self.algorithms[algo]
        result = algorithm_instance.run(start_node, target_resource, ttl)
        
        algorithm_instance.display_report(algo, result)
        
        return result