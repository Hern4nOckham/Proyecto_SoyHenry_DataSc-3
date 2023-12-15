import pandas as pd
import gzip # biblioteca qyue contiene funciones para comprimir y descomprimir archivos
import os  # biblioteca que proporciona una interfaz para interactuar con el sistema operativo
import shutil # biblioteca para hace operaciones de alto nivel con archivos y directorios


def gz_extract(dpath): # se crea una funcion para que luego que dentro de la función, directory tomará el valor ingresado en "dpath" 
    extension = ".gz" 
    os.chdir(dpath) # chrdir cambia de directorio a la ruta especifica dpath

    for item in os.listdir(dpath): #  Iterar sobre los elementos en el directorio
        if item.endswith(extension): # Busca los archivos que tengan (.Gz) como extensiom 
            gz_name = os.path.abspath(item)  # se obtiene la ruta completa y absoluta usando el sudmodulo "os.path" y la funcion "abspath" 
            file_name = os.path.splitext(os.path.basename(gz_name))[0] # Toma el nombre del archivo que tiene el .gz y lo divide en dos partes, el nombre y la extension convertdos en duplas

            with gzip.open(gz_name, "rb") as f_in, open(file_name, "wb") as f_out: #Gzip abre el archivo comprimido en lectura binar "rb" y "wb" abre en modo escritura binaria, f_in 
                shutil.copyfileobj(f_in, f_out) #Copyfilejob copia los archivos "f_in" hacia el destiono "f_out"
            os.remove(gz_name)# Elima el archivo con la extension ".gz" del sistema 
            print(f"Descomprimido y eliminado: {file_name}")
            

def tipo_dato(df):
    
    """
    Funcion para saber el tipo de dato de cada columna, tambien para saber el % de nulos y si existen
    filas que esten complemente nulas, 'df' es el dataframe a examinar
    """
 # Crear un diccionario para almacenar información sobre las columnas
    dic = {"Nombre_Columna": [], "Tipo_dato": [], "%_No_nulos": [], "%_Nulos": []}
# Iterar a través de las columnas del DataFrame
    for columna in df.columns:
        # Calcular el porcentaje de valores no nulos en la columna actual
        porcen_no_nulos = (df[columna].count() / len(df) *100 )

        # Agregar información al diccionario
        dic["Nombre_Columna"].append(columna) # se agrega el nombre de la columna al diccionario 'dic' 
        dic["Tipo_dato"].append(df[columna].apply(type).unique()) #se obtiene el tipo de dato  y se agrega al 'dic' en la columna'Tipo_dato'
        dic["%_No_nulos"].append(round(porcen_no_nulos, 2)) # Se calcula el % de valores no nulos y se agrega al 'dic' en la columna '%_No_nulos'
        dic["%_Nulos"].append(round(100-porcen_no_nulos,2)) # se calcula el % de nulos y se agrega al 'dic' en la columna 'nulos'

# Para la operacion de %_nulos, el 100 significa el 100% de datos de esa columna - % de no_nulos de la misma columna,
# se realizo de sta forma para simplificar la operacion 

    # Crear un DataFrame con la información recopilada
    df_info = pd.DataFrame(dic)

    # Imprimir la cantidad de valores nulos en cada columna
    for columna in df.columns:
        print(columna, "(nulos) = " , df[columna].isnull().sum()) #se suman los valores nulos  

    print("\n filas completamente nulas: ", df.isna().all(axis=1).sum()) # se suman las filas que esten completamente vacias

    # Devuelve el DataFrame con información sobre las columnas
    return df_info 


def duplicados(df,columna):

    """ 
    Esta funcion toma dos valores el primero df que va hacer el DataFrame y el segundo el nombre de la columna especifica,
    esto con el fin de  identificar las filas duplicadas que existen en la columna dada, estas filas las filtra y ordena 
    para compararlas
    """
    #Filtrar filas duplicadas
    duplicated_rows = df[df.duplicated(subset=columna,keep=False)] # se identifican los duplicados en la columna dada bajo el parametro 'subset' y con 'keep=False' se mostraran todas las filas duplicadas
    if duplicated_rows.empty: # Si 'duplicated_rows' esta vacio significa que no existen duplicados 
        return "No Existen Duplicados" # Se indica que no existen  filas duplicadas
    
    # Ordenar filas duplicadas para poder compararlas
    duplicated_rows_sorted = duplicated_rows.sort_values(by=columna)
    return duplicated_rows_sorted
    
