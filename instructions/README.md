# Mental Well-being Data Analysis Pipeline

This project implements a full data engineering pipeline to analyze mental health patterns using a modern tech stack.

## Technologies Used

- **Infrastructure as Code (IaC)**: Terraform  
- **Local Environment**: Windows  
- **Workflow Orchestration**: Mage  
- **Data Lake**: Azurite  
- **Data Warehouse**: DuckDB  
- **Data Transformation**: DBT  
- **Data Visualization**: Streamlit  

## Prerequisites

Ensure the following tools are installed:

- Python 3.8 or later  
- Docker  
- Terraform  
- Git  

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/victorfxz//Mental-Well-being-Monitor.git
cd mental_health_pipeline
```

### 2. Create a Python Virtual Environment

```bash
python -m venv venv
.\.venv\Scripts\activate   # For Windows
```

### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize Infrastructure with Terraform

```bash
cd terraform
terraform init
terraform apply -auto-approve
cd ..
```

This step will:
- Launch Azurite (via Docker) to serve as the local Data Lake  
- Create the necessary project directories  
- Download the sample dataset  
- Install and configure Mage, DBT, and Streamlit  

### 5. Configure and Run Mage

```bash
cd mage_project
mage start
```

In Mage's web interface (usually at `http://localhost:6789`):

1. Click on "New pipeline" and choose "Data Pipeline"  
2. Name it `mental_health_pipeline`  
3. Import the project’s predefined Python files:
   - Create a data loader: `load_mental_health_data.py`
   - Add two data exporters: `export_to_azurite.py` and `export_to_duckdb.py`
   - Define the main pipeline: `mental_health_pipeline.py`  
4. Run the complete pipeline  

### 6. Run Transformations with DBT

```bash
cd ../dbt_project
dbt deps
dbt run
dbt test
```

This will:
- Transform raw data within DuckDB  
- Create dimension and fact tables  
- Run data quality tests  

### 7. Visualize Data with Streamlit

```bash
cd ../streamlit
streamlit run app.py
```

The dashboard will be available at `http://localhost:8501`.

## Pipeline Overview

The data pipeline consists of the following stages:

1. **Extraction**: Load raw mental health data  
2. **Load to Data Lake**: Store raw data in Azurite  
3. **Load to Data Warehouse**: Transfer data to DuckDB  
4. **Transformation**: Normalize and enrich data using DBT  
5. **Visualization**: Perform interactive analysis with Streamlit dashboard  

## Dataset Overview

The dataset contains mental health-related information, including:

- Demographics (gender, country, occupation)  
- Family and personal mental health history  
- Stress and well-being indicators  
- Information on treatments and care options  

## Customization

To use a different or larger dataset:

1. Replace the file at `data/mental_health_dataset.csv` with your dataset  
2. Update the DBT transformation scripts accordingly  
3. Modify the Streamlit dashboard to highlight key aspects of your data  

## Troubleshooting

### Azurite Not Running

Check if Docker is running and the Azurite container is active:

```bash
docker ps | grep azurite
```

To restart Azurite:

```bash
docker restart azurite
```

### Mage Errors

Check the logs located in `mage_project/logs/` for troubleshooting.

### DBT Errors

Run the following command to check the DuckDB connection:

```bash
dbt debug
```
