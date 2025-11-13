# 📈 Gráfico Histórico de Jogadores - GTA V (Versão sem API)

Este projeto utiliza Python, Pandas e Plotly para criar um gráfico de linha interativo que visualiza a média mensal de jogadores de Grand Theft Auto V na Steam, com dados históricos desde 2015.

O gráfico é renderizado em modo escuro, com linha verde e inclui filtros de tempo interativos (3 meses, 1 ano, 6 anos, etc.).

---

## 🚀 Funcionalidades

* **Gráfico Interativo:** Feito com Plotly, abre no seu navegador.
* **Zoom e "Tooltip":** Passe o mouse sobre o gráfico para ver os dados de cada mês e use o scroll para dar zoom.
* **Modo Escuro:** O gráfico usa um tema escuro (`plotly_dark`).
* **Linha Verde:** A linha de dados é estilizada na cor verde.
* **Filtros de Tempo:** Inclui botões para filtrar o gráfico por "3 meses", "1 ano", "Tudo", etc.
* **Slider de Tempo:** Uma barra de rolagem na parte inferior permite selecionar períodos de tempo personalizados.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Pandas:** Para carregar e processar os dados do arquivo CSV.
* **Plotly:** Para criar e exibir o gráfico interativo.

---

## ⚙️ 1. Instalação e Configuração

Siga estes passos para preparar o ambiente.

### Passo 1: Instalar as Bibliotecas

Abra seu terminal na pasta do projeto e instale as dependências.

```bash
# Instale o pandas e o plotly
pip install pandas plotly
```
(Se `pip` não for reconhecido, use `py -m pip install pandas plotly`)

### Passo 2: Preparar o Arquivo de Dados (Obrigatório)
Este script não usa a API. Ele precisa de um arquivo chamado `gta_data.csv` na mesma pasta.

**Obtenha os Dados:** Vá para https://steamcharts.com/app/271590.

**Copie os Dados:** Role para baixo e copie os dados da tabela (desde o mês atual até "April 2015").

**Cole no CSV:** Crie um arquivo `gta_data.csv` no VS Code.

**FORMATE O ARQUIVO (Mais Importante!):** O seu arquivo CSV deve ter este formato exato:

  * **A Linha 1** deve ser exatamente: `mes,jogadores`

  * **A Linha 2** deve ser o primeiro dado (ex: `October 2025,57282.5`)

  * **Não pode haver linhas extras no topo (como `"Last 30 Days"`).**

Os números não podem ter vírgulas (ex: `57,282.5` está errado; `57282.5` está certo).

### Exemplo de como o `gta_data.csv` deve começar:
```
mes,jogadores
October 2025,57282.5
September 2025,55605.2
August 2025,68245.6
```

# 🖥️ 2. Como Executar
Depois que as bibliotecas estiverem instaladas e o gta_data.csv estiver formatado e salvo:

Abra o terminal do VS Code (`Exibir -> Terminal`).

```bash
Digite o comando para executar o script:
python grafico_interativo.py
```

(ou `py grafico_interativo.py`)

O script será executado no terminal e abrirá automaticamente o gráfico interativo no seu navegador padrão.
