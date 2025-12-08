# 🚀 Simulação Automatizada de Busca em Redes P2P

**Disciplina:** Computação Distribuída

**Professor(a):** Naboa das Chargas Mendonça

**Integrantes do Grupo:**
* Rafael Silva - Matrícula: 2212378
* Siwan Eden - Matrícula: 2220191
* Evandro Luz - Matrícula: 2220294

---

Este projeto simula e compara a eficiência de diferentes algoritmos de busca em redes Peer-to-Peer (P2P) não estruturadas. O fluxo é totalmente automatizado: a `main.py` serve como painel de controle, gerando a rede, executando o benchmark completo e plotando os gráficos de resultado.Você também pode gerar o grafo manualmente se quiser, bastaa mudar o `rede_teste_unica_json`

## ⚙️ Arquitetura do Projeto

O projeto segue um padrão modular (Domain-Driven Design), onde cada pasta tem uma responsabilidade clara, facilitando a manutenção e a expansão.

| Pasta | Responsabilidade | Exemplo de Arquivo |
| :--- | :--- | :--- |
| `domain/` | Lógica de Entidades (`Node`, `Network`). | `network.py`, `node.py` |
| `network/` | I/O e Validação de Rede. | `parser.py`, `validator.py`, `visualizer.py` |
| `search/` | Algoritmos de Busca. | `flooding.py`, `informed_flooding.py`, `random_walk.py`, `informed_random_walk.py` |
| `tools/` | Scripts de Automação e Utilitários. | `gerador.py`, `benchmark.py`, `plot_graphs.py` |
| `json/` | Armazena os arquivos de topologia (`.json`) gerados. Aqui você também pode criar manualmente seu json | `rede_teste_unica.json` |
| `data/` | **Resultados e Relatórios** (CSV e PNG). | `resultados_benchmark.csv`, gráficos |

---

## 🔍 Algoritmos Testados

O benchmark é projetado para comparar o custo de tráfego (mensagens) para seis variações de busca:

| Algoritmo | Estratégia | Objetivo no Teste |
| :--- | :--- | :--- |
| **Flooding** | Inundação total. | Medir o **Custo Máximo** de mensagens. |
| **Random Walk** | Caminhada aleatória. | Medir o **Custo Mínimo** de mensagens (probabilístico). |
| **Informed Walk (Cold/Warm)** | Random Walk com cache. | Provar a eficiência do cache na busca leve. |
| **Informed Flooding (Cold/Warm)** | Flooding com cache. | Provar que o cache funciona mesmo com o método mais pesado. |

---

## 🎯 Como Rodar o Projeto (Painel de Controle)

Toda a configuração da rede e o controle do fluxo estão centralizados no arquivo **`main.py`**.

### Pré-requisitos

Instale as bibliotecas necessárias (NetworkX, Matplotlib, Pandas, Seaborn):

```bash
pip install -r requirements.txt
```

### Rodar o código

```bash
python main.py
```
