import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 11})

def gerar_graficos(filename=None):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    
    data_dir = os.path.join(parent_dir, 'data')
    csv_path = os.path.join(data_dir, 'resultados_benchmark.csv')

    if not os.path.exists(csv_path):
        print(f"Erro: '{csv_path}' não encontrado. Rode o benchmark.py primeiro!")
        return

    df = pd.read_csv(csv_path)
    
    df['Topologia'] = df['Topologia'].str.replace('json/', '')

    # ==============================================================================
    # GRÁFICO 1: EFICIÊNCIA CLÁSSICA (Flooding vs Random Walk)
    # Mostra o problema de escala do Flooding na Rede Grande
    # ==============================================================================
    print("Gerando Gráfico 1: Eficiência Clássica...")
    
    df_eff = df[
        (df['Topologia'] == filename) & 
        (df['Algoritmo'].isin(['Flooding', 'Random Walk']))
    ]

    plt.figure(figsize=(8, 6))
    ax1 = sns.barplot(x='Algoritmo', y='Mensagens', data=df_eff, palette="viridis")
    
    plt.title('Flooding vs Random Walk (Rede Grande)', fontsize=14, pad=15)
    plt.ylabel('Total de Mensagens')
    plt.xlabel('') 
    
    for i in ax1.containers:
        ax1.bar_label(i, padding=3)

    plt.tight_layout()
    plt.savefig(os.path.join(data_dir, 'grafico_eficiencia.png'), dpi=300)
    plt.close()

    # ==============================================================================
    # GRÁFICO 2: O PODER DO CACHE (Comparativo Geral)
    # Mostra Walk e Flood: Antes (Cold) e Depois (Warm)
    # ==============================================================================
    print("Gerando Gráfico 2: Cache Completo...")

    df_cache = df[
        (df['Topologia'] == filename) & 
        (df['Algoritmo'].str.contains('Informed'))
    ]

    cores_personalizadas = {
        'Informed Walk (Cold)': '#ff9999',  
        'Informed Walk (Warm)': '#99ff99',  
        'Informed Flooding (Cold)': '#ff6666', 
        'Informed Flooding (Warm)': '#66b3ff'  
    }

    plt.figure(figsize=(10, 6))
    
    ax2 = sns.barplot(
        x='Algoritmo', 
        y='Mensagens', 
        data=df_cache, 
        palette=cores_personalizadas,
        order=['Informed Walk (Cold)', 'Informed Walk (Warm)', 'Informed Flooding (Cold)', 'Informed Flooding (Warm)']
    )
    
    plt.title('Impacto do Cache: Aprendizado (Cold) vs Memória (Warm)', fontsize=14, pad=15)
    plt.ylabel('Mensagens Necessárias')
    plt.xlabel('')
    plt.xticks(rotation=15) 
    
    for i in ax2.containers:
        ax2.bar_label(i, padding=3)

    plt.tight_layout()
    plt.savefig(os.path.join(data_dir, 'grafico_cache.png'), dpi=300)
    plt.close()

    print(f"\n✅ Gráficos atualizados salvos em: {data_dir}")