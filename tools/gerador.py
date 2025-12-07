import json
import random
import networkx as nx
import os

UNIQUE_TARGET_RESOURCE = "chave_mestra_secreta.bin"

def gerar_topologia(filename, num_nodes, min_neighbors, max_neighbors):
    print(f"--- Gerando {filename} ({num_nodes} nós) ---")
    
    while True:
        m = max(1, min_neighbors)
        if m >= num_nodes: m = num_nodes - 1
        
        G = nx.barabasi_albert_graph(num_nodes, m)
        
        if not nx.is_connected(G):
            continue 
            
        degrees = [d for n, d in G.degree()]
        if min(degrees) < min_neighbors or max(degrees) > max_neighbors:
            continue 
            
        break 

    resources_dict = {}
    
    mapping = {i: f"n{i+1}" for i in G.nodes()}
    G = nx.relabel_nodes(G, mapping)
    
    files_pool = [f"arquivo_{i}.txt" for i in range(1, 20)]
    
    all_nodes = list(G.nodes())
    unique_node = random.choice(all_nodes) 
    
    for node in G.nodes():
        qtd = random.randint(1, 5)
        
        my_files = random.sample(files_pool, qtd)
        
        if node == unique_node:
            my_files.append(UNIQUE_TARGET_RESOURCE)
            
        resources_dict[node] = my_files

    output_data = {
        "num_nodes": num_nodes,
        "min_neighbors": min_neighbors,
        "max_neighbors": max_neighbors,
        "unique_target_location": unique_node,
        "resources": resources_dict,
        "edges": list(G.edges())
    }

    pasta_destino = 'json'

    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    
    caminho_completo = os.path.join(pasta_destino, filename)

    with open(caminho_completo, 'w') as f:
        json.dump(output_data, f, indent=2)
    
    print(f"✅ Arquivo salvo em: {caminho_completo}")
    print(f"   (Recurso ÚNICO '{UNIQUE_TARGET_RESOURCE}' está no nó: {unique_node})")

if __name__ == "__main__":
    gerar_topologia("rede_pequena.json", num_nodes=10, min_neighbors=2, max_neighbors=5)
    gerar_topologia("rede_media.json", num_nodes=50, min_neighbors=2, max_neighbors=10)
    gerar_topologia("rede_grande.json", num_nodes=100, min_neighbors=3, max_neighbors=20)