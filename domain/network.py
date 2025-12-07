from typing import List, Dict, Optional
from domain.node import Node

class Network:
    def __init__(self, min_neighbors: int, max_neighbors: int):
        self.nodes: Dict[str, Node] = {}
        self.min_neighbors = min_neighbors
        self.max_neighbors = max_neighbors

    def add_node(self, node: Node):
        self.nodes[node.id] = node

    def get_node(self, node_id: str) -> Optional[Node]:
        return self.nodes.get(node_id)
    
    def get_all_nodes(self) -> List[Node]:
        return list(self.nodes.values())

    def add_edge(self, u: str, v: str):
        if u in self.nodes and v in self.nodes:
            self.nodes[u].add_neighbor(v)
            self.nodes[v].add_neighbor(u)
    
    def clear_all_caches(self):
        for node in self.nodes.values():
            node.clear_cache()