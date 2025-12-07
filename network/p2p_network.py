import json
import networkx as nx

class P2PNetwork:
    def __init__(self, config_file):
        self.graph = nx.Graph()
        self.config_file = config_file
        self.min_neighbors = 0
        self.max_neighbors = 0
        
        self.load_network()

    def load_network(self):
        with open(self.config_file, 'r') as f:
            data = json.load(f)
            
        self.min_neighbors = data.get('min_neighbors', 1)
        self.max_neighbors = data.get('max_neighbors', 4)
        
        resources = data['resources']
        for node_id, file_list in resources.items():
            self.graph.add_node(node_id, resources=set(file_list), cache={})
        
        self.graph.add_edges_from(data['edges'])
        
        print(f"Rede carregada: {self.graph.number_of_nodes()} nós e {self.graph.number_of_edges()} conexões.")

    def get_node(self, node_id):
        """Helper para pegar dados de um nó com segurança"""
        if self.graph.has_node(node_id):
            return self.graph.nodes[node_id]
        return None