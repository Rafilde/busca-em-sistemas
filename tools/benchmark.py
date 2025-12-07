import sys
import os
import csv
import time

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from network.validator import NetworkValidator
from network.parser import NetworkConfigParser
from search.engine import SearchEngine

def rodar_benchmark():
    arquivos = ["json/rede_pequena.json", "json/rede_media.json", "json/rede_grande.json"]
    
    data_dir = os.path.join(parent_dir, 'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"📁 Pasta '{data_dir}' criada.")

    csv_file = os.path.join(data_dir, 'resultados_benchmark.csv')
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Topologia', 'Algoritmo', 'Sucesso', 'Mensagens', 'Nos Visitados', 'Tempo(ms)', 'Obs'])

        print(f"--- INICIANDO BENCHMARK ---")

        for arquivo in arquivos:
            print(f"\n>> Processando: {arquivo}")
            path_completo = os.path.join(parent_dir, arquivo)

            try:
                parser = NetworkConfigParser()
                rede = parser.parse(path_completo)
                
                val = NetworkValidator()
                if not val.validate(rede):
                    print(f"Ignorando {arquivo} (Inválido)")
                    continue
            except Exception as e:
                print(f"Erro ao abrir {arquivo}: {e}")
                continue

            search = SearchEngine(rede)
            target = "chave_mestra_secreta.bin"
            start_node = "n1"
            
            total_nodes = len(rede.get_all_nodes())
            ttl = int(total_nodes / 2) + 2
            
            # --- 1. FLOODING (Padrão) ---
            start = time.time()
            res = search.run_search('flooding', start_node, target, ttl)
            end = time.time()
            writer.writerow([arquivo, 'Flooding', res['success'], res['msgs'], res['nodes'], round((end-start)*1000, 2), '-'])
            print(f"   Flooding: {res['msgs']} msgs")

            # --- 2. RANDOM WALK (Padrão) ---
            rede.clear_all_caches()
            start = time.time()
            res = search.run_search('random_walk', start_node, target, ttl * 2) 
            end = time.time()
            writer.writerow([arquivo, 'Random Walk', res['success'], res['msgs'], res['nodes'], round((end-start)*1000, 2), '-'])
            print(f"   Random Walk: {res['msgs']} msgs")

            # --- 3. INFORMED WALK (Aprendizado) ---
            rede.clear_all_caches()
            start = time.time()
            res1 = search.run_search('informed_random_walk', start_node, target, ttl * 2)
            end = time.time()
            writer.writerow([arquivo, 'Informed Walk (Cold)', res1['success'], res1['msgs'], res1['nodes'], round((end-start)*1000, 2), 'Cache Vazio'])
            print(f"   Informed Walk (Cold): {res1['msgs']} msgs")

            # --- 4. INFORMED WALK (Uso Cache) ---
            start = time.time()
            res2 = search.run_search('informed_random_walk', start_node, target, ttl * 2)
            end = time.time()
            writer.writerow([arquivo, 'Informed Walk (Warm)', res2['success'], res2['msgs'], res2['nodes'], round((end-start)*1000, 2), 'Cache Cheio'])
            print(f"   Informed Walk (Warm): {res2['msgs']} msgs")

            # --- 5. INFORMED FLOODING (Aprendizado) ---
            # Limpamos o cache de novo para testar o aprendizado do Flooding do zero
            rede.clear_all_caches()
            start = time.time()
            res3 = search.run_search('informed_flooding', start_node, target, ttl)
            end = time.time()
            writer.writerow([arquivo, 'Informed Flooding (Cold)', res3['success'], res3['msgs'], res3['nodes'], round((end-start)*1000, 2), 'Cache Vazio'])
            print(f"   Informed Flood (Cold): {res3['msgs']} msgs")

            # --- 6. INFORMED FLOODING (Uso Cache) ---
            start = time.time()
            res4 = search.run_search('informed_flooding', start_node, target, ttl)
            end = time.time()
            writer.writerow([arquivo, 'Informed Flooding (Warm)', res4['success'], res4['msgs'], res4['nodes'], round((end-start)*1000, 2), 'Cache Cheio'])
            print(f"   Informed Flood (Warm): {res4['msgs']} msgs")

    print(f"\n✅ Concluído! Arquivo salvo em: '{csv_file}'")

if __name__ == "__main__":
    rodar_benchmark()