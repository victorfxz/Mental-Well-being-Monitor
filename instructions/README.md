# Pipeline de Dados para Análise de Saúde Mental

Este projeto implementa um pipeline completo de engenharia de dados para análise de padrões em saúde mental, utilizando diversas tecnologias modernas.

## Tecnologias Utilizadas

- **IaC**: Terraform
- **Ambiente**: Windows local
- **Orquestração de fluxo de trabalho**: Mage
- **Data Lake**: Azurite
- **Data Warehouse**: DuckDB
- **Transformação de dados**: DBT
- **Visualização**: Streamlit

## Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- Python 3.8+
- Docker
- Terraform
- Git

## Instalação e Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/mental_health_pipeline.git
cd mental_health_pipeline
```

### 2. Criar ambiente virtual Python

```bash
python -m venv venv
.\.venv\Scripts\activate   # Windows
```

### 3. Instalar dependências básicas

```bash
pip install -r requirements.txt
```

### 4. Inicializar a infraestrutura com Terraform

```bash
cd terraform
terraform init
terraform apply -auto-approve
cd ..
```

Este comando irá:
- Iniciar o Azurite (via Docker) para servir como Data Lake
- Criar as pastas necessárias para o projeto
- Baixar o conjunto de dados de exemplo
- Instalar e configurar Mage, DBT e Streamlit

### 5. Configurar e executar o Mage

```bash
cd mage_project
mage start
```

No ambiente web do Mage (navegador), que normalmente abre em `http://localhost:6789`:

1. Clique em "New pipeline" e selecione "Data Pipeline"
2. Nomeie como "mental_health_pipeline"
3. Importe os arquivos Python definidos neste projeto:
   - Crie um data loader: `load_mental_health_data.py`
   - Crie dois data exporters: `export_to_azurite.py` e `export_to_duckdb.py`
   - Configure a pipeline principal: `mental_health_pipeline.py`
4. Execute a pipeline completa

### 6. Executar transformações com DBT

```bash
cd ../dbt_project
dbt deps
dbt run
dbt test
```

Isso irá:
- Transformar os dados brutos no DuckDB
- Criar as tabelas dimensionais e de fatos
- Executar testes para garantir a qualidade dos dados

### 7. Visualizar os dados com Streamlit

```bash
cd ../streamlit
streamlit run app.py
```

O dashboard Streamlit estará disponível em `http://localhost:8501`

## Estrutura da Pipeline

O pipeline de dados segue os seguintes passos:

1. **Extração**: Carregamento dos dados brutos de saúde mental
2. **Carregamento no Data Lake**: Armazenamento dos dados brutos no Azurite
3. **Carregamento no Data Warehouse**: Transferência dos dados para o DuckDB
4. **Transformação**: Normalização e enriquecimento dos dados com DBT
5. **Visualização**: Análise interativa dos dados através do dashboard Streamlit

## Detalhes do Conjunto de Dados

O conjunto de dados contém informações sobre saúde mental, incluindo:
- Dados demográficos (gênero, país, ocupação)
- Histórico familiar e de saúde mental
- Indicadores de estresse e bem-estar
- Informações sobre tratamentos e opções de cuidado

## Customização

Para utilizar um conjunto de dados maior ou diferente:

1. Substitua o arquivo `data/mental_health_dataset.csv` pelo seu próprio conjunto de dados
2. Ajuste os scripts de transformação no DBT conforme necessário
3. Modifique a visualização no Streamlit para destacar os aspectos mais relevantes do seu conjunto de dados

## Resolução de Problemas

### Azurite não está funcionando

Verifique se o Docker está em execução e se o container do Azurite foi criado:

```bash
docker ps | grep azurite
```

Para reiniciar o Azurite:

```bash
docker restart azurite
```

### Erros no Mage

Verifique os logs do Mage em `mage_project/logs/` para identificar possíveis problemas.

### Erros no DBT

Execute `dbt debug` para verificar a conexão com o DuckDB.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues.