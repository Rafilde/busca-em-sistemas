from network.parser import NetworkConfigParser     
from network.validator import NetworkValidator
from network.visualizer import NetworkVisualizer
from search.engine import SearchEngine           

def main():
    config_file = "network.json"

    parser = NetworkConfigParser()
    try:
        rede = parser.parse(config_file)
        print(f"Rede carregada com sucesso! ({len(rede.get_all_nodes())} nós)")
    except Exception as e:
        print(f"Erro fatal ao carregar/parsear: {e}")
        return

    validator = NetworkValidator()
    
    if not validator.validate(rede):
        print("Abortando: Rede inválida.")
        return
    
    # NetworkVisualizer.draw(rede)

    search = SearchEngine(rede)

    print("\n--- INICIANDO TESTES ---")

    search.run_search('flooding', 'n1', 'dados.csv', 5)

    search.run_search('random_walk', 'n1', 'dados.csv', 10)
    
    print("\n>> Teste de Aprendizado (Cache) <<")
    
    search.run_search('informed_random_walk', 'n1', 'dados.csv', 10)
    
    search.run_search('informed_flooding', 'n1', 'dados.csv', 5)

    search.run_search('informed_random_walk', 'n1', 'dados.csv', 10)
    
    search.run_search('informed_flooding', 'n1', 'dados.csv', 5)

    search.run_search('informed_random_walk', 'n1', 'dados.csv', 10)
    
    search.run_search('informed_flooding', 'n1', 'dados.csv', 5)

if __name__ == "__main__":
    main()