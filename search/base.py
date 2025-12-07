class SearchAlgorithm:
    def __init__(self, network):
        self.network = network

    def run(self, start_node, target_resource, ttl):
        raise NotImplementedError("Implementar no algoritmo específico")
    
    def display_report(self, algo_name, result):
        print(f"\n{'='*15} RELATÓRIO: {algo_name.upper()} {'='*15}")
        
        if result['success']:
            origem = f"(via {result['source'].upper()})" if 'source' in result else ""
            icon = "⚡" if 'source' in result and result['source'] == 'cache' else "✅"
            
            print(f"{icon} STATUS:        SUCESSO {origem}")
            print(f"📍 ENCONTRADO EM: {result.get('final_node')}")
        else:
            print(f"❌ STATUS:        FALHA (Recurso não encontrado)")
            print(f"💀 MOTIVO:        TTL expirou ou rede esgotada")

        print(f"📨 MENSAGENS:     {result['msgs']}")
        print(f"🌐 NÓS VISITADOS: {result['nodes']}")
        print("=" * (30 + len(algo_name) + 2))