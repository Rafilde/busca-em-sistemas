from typing import Dict, Set, Optional

class Node:
    def __init__(self, node_id: str):
        self.id = node_id
        self.neighbors: Set[str] = set()        
        self.resources: Set[str] = set()        
        self.cache: Dict[str, str] = {}        

    def add_neighbor(self, node_id: str):
        if node_id != self.id:
            self.neighbors.add(node_id)

    def add_resource(self, resource_id: str):
        self.resources.add(resource_id)

    def has_resource(self, resource_id: str) -> bool:
        return resource_id in self.resources

    def get_cache(self, resource_id: str) -> Optional[str]:
        return self.cache.get(resource_id)

    def update_cache(self, resource_id: str, location: str):
        self.cache[resource_id] = location
    
    def clear_cache(self):
        self.cache.clear()

    def __repr__(self):
        return f"Node({self.id})"