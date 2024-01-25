import numpy as np
import pandas as pd
import streamlit as st
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import webbrowser

# Definir colores
background_color = "#d9efef"
title_color = "#436Ab8"

# Configurar el fondo y el color de los títulos
st.markdown(
    f"""
    <style>
        .reportview-container {{
            background-color: {background_color};
            color: {title_color};
        }}
        h1, h2, h3, h4, h5, h6, label, div {{
            color: {title_color};
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Agregar un logo en la esquina superior izquierda
logo = st.image('data/imagen/LOGO2.png', width=100)

# Path del modelo preentrenado
MODEL_PATH = 'models/random_restaurant_model.pkl'

# Se recibe el conjunto de datos y el modelo, devuelve la predicción
def model_prediction(x_in, model, df):
    x = np.asarray(x_in).reshape(1, -1)
    preds = model.predict(x)

    # Obtener la información de restaurantes predichos
    restaurant_info = df.loc[df['Stars'] == preds[0], ['Name', 'Latitude', 'Longitude', 'Sentimiento', 'Stars']]

    return preds, restaurant_info

# Cargar el conjunto de datos
def load_data():
    # Cargar el conjunto de datos (ajusta la ruta del archivo según tu ubicación)
    data_path = 'data/ETL_YELP_con_sentimientos_unicos.csv'
    df = pd.read_csv(data_path)
    return df

# Preprocesamiento del conjunto de datos
def preprocess_data(df):
    features = ['Useful', 'Funny', 'Cool', 'Sentimiento']
    target = 'Stars'

    # Convertir etiquetas de 'Sentimiento' a valores numéricos usando codificación de etiquetas
    label_encoder = LabelEncoder()
    df['Sentimiento'] = label_encoder.fit_transform(df['Sentimiento'])

    X = df[features]
    y = df[target]
    return X, y

# Entrenamiento del modelo
def train_model(X_train, y_train):
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

# Función para encontrar restaurantes cercanos sin repetir
def find_nearest_non_repeated(user_location, restaurant_locations, recommended_indices, df):
    nn = NearestNeighbors(n_neighbors=6, algorithm='ball_tree')
    nn.fit(restaurant_locations)
    distances, indices = nn.kneighbors(user_location)

    # Excluir restaurantes ya recomendados y con el mismo nombre
    indices = [idx for idx in indices.flatten() if idx not in recommended_indices and df.loc[idx, 'Name'] not in df.loc[recommended_indices, 'Name'].values]

    return distances.flatten(), indices

# Función principal
def main():
    # Cargar el conjunto de datos
    df = load_data()

    # Preprocesar el conjunto de datos
    X, y = preprocess_data(df)

    # Dividir el conjunto de datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entrenar el modelo (se guarda el modelo entrenado)
    model = train_model(X_train, y_train)
    with open(MODEL_PATH, 'wb') as file:
        pickle.dump(model, file)

    # Título con estilo azul y centrado
    st.title("Consultora SMART DATA - Análisis de Datos para Gruma")
    st.markdown(
        """
        ¡Bienvenido a la presentación de la consultora SMART DATA! Estamos aquí para ayudar a Gruma a entender el mercado estadounidense 
        y su interés en la comida mexicana. Vamos a explorar si el consumo de comida mexicana en restaurantes está en crecimiento en Estados Unidos 
        utilizando nuestro sistema de recomendación.
        """
    )
    # Lista de índices recomendados
    recommended_indices = []

    # Ubicación del usuario
    user_location = st.text_input("Ingrese su ubicación (Latitud, Longitud):", "36.1592955102, -86.7747332491")

    try:
        user_lat, user_lon = map(float, user_location.split(','))
    except ValueError:
        st.error("Error al interpretar la ubicación. Asegúrese de ingresar valores válidos.")
        st.stop()

    # Botón de predicción
    if st.button("Recomendados por calificaciones y distancia"):
        x_in = [0, 0, 0, 0]  # Puedes ajustar los valores según tus necesidades
        prediction, restaurant_info = model_prediction(x_in, model, df)

        # Calcular distancias y encontrar los vecinos más cercanos (excluyendo los ya recomendados y con el mismo nombre)
        user_location = np.array([user_lat, user_lon]).reshape(1, -1)
        restaurant_locations = df[['Latitude', 'Longitude']]

        distances, indices = find_nearest_non_repeated(user_location, restaurant_locations, recommended_indices, df)

        # Obtener la información de restaurantes cercanos
        nearest_restaurants = df.loc[indices, ['Name', 'City', 'Latitude', 'Longitude', 'Sentimiento', 'Stars']]
        nearest_restaurants['Distance'] = distances

        # Eliminar duplicados y ordenar por distancia
        nearest_restaurants = nearest_restaurants.drop_duplicates(subset='Name').sort_values(by='Distance')

        # Mostrar la información simplificada
        st.success("Restaurantes Recomendados:")
        for i, restaurant in nearest_restaurants.iterrows():
            st.write(f'Nombre: {restaurant["Name"]}')
            st.write(f'Ciudad: {restaurant["City"]}')
            st.write(f'Ubicación (Latitud): {restaurant["Latitude"]}')
            st.write(f'Ubicación (Longitud): {restaurant["Longitude"]}')

            # Mapear el sentimiento a la interpretación deseada
            sentimiento_interpretado = "Malo" if restaurant["Sentimiento"] == 0 else "Neutral" if restaurant["Sentimiento"] == 1 else "Muy Bueno"
            st.write(f'Apreciación promedio de Usuarios: {sentimiento_interpretado}')

            st.write(f'Calificación (Stars): {restaurant["Stars"]}')
            st.write(f'Distancia a su ubicación: {restaurant["Distance"]:.2f} km')

            # Enlace HTML para abrir Google Maps en una nueva pestaña
            google_maps_link = f'<a href="https://www.google.com/maps/place/{restaurant["Latitude"]},{restaurant["Longitude"]}" target="_blank">Ir al Restaurant</a>'
            st.markdown(google_maps_link, unsafe_allow_html=True)

            st.write("---")
            # Actualizar la lista de índices recomendados
            recommended_indices.extend(indices)

if __name__ == '__main__':
    main()