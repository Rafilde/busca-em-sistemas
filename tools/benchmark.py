import sys
import os
import csv
import time

# Pega o diretório raiz do projeto para imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from network.validator import NetworkValidator
from network.parser import NetworkConfigParser
from search.engine import SearchEngine

def rodar_benchmark(arquivos_a_testar: list, target: str, start_node: str, custom_ttl: int):
    """
    Executa a bateria de testes de benchmark nos arquivos fornecidos.
    Recebe TTL fixo (custom_ttl) da main.py.
    """
    
    data_dir = os.path.join(parent_dir, 'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    # O CSV agora será salvo com um nome específico para o teste único
    csv_file = os.path.join(data_dir, 'resultados_benchmark.csv') 
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Topologia', 'Algoritmo', 'Sucesso', 'Mensagens', 'Nos Visitados', 'Tempo(ms)', 'Obs', 'TTL_Usado'])

        # AQUI VOCÊ SÓ RODA NO ARQUIVO ÚNICO PASSADO PELA MAIN
        for arquivo_path in arquivos_a_testar:
            # ----------------------------------------------------
            # O TTL NÃO É MAIS CALCULADO, USA O VALOR CUSTOMIZADO
            ttl = custom_ttl
            # ----------------------------------------------------
            
            # 1. Carrega e Valida
            try:
                parser = NetworkConfigParser()
                # O parse agora usa o caminho absoluto
                rede = parser.parse(arquivo_path)
                
                val = NetworkValidator()
                if not val.validate(rede):
                    print(f"Ignorando {arquivo_path} (Inválido)")
                    continue
            except Exception as e:
                print(f"Erro ao abrir {arquivo_path}: {e}")
                continue

            search = SearchEngine(rede)
            
            print(f"\n>> Processando: {os.path.basename(arquivo_path)} | TTL: {ttl}")
            
            # --- 1. FLOODING (Padrão) ---
            start = time.time()
            res = search.run_search('flooding', start_node, target, ttl)
            end = time.time()
            writer.writerow([os.path.basename(arquivo_path), 'Flooding', res['success'], res['msgs'], res['nodes'], round((end-start)*1000, 2), '-', ttl])
            print(f"   Flooding: {res['msgs']} msgs")

            # --- 2. RANDOM WALK (Padrão) ---
            rede.clear_all_caches()
            start = time.time()
            res = search.run_search('random_walk', start_node, target, ttl * 2) 
            end = time.time()
            writer.writerow([os.path.basename(arquivo_path), 'Random Walk', res['success'], res['msgs'], res['nodes'], round((end-start)*1000, 2), '-', ttl * 2])
            print(f"   Random Walk: {res['msgs']} msgs")

            # --- 3. INFORMED WALK (Aprendizado) ---
            rede.clear_all_caches()
            start = time.time()
            res1 = search.run_search('informed_random_walk', start_node, target, ttl * 2)
            end = time.time()
            writer.writerow([os.path.basename(arquivo_path), 'Informed Walk (Cold)', res1['success'], res1['msgs'], res1['nodes'], round((end-start)*1000, 2), 'Cache Vazio', ttl * 2])
            print(f"   Informed Walk (Cold): {res1['msgs']} msgs")

            # --- 4. INFORMED WALK (Uso Cache) ---
            start = time.time()
            res2 = search.run_search('informed_random_walk', start_node, target, ttl * 2)
            end = time.time()
            writer.writerow([os.path.basename(arquivo_path), 'Informed Walk (Warm)', res2['success'], res2['msgs'], res2['nodes'], round((end-start)*1000, 2), 'Cache Cheio', ttl * 2])
            print(f"   Informed Walk (Warm): {res2['msgs']} msgs")

            # --- 5. INFORMED FLOODING (Aprendizado) ---
            rede.clear_all_caches()
            start = time.time()
            res3 = search.run_search('informed_flooding', start_node, target, ttl)
            end = time.time()
            writer.writerow([os.path.basename(arquivo_path), 'Informed Flooding (Cold)', res3['success'], res3['msgs'], res3['nodes'], round((end-start)*1000, 2), 'Cache Vazio', ttl])
            print(f"   Informed Flood (Cold): {res3['msgs']} msgs")

            # --- 6. INFORMED FLOODING (Uso Cache) ---
            start = time.time()
            res4 = search.run_search('informed_flooding', start_node, target, ttl)
            end = time.time()
            writer.writerow([os.path.basename(arquivo_path), 'Informed Flooding (Warm)', res4['success'], res4['msgs'], res4['nodes'], round((end-start)*1000, 2), 'Cache Cheio', ttl])
            print(f"   Informed Flood (Warm): {res4['msgs']} msgs")

    print(f"\n✅ Concluído! Arquivo salvo em: '{csv_file}'")