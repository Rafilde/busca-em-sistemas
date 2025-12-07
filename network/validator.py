import networkx as nx

class NetworkValidator:
    @staticmethod
    def validate(network):
        
        print("\n--- Iniciando Validações ---")
        graph = network.graph
        errors = []

        if not nx.is_connected(graph):
            errors.append("ERRO: A rede está particionada (existem nós isolados).")
        
        for node in graph.nodes():
            degree = graph.degree[node]
            resources = graph.nodes[node]['resources']
            
            if not (network.min_neighbors <= degree <= network.max_neighbors):
                errors.append(f"ERRO: Nó {node} tem {degree} vizinhos (Permitido: {network.min_neighbors}-{network.max_neighbors}).")
            
            if not resources:
                errors.append(f"ERRO: Nó {node} não possui recursos.")

        if list(nx.selfloop_edges(graph)):
            errors.append("ERRO: Existem laços (nós conectados a si mesmos).")

        if errors:
            for e in errors:
                print(e)
            print(">>> A REDE É INVÁLIDA <<<")
            return False
        else:
            print(">>> SUCESSO: A REDE É VÁLIDA! <<<")
            return True