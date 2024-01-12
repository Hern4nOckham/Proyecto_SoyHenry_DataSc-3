<img src="Imagenes2\5.jpg" width="1010" height="300">



## ☁️ *1. Data Pipelines - Stack Tecnológico*

Se toman los datos de la plataforma de Yelp y se los procesa con herramientas de **Google Cloud Platform (GCP)** para crear un el flujo de los datos constantes que seran almacenados en un **Data Warehouse** donde estarán disponibles para ser usados en **Power BI** para su visualización y ser insumos de un sistema de recomendación visualizado en **Streamlit**.

La plataforma **NovyPro** nos permite que el dashbord creado en Power BI este disponible on line.


<p align="center">
<img src="Imagenes2\Data Pipeline.jpg" width="520" height="550">
</p>

## 🗃️ *2. Data Warehouse*

Las herramientas de **Google Cloud Platform (GCP)** que se utilizaron para el procesamiento de los datos son:

- **Cloud Storage**: es un servicio de almacenamiento y recopilación de datos de datos. Se lo puede programar para la toma de datos en ciertos periodos de tiempo.

- **Cloud Dataproc**: es un servicio que brinda el proceso de extracción, transformación y carga (ETL) de datos.

- **Big Query**:  almacena datos y permite el su análisis. También tiene capacidades integradas de machine learning.

- **Cloud Composer**: crea flujos de trabajo que conectan los datos, el procesamiento y los servicios de toda la nube.

<p align="center">
<img src="Imagenes2\Data warehouse.jpg" width="700" height="300">
</p>

                                                Google Cloud Platform
Panel de control
<p align="center">
<img src="Imagenes2\GCP_1.jpg" height="433">
</p>

Funcionamiento de la plataforma
<p align="center">
<img src="Imagenes2\GCP_2.gif" height="400">
</p>

- Ver vídeo completo en el siguiente link 👉 [Visualización de video](https://youtu.be/H4Fy8GOCF0M).

## 🔄 *3. Modelo Entidad-Relación*

- Esquema relacional de Yelp.

<p align="center">
<img src="Imagenes2\Modelo entidad-relacion.png" height=400>
</p>

## 📊 *4. Dashboard (preliminar)*

Este dashboard interativo se desarrollo en Power BI con la intención de tener una mejor visualización de los datos en forma ordenada para poder permitir un análisis de los KPI (key performance indicator) y de los insight, que se pretende obtener tras la investigación. 

<p align="center">
<img src="Imagenes2\Dashboard_1.gif" height=400>
</p>

- Versión online del dashboard en el siguiente link 👉 [Visualización de datos](https://app.powerbi.com/view?r=eyJrIjoiNDc5MmY1YzgtYWMxOC00NjE1LWFiM2QtYzFjMmU0ZTVlYTdkIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9).

                                   Conexión entre Google Cloud Platform y Power BI.

Google Cloud Platform
<p align="center">
<img src="Imagenes2\4.1.jpg" height=400>
</p>

Power BI
<p align="center">
<img src="Imagenes2\4.2.jpg" height=423>
</p>


## 📈 *5. Información preliminar*

Gráficos: Cantidad de Restaurantes Mexicanos por año y Evolución del KPI.
- En este gráfico se muestra la evolución de la cantidad de restaurantes mexicanos desde el año 2019 al 2022 por trimestres, se observa una tendencia a una diminucion de la cantidad de restaurantes mexicanos. 
<p align="center">
<img src="Imagenes2\5.1.jpg" height=500>
</p>


Gráfico: Cantidad de Restaurantes Mexicanos por Estado y Segmentación de valoraciones.
- En este gráfico se muestra la cantidad de restaurantes mexicanos por estado para el primer trimestre del año 2022, se observa que en los Estado de Florida, Arizona y Pensilvania se encuentra una cantidad significativa de restaurantes con respecto a los demas estados.
<p align="center">
<img src="Imagenes2\5.2.jpg" height=500>
</p>

Gráfico: Nube de palabras de las reseñas de los clientes.

Las palabras que mas se repiten en las reseñas de los clientes son:

- Place     >>> Lugar
- Food      >>> Alimento
- Good      >>> Bien
- Order     >>> Orden
- Taco      >>> Taco (Plato mexicano)
- Deliciou  >>> Delicioso
- Service   >>> Servicio
- One       >>> Uno
- Ordered   >>> Ordenado
- Love      >>> Amor

<p align="center">
<img src="Imagenes2\nube_palabras.png" width="200" height=600>
</p>
