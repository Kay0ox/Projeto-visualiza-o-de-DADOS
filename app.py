import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página Define o título da aba e um layout mais largo para aproveitar melhor o espaço na tela.
st.set_page_config(page_title="Painel de Vendas", layout="wide")

# Carregando os dados
#Usei cache para evitar recarregar os dados toda vez que você interage com o painel.
@st.cache_data
def carregar_dados():
    vendas = pd.read_csv("fato_vendas.csv")
    produtos = pd.read_csv("dim_produtos.csv")
    clientes = pd.read_csv("dim_clientes.csv")
    vendedores = pd.read_csv("dim_vendedores.csv")
    fornecedores = pd.read_csv("dim_fornecedores.csv")

    df = vendas.merge(produtos, on="id_produto") \
              .merge(clientes, on="id_cliente") \
              .merge(vendedores, on="id_vendedor") \
              .merge(fornecedores, on="fornecedor_id")

    df["data"] = pd.to_datetime(df["data"])
    df["mes"] = df["data"].dt.to_period("M")
    df["lucro"] = df["preco_total"] - (df["quantidade"] * df["preco_unitario"])
    return df

# Dados
base_dados = carregar_dados()

# Filtros laterais
st.sidebar.header("Filtros")
mes_escolhido = st.sidebar.selectbox("Selecione o mês:", base_dados['mes'].astype(str).unique())
df_filtrado = base_dados[base_dados['mes'].astype(str) == mes_escolhido]

# Abas
aba1, aba2, aba3 = st.tabs(["📊 Vendas", "📦 Produtos & Clientes", "📈 Relatórios"])

with aba1:
    st.header("Resumo de Vendas")
    fig_vendas = px.bar(df_filtrado, x="nome_vendedor", y="preco_total", color="categoria", barmode="group",
                         title="Total de Vendas por Vendedor")
    st.plotly_chart(fig_vendas, use_container_width=True)

with aba2:
    st.header("Análise de Produtos")
    fig_prod = px.pie(base_dados, names='nome_produto', values='quantidade', title="Participação dos Produtos")
    st.plotly_chart(fig_prod, use_container_width=True)

    st.header("Clientes por Estado")
    fig_cli = px.histogram(base_dados, x='estado_x', color='estado_x', title="Distribuição dos Clientes por Estado")
    st.plotly_chart(fig_cli, use_container_width=True)

with aba3:
    st.header("Relatórios Analíticos")
    st.subheader("Lucro por Produto")
    lucro_prod = base_dados.groupby("nome_produto")["lucro"].sum().reset_index()
    fig_lucro = px.bar(lucro_prod, x="nome_produto", y="lucro", title="Lucro Total por Produto")
    st.plotly_chart(fig_lucro, use_container_width=True)

    st.subheader("Distribuição de Vendas por Região")
    fig_regiao = px.box(base_dados, x="região", y="preco_total", title="Distribuição de Vendas por Região")
    st.plotly_chart(fig_regiao, use_container_width=True)

st.caption("Projeto 01 – Painel com Informações Analíticas sobre Vendas | Desenvolvido em Python + Streamlit + Plotly")
