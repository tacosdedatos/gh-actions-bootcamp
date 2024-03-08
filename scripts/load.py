import pandas as pd
from snowflake.connector.pandas_tools import write_pandas
import snowflake.connector
import os 

# Conexión a Snowflake
conn = snowflake.connector.connect(
    user=os.environ['SNOWSQL_USER'],
    password=os.environ['SNOWSQL_PWD'],
    account=os.environ['SNOWSQL_ACCOUNT'],
    warehouse='COMPUTE_WH',
    database='SOURCE',
    schema='RAW'
)

# Lista de archivos:tablas
ARCHIVOS = [
    {
        "archivo": "cf_usuarios.csv",
        "tabla": "CF_USUARIOS",
    },
    {
        "archivo": "cf_resenas.csv",
        "tabla": "CF_RESENAS",
    },
    {
        "archivo": "cf_cursos.csv",
        "tabla": "CF_CURSOS",
    },
    {
        "archivo": "cf_inscripciones.csv",
        "tabla": "CF_INSCRIPCIONES",
    },
    
]

# Crear cursor
cur = conn.cursor()

for archivo in ARCHIVOS:
    df = pd.read_csv(archivo['archivo'])
    df.columns = df.columns.str.upper()

    # Cargar el DataFrame en la tabla de Snowflake
    write_pandas(conn, df, archivo['tabla']) # debe ser mayusculas aqui

    print("DataFrame cargado en Snowflake.")

# Cerrar la conexión
cur.close()
conn.close()
