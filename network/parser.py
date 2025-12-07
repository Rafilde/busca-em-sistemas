import json
from domain.network import Network
from domain.node import Node

class NetworkConfigParser:
    def parse(self, filepath: str) -> Network:
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
        except Exception as e:
            raise ValueError(f"Erro ao ler arquivo: {e}")

        num_nodes = data.get('num_nodes')
        if not isinstance(num_nodes, int) or num_nodes <= 0:
            raise ValueError("O parâmetro 'num_nodes' deve ser um inteiro positivo.")

        network = Network(
            min_neighbors=data.get('min_neighbors', 1),
            max_neighbors=data.get('max_neighbors', 4)
        )

        valid_node_ids = set()
        for i in range(1, num_nodes + 1):
            node_id = f"n{i}"
            network.add_node(Node(node_id))
            valid_node_ids.add(node_id)

        resources = data.get('resources', {})
        for node_id, res_list in resources.items():
            if node_id not in valid_node_ids:
                raise ValueError(f"Erro no JSON: Recurso atribuído ao nó '{node_id}', mas 'num_nodes' vai apenas até n{num_nodes}.")
            
            node = network.get_node(node_id)
            for res_id in res_list:
                node.add_resource(res_id)

        edges = data.get('edges', [])
        for edge in edges:
            if len(edge) != 2:
                raise ValueError(f"Aresta inválida: {edge}")
            u, v = edge
            
            if u == v:
                raise ValueError(f"Erro: Self-loop detectado no nó {u}.")
            
            if u not in valid_node_ids or v not in valid_node_ids:
                 raise ValueError(f"Erro: Aresta tenta conectar nó inexistente ({u}-{v}). Limite é n{num_nodes}.")

            network.add_edge(u, v)

        return network