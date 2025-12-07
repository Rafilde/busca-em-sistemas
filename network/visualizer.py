import networkx as nx
import matplotlib.pyplot as plt

class NetworkVisualizer:
    @staticmethod
    def draw(manual_network):
        
        print("Gerando visualização gráfica...")
        
        G = nx.Graph()
        
        nodes = manual_network.get_all_nodes()
        
        for node in nodes:
            G.add_node(node.id)
            
            for neighbor_id in node.neighbors:
                G.add_edge(node.id, neighbor_id)
        
        plt.figure(figsize=(10, 8))
        
        pos = nx.spring_layout(G, seed=42) 
        
        nx.draw(
            G, pos, 
            with_labels=True, 
            node_color='lightblue', 
            node_size=2000, 
            font_size=10, 
            font_weight='bold',
            edge_color='gray',
            width=1.5
        )
        
        plt.title("Visualização da Rede P2P")
        plt.show()