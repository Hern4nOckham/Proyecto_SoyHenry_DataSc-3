# my_functions.py
import pandas as pd
from textblob import TextBlob
from pandas_gbq import to_gbq
from google.cloud import bigquery

# Define las variables de entorno
project_id = "fluted-union-410422"
dataset_id = "PG_Yelp"
table_id = "PBI_yelp"


def analizo_sentimiento(text):
    if not isinstance(text, str):
        text = str(text)

    if not text:
        return 1
         
    analysis = TextBlob(text)
    sentiment_score = analysis.sentiment.polarity

    if sentiment_score < 0:
        return 0
    elif sentiment_score > 0:
        return 2
    else:
        return 1

def execute_yelp_script():
    try:
        
        yelp = pd.read_csv('gs://bucket_restaurant_mexicanos/ETL_YELP.csv')
        
        estados = pd.read_csv('gs://bucket_restaurant_mexicanos/PBI_estados.csv')
        print(yelp.columns)
        print(estados.columns)
        # Aplicar el análisis de sentimiento y crear la nueva columna
        yelp['sentimiento'] = yelp['Text'].apply(analizo_sentimiento)

        # Convertir la columna a tipo entero
        yelp['Stars'] = yelp['Stars'].astype(int)

        yelp['sentimiento'].value_counts()
        yelp['User_id'].value_counts()
       
        # Realiza el merge basado en la columna 'Estado'
        merged_df = pd.merge(estados, yelp, on='State', how='inner')
        print("llegue aqui")
        yelp['Date'] = pd.to_datetime(yelp['Date'], format='%Y-%m-%d')
        # Ordenar el DataFrame por la columna "Date"
        merged_df = merged_df.sort_values(by='Date')

        # Crear la nueva columna 'Valoracion del Usuario' basada en la columna 'sentimiento'
        merged_df['Valoracion_del_Usuario'] = merged_df['sentimiento'].map({0: 'Malo', 1: 'Regular', 2: 'Muy bueno'})

        del merged_df['Text']
        merged_df= merged_df.reset_index(drop=True)
       
        destination_table = f'{project_id}.{dataset_id}.{table_id}'
        to_gbq(merged_df, destination_table, project_id=project_id, if_exists='replace')
        print(merged_df)
        
        return merged_df

    except Exception as e:
        # Manejo de la excepción: imprime el error y devuelve un valor predeterminado o lanza una nueva excepción si es necesario.
        print(f"Error en execute_yelp_script: {str(e)}")
        return None


if __name__ == "__main__":
    result = execute_yelp_script()
    if result is not None:
        print("Script ejecutado exitosamente. Resultado:")
        print(result)
    else:
        print("Hubo un error al ejecutar el script.")
