from algorithms import SearchEngine
from p2p_network import P2PNetwork

def main():
    try:
        rede = P2PNetwork("network.json")
    except ValueError:
        print("Abortando: Configuração inválida.")
        return
    
    # rede.draw() 

    search = SearchEngine(rede.graph)

    result = search.run_search(
        start_node='n1',
        target_resource="jogo_se.exe",
        ttl=10,
        algo='flooding'
    )

    print("\nRELATÓRIO FINAL:")
    print(f"Sucesso: {result['success']}")
    print(f"Mensagens Trocadas: {result['msgs']}")
    print(f"Nós envolvidos: {result['nodes']}")
    print(f"Nó final: {result.get('final_node', 'Nenhum')}")

if __name__ == "__main__":
    main()