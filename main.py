from p2p_network import P2PNetwork

def main():
    try:
        rede = P2PNetwork("network.json")
    except ValueError:
        print("Abortando: Configuração inválida.")
        return
    
    # rede.draw() 

if __name__ == "__main__":
    main()