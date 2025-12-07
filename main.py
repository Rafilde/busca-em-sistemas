import sys
import os

from network.parser import NetworkConfigParser
from network.visualizer import NetworkVisualizer
from tools.plot_graphs import gerar_graficos

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from tools.benchmark import rodar_benchmark
from tools.gerador import gerar_topologia, UNIQUE_TARGET_RESOURCE

USE_GENERATOR = True

CONFIG_FILENAME = "rede_teste_unica.json" 
NUM_NODES = 20           
MIN_NEIGHBORS = 2
MAX_NEIGHBORS = 6 

TARGET_RESOURCE = UNIQUE_TARGET_RESOURCE 
START_NODE = "n1"
CUSTOM_TTL = 15                         


def main():
    print("\n=============================================")
    print(f"🔄 Modo de Operação: {'AUTOMÁTICO (GERANDO NOVO JSON)' if USE_GENERATOR else 'MANUAL (USANDO ARQUIVO EXISTENTE)'}")
    print("=============================================")

    path_arquivo_json = ""

    if USE_GENERATOR:
    
        path_arquivo_json = gerar_topologia(
            CONFIG_FILENAME, 
            num_nodes=NUM_NODES, 
            min_neighbors=MIN_NEIGHBORS, 
            max_neighbors=MAX_NEIGHBORS
        )

    else:

        project_root = os.path.dirname(os.path.abspath(__file__))
        path_arquivo_json = os.path.join(project_root, 'json', CONFIG_FILENAME)


    # parser = NetworkConfigParser()
    # try:
    #     rede = parser.parse(path_arquivo_json)
    #     print(f"✅ Rede carregada com sucesso! ({len(rede.get_all_nodes())} nós)")
    # except Exception as e:
    #     print(f"Erro fatal ao carregar/parsear '{path_arquivo_json}': {e}")
    #     return
    # NetworkVisualizer.draw(
    #     rede
    # )
    
    rodar_benchmark(
        arquivos_a_testar=[path_arquivo_json],
        target=TARGET_RESOURCE,
        start_node=START_NODE,
        custom_ttl=CUSTOM_TTL
    )

    print("\n--- GERANDO GRÁFICOS ---")
    gerar_graficos(filename=CONFIG_FILENAME)
    
    print("=============================================\n")

if __name__ == "__main__":
    main()