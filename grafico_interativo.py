import pandas as pd
import plotly.express as px
# A biblioteca 'datetime' não é mais necessária se o pandas lidar com tudo
# Mas vamos precisar dela para os cálculos de data, então é bom importar
from datetime import datetime

# --- Configuração ---
NOME_ARQUIVO_CSV = 'gta_data.csv'
# --------------------

print(f"Tentando carregar o arquivo: {NOME_ARQUIVO_CSV}")

# --- Carregando os dados (mesmo código de antes) ---
try:
    dados = pd.read_csv(NOME_ARQUIVO_CSV)
except FileNotFoundError:
    print(f"\n--- ERRO ---")
    print(f"Arquivo '{NOME_ARQUIVO_CSV}' não encontrado.")
    exit()
except pd.errors.ParserError:
    print("Ocorreu um erro ao ler o CSV. Tentando com separador ';'")
    try:
        dados = pd.read_csv(NOME_ARQUIVO_CSV, sep=';')
    except Exception as e:
        print(f"Erro ao tentar com ';': {e}")
        exit()
except Exception as e:
    print(f"Um erro inesperado ocorreu: {e}")
    exit()

print("Arquivo CSV carregado com sucesso!")

# === 1. MUDANÇA IMPORTANTE: CONVERTER A DATA ===
# Precisamos converter a coluna de texto 'mes' (ex: "October 2025")
# para um objeto de data real que o Plotly entenda.
try:
    dados['mes'] = pd.to_datetime(dados['mes'])
except Exception as e:
    print(f"Erro ao converter a coluna 'mes' para data: {e}")
    print("Verifique o formato das datas no seu CSV.")
    exit()

# --- Tratamento dos Dados ---
# Inverte a ordem para o gráfico ir de 2015 para 2025
# (O Plotly pode lidar com isso automaticamente, mas é bom manter)
dados = dados.sort_values(by='mes') # Garante que está em ordem de data

print("Gerando o gráfico interativo com filtros...")

# --- Criação do Gráfico Interativo ---
fig = px.line(
    dados,
    x='mes', # Agora esta é uma coluna de DATA
    y='jogadores',
    title='Média de Jogadores de GTA V no Steam (2015-Presente)',
    markers=True,
    labels={'mes': 'Data', 'jogadores': 'Média de Jogadores'},
    color_discrete_sequence=['#2CA02C'] # Mantém sua linha verde
)

# --- Configuração do Layout (Modo Escuro e Filtros) ---
fig.update_layout(
    template='plotly_dark', # Mantém seu modo escuro
    xaxis_title="Data",
    yaxis_title="Número de Jogadores"
)

# === 2. MUDANÇA IMPORTANTE: ADICIONAR OS BOTÕES DE FILTRO ===
fig.update_xaxes(
    # Adiciona os botões de filtro de tempo
    rangeselector=dict(
        buttons=list([
            # O 'count' é o número, e 'step' é a unidade (mês, ano)
            dict(count=3, label="3 meses", step="month", stepmode="backward"),
            dict(count=6, label="6 meses", step="month", stepmode="backward"),
            dict(count=1, label="1 ano", step="year", stepmode="backward"),
            dict(count=3, label="3 anos", step="year", stepmode="backward"),
            dict(count=6, label="6 anos", step="year", stepmode="backward"),
            dict(label="Tudo", step="all") # Botão para ver tudo
        ]),
        bgcolor="#333", # Cor de fundo dos botões (para o modo escuro)
        activecolor="#555" # Cor do botão ativo
    ),
    # Adiciona a "barra de rolagem" (slider) na parte de baixo
    rangeslider=dict(
        visible=True
    ),
    type="date" # Diz ao eixo X que ele é do tipo "data"
)

fig.show()

print("Gráfico pronto. Verifique seu navegador!")
