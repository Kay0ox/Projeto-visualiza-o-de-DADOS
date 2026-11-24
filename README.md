# Visualização de Dados: Dashboards em Power BI e Python

Projetos da disciplina de **Visualização de Dados** (Ciência da Computação, UNIPÊ), avaliados pelo Prof. Ricardo Roberto de Lima. Trabalho feito em equipe com os colaboradores do repositório.

## Projetos

### 1. Painel de Vendas interativo (Python + Streamlit)

Arquivo `app.py`. Painel web que junta uma tabela de vendas com as tabelas de produtos, clientes, vendedores e fornecedores (modelo estrela) e mostra:

- Resumo de vendas do mês escolhido no filtro lateral
- Análise de produtos e clientes por estado
- Lucro por produto e distribuição de vendas por região

**Tecnologias:** Python, Pandas, Plotly, Streamlit

### 2. Vendas Globais (Power BI)

Arquivo `Vendas Globais Trabalho.pbix`: dashboard de vendas globais.

### 3. Marketing (Power BI)

Arquivo `Marketing Trabalho.pbix`: dashboard de indicadores de marketing.

O arquivo `Dashboard final.pdf` mostra os painéis exportados, para quem não tem o Power BI.

## Dados

Os dados estão em CSV, no formato de modelo estrela:

- `fato_vendas.csv`: tabela fato (vendas)
- `dim_produtos.csv`, `dim_clientes.csv`, `dim_vendedores.csv`, `dim_fornecedores.csv`: tabelas de dimensão

## Como rodar o painel em Python

```bash
git clone https://github.com/Kay0ox/Projeto-visualiza-o-de-DADOS.git
cd Projeto-visualiza-o-de-DADOS
pip install streamlit pandas plotly
streamlit run app.py
```

Os arquivos `.pbix` abrem no Power BI Desktop.

## Autor

**Kayo Victor Vilar Silva**: [LinkedIn](https://www.linkedin.com/in/kayo-victor-vilar-525205373/) · [GitHub](https://github.com/Kay0ox)
