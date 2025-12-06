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

    # fLooding ----------------------------------------------------
    result = search.run_search(
        start_node='n1',
        target_resource="dados.csv",
        ttl=5,
        algo='flooding'
    )

    print("\nRELATÓRIO FINAL:")
    print(f"Sucesso: {result['success']}")
    print(f"Mensagens Trocadas: {result['msgs']}")
    print(f"Nós envolvidos: {result['nodes']}")
    print(f"Nó final: {result.get('final_node', 'Nenhum')}")

    # Random Walk -------------------------------------------------

    result = search.run_search(
        start_node='n1',
        target_resource="dados.csv",
        ttl=5,
        algo='random_walk'
    )

    print("\nRELATÓRIO FINAL:")
    print(f"Sucesso: {result['success']}")
    print(f"Mensagens Trocadas: {result['msgs']}")
    print(f"Nós envolvidos: {result['nodes']}")
    print(f"Nó final: {result.get('final_node', 'Nenhum')}")

    # Informed Random Walk -----------------------------------------
    result = search.run_search(
        start_node='n1',
        target_resource="dados.csv",
        ttl=6,
        algo='informed_random_walk'
    )

    print("\nRELATÓRIO FINAL:")
    print(f"Sucesso: {result['success']}")
    print(f"Mensagens Trocadas: {result['msgs']}")
    print(f"Nós envolvidos: {result['nodes']}")
    print(f"Nó final: {result.get('final_node', 'Nenhum')}")

    # Informed Flooding --------------------------------------------
    # result = search.run_search(
    #     start_node='n1',
    #     target_resource="dados.csv",
    #     ttl=5,
    #     algo='informed_flooding'
    # )

    # print("\nRELATÓRIO FINAL:")
    # print(f"Sucesso: {result['success']}")
    # print(f"Mensagens Trocadas: {result['msgs']}")
    # print(f"Nós envolvidos: {result['nodes']}")
    # print(f"Nó final: {result.get('final_node', 'Nenhum')}")

if __name__ == "__main__":
    main()