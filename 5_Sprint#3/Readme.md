<img src="Imagenes3\0.jpg" width="1010" height="300">



## 📊 *1. Dashboard*

Este es un dashboard interactivo realizado en Power BI, con una ingesta de datos automatizada periódicamente desde Bigquery de Google Cloud. 

Los datos provienen de la plataforma de Yelp y son procesados en la nube con análisis de sentimiento en un DAG en Python a través del Composer y Airflow. Abarca una amplia gama de tipos de accesos a los datos entrando por estados, año, reseñas de clientes y valoraciones por cantidad de estrellas. 

Se pueden observar las gráficas de evolución de 3 KPI, y consultar la geolocalización de restaurantes identificándolos por las valoraciones de clientes en cuanto a la valoración por cantidad de estrellas y reseñas. Podremos observar también porcentajes de aceptación y ranking de restaurants entre otras medidas.

- Versión online del dashboard 👉 [Visualización de datos](https://app.powerbi.com/view?r=eyJrIjoiNDc5MmY1YzgtYWMxOC00NjE1LWFiM2QtYzFjMmU0ZTVlYTdkIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9).

<div style="display: flex; justify-content: center;"> <img src="Imagenes3\Visualizacion_datos.jpg" width="800" height="400"> </div>


## 📈 *3. Resultado y discusión*
 
En la sección de resultados y discusión, presentamos y analizamos los hallazgos de nuestro trabajo. Los resultados obtenidos son discutidos en detalle en la presentación del sprint 3 para proporcionar una comprensión clara y profunda de los datos recopilados. 

A continuación se presentan algunos gráficos analizados en el **Análisis Exploratorio de Datos** que se adjunta el archivo con el nombre de EDA.ipynb .

- Correlación entre variables 
<div style="display: flex; justify-content: center;"> <img src="Imagenes3/3.png" width="500" height="450"> </div>

- Cantidad de restaurantes mexicanos por año.
<div style="display: flex; justify-content: center;"> <img src="Imagenes3/4_1.png" width="750" height="450"> </div>

<div style="display: flex; justify-content: center;"> <img src="Imagenes3/4_2.png" width="350" height="100"> </div>

- Cantidad de restaurantes mexicanos por trimestre.
<div style="display: flex; justify-content: center;"> <img src="Imagenes3/5_1.png" width="750" height="450"> </div>

<div style="display: flex; justify-content: center;"> <img src="Imagenes3/5_2.png" width="450" height="350"> </div>

- Cantidad de restaurantes mexicanos por estado.
<div style="display: flex; justify-content: center;"> <img src="Imagenes3/6_1.png" width="750" height="450"> </div>

<div style="display: flex; justify-content: center;"> <img src="Imagenes3/6_2.png" width="450" height="350"> </div>

- Cantidad de sucursales por empresa.
<div style="display: flex; justify-content: center;"> <img src="Imagenes3/7_1.png" width="750" height="470"> </div>

<div style="display: flex; justify-content: center;"> <img src="Imagenes3/7_2.png" width="450" height="750"> </div>

<div style="display: flex; justify-content: center;"> <img src="Imagenes3/7_3.png" width="450" height="450"> </div>

- Evolución de la cantidad de sucursales por empresa por trimestre.
<div style="display: flex; justify-content: center;"> <img src="Imagenes3/8_1.png" width="850" height="450"> </div>

<div style="display: flex; justify-content: center;"> <img src="Imagenes3/8_2.png" width="450" height="200"> </div>

- Cantidad de restaurantes mexicanos por empresa por estado.
<div style="display: flex; justify-content: center;"> <img src="Imagenes3/9_1.png" width="850" height="450"> </div>

- Calificación de los restaurantes mexicanos.
<div style="display: flex; justify-content: center;"> <img src="Imagenes3/10_1.png" width="750" height="450"> </div>


- Nube de palabras de las reseñas de los clientes.
<div style="display: flex; justify-content: center;"> <img src="Imagenes3/11_1.png" width="750" height="550"> </div>

<div style="display: flex; justify-content: center;"> <img src="Imagenes3/11_2.png" width="450" height="300"> </div>

## 🦾 *2. Modelo de Machine Learning*
Presentamos dos Productos Minimos Viables:

- Exploración de datos 👉 [Sistema de recomendación](https://jbe777-recomendacion-introduccion-nosbuj.streamlit.app/).

Se puede **consultar informacón sobre las valoraciones** por parte de los clientes de los restaurantes mexicanos y ver graficas de las respuestas del sistema. Se busca con este producto que se hagan consultas y obtener gráficos al instantes de los temas que se requieren información para el proceso de toma de decisiones.

<div style="display: flex; justify-content: center;"> <img src="Imagenes3\Sistema_recomendacion1.jpg" width="800" height="400"> </div>



- Modelo de Machine Learning 👉 [Sistema de recomendación](https://mxrestaurant-vkbd9vf6vqedaodnbjckw4.streamlit.app/).

En este **sistema de recomendación al ingresar nuestra ubicación** nos da una lista de los restaurantes mexicanos más cercano y ordenados según valoración de los clientes, al seleccionar el restaurante que se quiere visitar tiene la opción de que le indique la ruta más rápida por medio de Google Maps. Con este producto se busca que se validen in situ la información de cada restaurante.

<div style="display: flex; justify-content: center;"> <img src="Imagenes3\Machine_learning2.jpg" width="800" height="400"> </div>





