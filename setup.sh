#!/bin/bash

# Mensagem de boas-vindas
echo "==================================================="
echo "  Configuração do Pipeline de Dados de Saúde Mental"
echo "==================================================="
echo

# Criar ambiente virtual
echo "Criando ambiente virtual Python..."
python -m venv venv
source venv/Scripts/activate  # Windows
# source venv/bin/activate     # Linux/Mac

# Instalar dependências
echo "Instalando dependências..."
pip install -r requirements.txt

# Configurar diretórios do projeto
echo "Configurando estrutura de diretórios..."
mkdir -p data/duckdb
mkdir -p mage_project/data_loaders
mkdir -p mage_project/data_exporters
mkdir -p mage_project/pipelines
mkdir -p dbt_project/models/staging
mkdir -p dbt_project/models/marts
mkdir -p streamlit

# Inicializar infraestrutura com Terraform
echo "Inicializando infraestrutura com Terraform..."
cd terraform
terraform init
terraform apply -auto-approve
cd ..

echo
echo "==================================================="
echo "Configuração inicial concluída!"
echo
echo "Próximos passos:"
echo "1. Configure o Mage: cd mage_project && mage start"
echo "2. Execute as transformações DBT: cd dbt_project && dbt run"
echo "3. Inicie o dashboard: cd streamlit && streamlit run app.py"
echo "==================================================="