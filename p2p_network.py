import json
import networkx as nx
import matplotlib.pyplot as plt

class P2PNetwork:
    def __init__(self, config_file):
        self.graph = nx.Graph()
        self.config_file = config_file
        self.load_network()
        
    def load_network(self):
        try:
            with open(self.config_file, 'r') as f:
                data = json.load(f)
                
            self.min_neighbors = data['min_neighbors']
            self.max_neighbors = data['max_neighbors']
            
            resources = data['resources']
            for node_id in resources:
                file_list = resources[node_id]
                self.graph.add_node(node_id, resources=set(file_list))
            
            self.graph.add_edges_from(data['edges'])
            
            print(f"Rede carregada: {self.graph.number_of_nodes()} nós e {self.graph.number_of_edges()} conexões.")
            
            self._validate()
            
        except FileNotFoundError:
            print(f"Erro: Arquivo '{self.config_file}' não encontrado.")
        except json.JSONDecodeError:
            print("Erro: O arquivo de configuração não é um JSON válido.")

    def _validate(self):
        print("\n--- Iniciando Validações ---")
        errors = []

        if not nx.is_connected(self.graph):
            errors.append("ERRO: A rede está particionada (existem nós isolados).")
        
        for node in self.graph.nodes():
            degree = self.graph.degree[node]
            resources = self.graph.nodes[node]['resources']
            
            if not (self.min_neighbors <= degree <= self.max_neighbors):
                errors.append(f"ERRO: Nó {node} tem {degree} vizinhos (Permitido: {self.min_neighbors}-{self.max_neighbors}).")
            
            if not resources:
                errors.append(f"ERRO: Nó {node} não possui recursos.")

        if list(nx.selfloop_edges(self.graph)):
            errors.append("ERRO: Existem laços (nós conectados a si mesmos).")

        if errors:
            for e in errors:
                print(e)
            print(">>> A REDE É INVÁLIDA <<<")
        else:
            print(">>> SUCESSO: A REDE É VÁLIDA E ESTÁ PRONTA! <<<")

    def draw(self):
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', 
                node_size=2000, font_size=10, font_weight='bold')
        plt.title("Visualização da Rede P2P")
        plt.show()