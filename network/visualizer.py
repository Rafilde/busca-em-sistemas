import networkx as nx
import matplotlib.pyplot as plt

class NetworkVisualizer:
    @staticmethod
    def draw(network):
        plt.figure(figsize=(8, 6))
        
        graph = network.graph
        pos = nx.spring_layout(graph, seed=42) 
        
        nx.draw(
            graph, pos, 
            with_labels=True, 
            node_color='lightblue', 
            node_size=2000, 
            font_size=10, 
            font_weight='bold',
            edge_color='gray'
        )
        
        plt.title("Visualização da Rede P2P")
        plt.show()