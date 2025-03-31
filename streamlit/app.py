import streamlit as st
import pandas as pd
import duckdb
import plotly.express as px
import plotly.graph_objects as go
import os
from pathlib import Path

# Configuração da página
st.set_page_config(
    page_title="Dashboard de Saúde Mental",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Funções para carregar dados
@st.cache_data
def load_data():
    # Caminho para o DuckDB
    db_path = "C:/Users/Admin/Downloads/mental-health-de-zoomcamp/data/duckdb/mental_health.db"
    
    # Conectar ao DuckDB
    con = duckdb.connect(db_path)
    
    # Carregar os dados das tabelas transformadas
    facts = con.execute("SELECT * FROM fact_mental_health").fetchdf()
    geography = con.execute("SELECT * FROM dim_geography").fetchdf()
    
    con.close()
    
    return facts, geography

# Título do dashboard
st.title("🧠 Dashboard de Análise de Saúde Mental")
st.markdown("Este dashboard apresenta análises de um conjunto de dados de saúde mental, mostrando padrões e tendências importantes.")

# Carregando os dados
with st.spinner("Carregando dados..."):
    try:
        facts, geography = load_data()
        st.success("Dados carregados com sucesso!")
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        st.info("Certifique-se de que o pipeline de dados foi executado e as transformações DBT foram aplicadas.")
        st.stop()

# Sidebar para filtros
st.sidebar.header("Filtros")

# Filtro de países
countries = ["Todos"] + sorted(facts["Country"].unique().tolist())
selected_country = st.sidebar.selectbox("País", countries)

# Filtro de gênero
genders = ["Todos"] + sorted(facts["Gender"].unique().tolist())
selected_gender = st.sidebar.selectbox("Gênero", genders)

# Aplicando filtros
filtered_data = facts.copy()
if selected_country != "Todos":
    filtered_data = filtered_data[filtered_data["Country"] == selected_country]
if selected_gender != "Todos":
    filtered_data = filtered_data[filtered_data["Gender"] == selected_gender]

# Layout das métricas principais
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total de Respondentes",
        value=len(filtered_data)
    )

with col2:
    treatment_pct = filtered_data["treatment"].mean() * 100
    st.metric(
        label="Em Tratamento",
        value=f"{treatment_pct:.1f}%"
    )

with col3:
    stress_pct = filtered_data["Growing_Stress"].mean() * 100
    st.metric(
        label="Com Estresse Crescente",
        value=f"{stress_pct:.1f}%"
    )

with col4:
    history_pct = filtered_data["Mental_Health_History"].mean() * 100
    st.metric(
        label="Com Histórico",
        value=f"{history_pct:.1f}%"
    )

# Visualizações principais
st.header("Análises Principais")

# Layout para gráficos
col1, col2 = st.columns(2)

with col1:
    # Distribuição por país
    country_data = filtered_data.groupby("Country").size().reset_index(name="count")
    country_data = country_data.sort_values("count", ascending=False)
    
    fig = px.bar(
        country_data, 
        x="Country", 
        y="count",
        title="Distribuição por País",
        color="count",
        color_continuous_scale="Viridis"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Estresse por gênero
    stress_gender = filtered_data.groupby("Gender")["Growing_Stress"].mean().reset_index()
    stress_gender["Growing_Stress"] = stress_gender["Growing_Stress"] * 100
    
    fig = px.bar(
        stress_gender,
        x="Gender",
        y="Growing_Stress",
        title="Estresse Crescente por Gênero (%)",
        color="Growing_Stress",
        color_continuous_scale="RdBu_r",
        text_auto='.1f'
    )
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

# Análise de tratamento e histórico familiar
st.subheader("Relação entre Histórico Familiar e Tratamento")

treatment_history = pd.crosstab(
    filtered_data["family_history"], 
    filtered_data["treatment"], 
    normalize="index"
) * 100

fig = px.bar(
    treatment_history,
    title="Tratamento vs. Histórico Familiar",
    barmode="group",
    text_auto='.1f'
)
fig.update_layout(
    xaxis_title="Histórico Familiar",
    yaxis_title="Percentual (%)",
    legend_title="Em Tratamento"
)
fig.update_traces(texttemplate='%{text}%', textposition='outside')
st.plotly_chart(fig, use_container_width=True)

# Análise de sintomas
st.subheader("Análise de Sintomas")

# Preparando dados para radar chart
symptoms = ["Growing_Stress", "Mental_Health_History", "Mood_Swings", 
            "Coping_Struggles", "Work_Interest", "Social_Weakness"]

# Converter nomes para mais legíveis
symptom_labels = {
    "Growing_Stress": "Estresse Crescente",
    "Mental_Health_History": "Histórico", 
    "Mood_Swings": "Mudanças de Humor", 
    "Coping_Struggles": "Dificuldade de Lidar", 
    "Work_Interest": "Desinteresse no Trabalho", 
    "Social_Weakness": "Fragilidade Social"
}

# Calcular percentuais para cada sintoma
symptom_data = {}
for symptom in symptoms:
    if symptom == "Mood_Swings":
        # Converter para booleano
        symptom_data[symptom] = (filtered_data[symptom].str.lower() == "medium").mean() * 100
    else:
        symptom_data[symptom] = filtered_data[symptom].mean() * 100

# Criar radar chart
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=[symptom_data[s] for s in symptoms],
    theta=[symptom_labels[s] for s in symptoms],
    fill='toself',
    name='Sintomas'
))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100]
        )
    ),
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

# Tabela completa
st.subheader("Dados Detalhados")
if st.checkbox("Mostrar dados completos"):
    st.dataframe(filtered_data)

# Rodapé
st.markdown("---")
st.markdown("Dashboard criado para análise de dados de saúde mental - Projeto de Engenharia de Dados")