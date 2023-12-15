<img src="Imagenes1\0.jpg" width="1010" height="300">



##  *1. Rol*
Somos la consultora SMART DATA especialista en Business Intelligence y Data Analytics. 
<img src="Imagenes1\1.png" width="600" height="300">

## *2. Propuesta de trabajo*
Nos contrató la empresa Gruma, que es la mayor productora de harina de maíz y tortillas en el mundo. Con marcas líderes en la mayoría de sus mercados, opera principalmente en los Estados Unidos, México, Centroamérica, Europa, Asia y Oceanía. 

<div style="display: flex; justify-content: center;">
<img src="Imagenes1\3.jpeg" width="320" height="90" style="margin-right: 70px;">
<img src="Imagenes1\4.jpg" width="200" height="90">
</div>

Cuenta con alrededor de 23.500 empleados y 73 plantas en Mexico. Tiene ventas netas de aproximadamente U$S 4.600 millones, de las cuales el 74% provinieron de las operaciones fuera de México. 

Alrededor de 37 millones de latinos en Estados Unidos son de origen mexicano, es el grupo más extenso entre la población hispana.


##  *3. Objetivos*

**Objetivo general**

Realizar un análisis de mercado de los restaurantes mexicanos en los estados de California, Arizona, Nuevo México y Texas.

La empresa Gruma saber si en estos estados la comida mexicana está en crecimiento en cuanto a la aceptación por parte de los consumidores locales después del inicio de la pandemia de COVID (desde año 2020 al 2022).

<div style="display: flex; justify-content: center;">
<img src="Imagenes1\5.png" width="620" height="330" style="margin-right: 70px;">
<img src="Imagenes1\6.jpg" width="500" height="250">
</div>



**Objetivos específicos**

Para realizar el análisis de mercado se evaluará desde el año 2020 al 2022.

- Crecimiento del 2 % en la cantidad de restaurantes de comidas mexicanas por trimestre por estado.

- Crecimiento del 3 % en las calificaciones iguales o mayores a tres estrellas por trimestre por estado.

- Reducción del 5 % en las calificaciones menores a tres estrellas por trimestre por estado.

- Crecimiento del 2 % de reseñas positivas por trimestre por año.


##  *4. Producto final*

Nube de palabras:

- Análisis de sentimiento de los restaurantes de comidas mexicanas en 2022.

Sistema de recomendación:

- Top 5 de mayor calificación de los restaurantes mexicanos de los cuatro estados.

- Top 5 con mayor calificación de restaurantes mexicanos por estados.

- Top 5 con menor calificación de restaurantes mexicanos por estado.


##  *5. Diagrama de Grantt*

<img src="Imagenes1\8.jpeg" width="1000" height="400">

##  *6. Datasets*

Henry nos proporciono un Drive donde se encontraban los datasets de Local Guides de Google Maps y de Yelp, al realizar el análisis exploratorio de datos se termino seleccionando solo los de Yelp debido a que mas se adecuan al trabajo que se desarrollara.

**Datasets Yelp**: business.pkl, checkin.json, tip.json, review.json y user.parquet

- Business:
    1.	Contiene información sobre negocios, incluyendo su identificación, nombre, dirección, ciudad, estado, código postal, coordenadas geográficas (latitud y longitud), calificación promedio (estrellas), número de reseñas y si el negocio está abierto o no.
    2.	Es posible que algunas columnas tengan valores nulos, lo que puede requerir una limpieza y manejo adecuado de los datos para un análisis preciso.
    3.	Algunas columnas (como "attributes", "categories" y "hours") podrían contener información en formato de diccionario o lista, lo que puede requerir un procesamiento adicional para extraer datos relevantes.

- checkin:
    1.	Contiene información sobre los check-ins realizados por los usuarios en diferentes negocios.
    2.	Los datos están anidados en la columna "date", donde múltiples fechas están separadas por comas.
    3.	Se deberían desanidar las fechas para tener una fila por cada fecha asociada a su respectivo "business_id".

- tip:
    1. Contiene información sobre las propinas ("tips") que los usuarios han dejado en diferentes negocios.
    2. Las columnas incluyen información sobre el usuario que dejó la propina ("user_id"), el negocio en el que se dejó la propina ("business_id"), el texto de la propina ("text"), la fecha en que se dejó la propina ("date"), y la cantidad de cumplidos ("compliment_count") que recibió la propina.
    3. Es posible que algunas columnas, como "text" y "compliment_count", contengan valores nulos o que requieran un procesamiento adicional para extraer información relevante.

- Review 
    1.	Contiene información sobre las reseñas ("reviews") que los usuarios han dejado en diferentes negocios.
    2.	Las columnas incluyen información sobre el ID de la reseña ("review_id"), el ID del usuario que dejó la reseña ("user_id"), el ID del negocio en el que se dejó la reseña ("business_id"), la calificación ("stars"), y las votaciones útiles ("useful"), divertidas ("funny") y geniales ("cool") que recibió la reseña.
    3.	También contiene el texto de la reseña ("text") donde los usuarios expresan sus opiniones y experiencias sobre el negocio.
    4.	La columna "date" indica la fecha en que se dejó la reseña.

##  *7. Stack tecnológico*

<img src="Imagenes1\7.jpg" width="600" height="300">


##  *8. Extracción, Transformación y Carga*

Despues del análisis del datasets se genero el siguiente notebook ETL_Metadatos.ipynb


