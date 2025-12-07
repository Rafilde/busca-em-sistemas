from domain.network import Network


class NetworkValidator:
    def validate(self, network: Network) -> bool:
        print("\n--- Validando Regras da Rede ---")
        errors = []
        nodes = network.get_all_nodes()

        if not nodes:
            print("Erro Crítico: A rede está vazia.")
            return False

        start_node = nodes[0]
        visited = {start_node.id}
        queue = [start_node]

        while queue:
            current = queue.pop(0)
            for neighbor_id in current.neighbors:
                if neighbor_id not in visited:
                    visited.add(neighbor_id)
                    neighbor_node = network.get_node(neighbor_id)
                    if neighbor_node:
                        queue.append(neighbor_node)
        
        if len(visited) != len(nodes):
            errors.append(f"ERRO: Rede Particionada! Apenas {len(visited)} de {len(nodes)} nós são alcançáveis.")

        for node in nodes:
            degree = len(node.neighbors)
            
            if not (network.min_neighbors <= degree <= network.max_neighbors):
                errors.append(f"ERRO: Nó {node.id} tem {degree} vizinhos (Permitido: {network.min_neighbors}-{network.max_neighbors}).")
            
            if not node.resources:
                errors.append(f"ERRO: Nó {node.id} não possui nenhum recurso.")

        if errors:
            print(">>> A REDE É INVÁLIDA <<<")
            for e in errors: print(f" - {e}")
            return False
        
        print(">>> SUCESSO: Rede Válida e Pronta! <<<")
        return True