
from search.algorithms.flooding import FloodingSearch
from search.algorithms.informed_flooding import InformedFloodingSearch
from search.algorithms.informed_random_walk import InformedRandomWalkSearch
from search.algorithms.random_walk import RandomWalkSearch


class SearchEngine:
    def __init__(self, graph):
        self.graph = graph
        self.algorithms = {
            "flooding": FloodingSearch(graph),
            "informed_flooding": InformedFloodingSearch(graph),
            "random_walk": RandomWalkSearch(graph),
            "informed_random_walk": InformedRandomWalkSearch(graph),
        }

    def run_search(self, algo, start_node, target_resource, ttl):
        if algo not in self.algorithms:
            raise ValueError(f"Algoritmo '{algo}' inválido.")

        algorithm_instance = self.algorithms[algo]
        result = algorithm_instance.run(start_node, target_resource, ttl)
        
        algorithm_instance.display_report(algo, result)
        
        return result