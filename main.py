from network.p2p_network import P2PNetwork
from network.validator import NetworkValidator
from network.visualizer import NetworkVisualizer
from search.engine import SearchEngine 

def main():
    try:
        rede = P2PNetwork("network.json")
        if not NetworkValidator.validate(rede): return
    except Exception as e:
        print(e); return

    search = SearchEngine(rede.graph)

    # NetworkVisualizer.draw(rede)

    search.run_search('flooding', 'n1', 'dados.csv', 5)

    search.run_search('random_walk', 'n1', 'dados.csv', 10)
    
    search.run_search('informed_random_walk', 'n1', 'dados.csv', 10)
    
    search.run_search('informed_flooding', 'n1', 'dados.csv', 10)

    # search.run_search('informed_random_walk', 'n1', 'dados.csv', 10)
    
    # search.run_search('informed_flooding', 'n1', 'dados.csv', 10)

    # search.run_search('informed_random_walk', 'n1', 'dados.csv', 10)
    
    # search.run_search('informed_flooding', 'n1', 'dados.csv', 10)

    # search.run_search('informed_random_walk', 'n1', 'dados.csv', 10)
    
    # search.run_search('informed_flooding', 'n1', 'dados.csv', 10)

    # search.run_search('informed_random_walk', 'n1', 'dados.csv', 10)
    
    # search.run_search('informed_flooding', 'n1', 'dados.csv', 10)

if __name__ == "__main__":
    main()