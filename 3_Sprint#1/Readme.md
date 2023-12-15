<img src="Imagenes1\0.jpg" width="1010" height="300">



##  *1. Rol del grupo*
Somos la consultora SMART DATA especialista en Business Intelligence y Data Analytics. Nos dedicamos al análisis de datos del mercado estadounidense. 


<img src="Imagenes1\1.png" width="600" height="300">

## *2. Contexto*

Nos contrató la empresa Gruma, quiere lanzar al mercado nuevos productos y necesita saber si **el consumo de comida mexicana en restaurantes está en crecimiento** en Estados Unidos después del inicio de la pandemia de COVID (desde año 2020 al 2022).

<div style="display: flex; justify-content: center;">
<img src="Imagenes1\6.jpg" width="320" height="200" style="margin-right: 70px;">
<img src="Imagenes1\2.png" width="300" height="150"> 

La población en EE.UU. de origen mexicana es aproximadamente 36 millones.
</div>

La empresa **Gruma**, es la mayor productora de harina de maíz y tortillas en el mundo.
- Tiene alrededor de 23.500 empleados y 73 plantas industriales en México.
- Con marcas líderes en la mayoría de sus mercados, opera principalmente en los Estados Unidos, México, Centroamérica, Europa, Asia y Oceanía.
- Durante el 2022 tuvo ventas netas de aproximadamente U$S 4.600 millones, siendo el 74% de estas ventas provinieron de las operaciones fuera de México.

<div style="display: flex; justify-content: center;">
<img src="Imagenes1\3.jpeg" width="370" height="150" style="margin-right: 70px;">

<img src="Imagenes1\4.jpg" width="300" height="150"> 
</div>

##  *3. Propuesta de trabajo*

**Objetivo general**

Realizar un análisis de mercado de los restaurantes mexicanos en los estados de:

- Arizona (AZ)
- Louisiana (LA)
- Florida (FL)
- Missouri (MO)
- Tennessee (TN)
- Indiana (IN)
- Pennsylvania (PA).

<div style="display: flex; justify-content: center;">
<img src="Imagenes1\5.png" width="620" height="330" style="margin-right: 70px;">
</div>



**Objetivos específicos**

- Para realizar el análisis de mercado se evaluará desde el año 2020 al 2022.
- Crecimiento del 2 % en la cantidad de restaurantes de comidas mexicanas por trimestre por estado.
- Crecimiento del 3 % en las calificaciones iguales o mayores a tres estrellas por trimestre por estado.
- Reducción del 5 % en las calificaciones menores a tres estrellas por trimestre por estado.


##  *4. Producto final*

Nube de palabras:

- Análisis de sentimiento de los restaurantes de comidas mexicanas en 2022.

Sistema de recomendación:

- Top 5 de mayor calificación de los restaurantes mexicanos de los cuatro estados.

- Top 5 con mayor calificación de restaurantes mexicanos por estados.

- Top 5 con menor calificación de restaurantes mexicanos por estado.


##  *5. Diagrama de Grantt*

<img src="Imagenes1\8.jpeg" width="1000" height="400">

##  *6. Dataset*

Henry nos proporciono un Drive donde se encontraban los datasets de Local Guides de Google Maps y de Yelp, al realizar el análisis exploratorio de datos se seleccionando solo los archivos de Yelp debido a que mejor se adecuan al trabajo que se desarrollara. 

**Datasets Yelp**: business.pkl, checkin.json, tip.json, review.json y user.parquet

- business.pkl
    1.	Contiene información sobre negocios, incluyendo su identificación, nombre, dirección, ciudad, estado, código postal, coordenadas geográficas (latitud y longitud), calificación promedio (estrellas), número de reseñas y si el negocio está abierto o no.
    2.	Es posible que algunas columnas tengan valores nulos, lo que puede requerir una limpieza y manejo adecuado de los datos para un análisis preciso.
    3.	Algunas columnas (como "attributes", "categories" y "hours") podrían contener información en formato de diccionario o lista, lo que puede requerir un procesamiento adicional para extraer datos relevantes.

- checkin.json
    1.	Contiene información sobre los check-ins realizados por los usuarios en diferentes negocios.
    2.	Los datos están anidados en la columna "date", donde múltiples fechas están separadas por comas.
    3.	Se deberían desanidar las fechas para tener una fila por cada fecha asociada a su respectivo "business_id".

- tip.json
    1. Contiene información sobre las propinas ("tips") que los usuarios han dejado en diferentes negocios.
    2. Las columnas incluyen información sobre el usuario que dejó la propina ("user_id"), el negocio en el que se dejó la propina ("business_id"), el texto de la propina ("text"), la fecha en que se dejó la propina ("date"), y la cantidad de cumplidos ("compliment_count") que recibió la propina.
    3. Es posible que algunas columnas, como "text" y "compliment_count", contengan valores nulos o que requieran un procesamiento adicional para extraer información relevante.

- review.json 
    1.	Contiene información sobre las reseñas ("reviews") que los usuarios han dejado en diferentes negocios.
    2.	Las columnas incluyen información sobre el ID de la reseña ("review_id"), el ID del usuario que dejó la reseña ("user_id"), el ID del negocio en el que se dejó la reseña ("business_id"), la calificación ("stars"), y las votaciones útiles ("useful"), divertidas ("funny") y geniales ("cool") que recibió la reseña.
    3.	También contiene el texto de la reseña ("text") donde los usuarios expresan sus opiniones y experiencias sobre el negocio.
    4.	La columna "date" indica la fecha en que se dejó la reseña.

- user.parquet
    1. xxx

##  *7. Stack tecnológico*

<img src="Imagenes1\7.jpg" width="600" height="300">


##  *8. Extracción, Transformación y Carga*

Se realizó un análisis exploratorio de los datos preliminar y una extracción, limpieza y carga del **dataset de Yelps** en estos notebbok:
 - xxx.ipynb
 - xxxx.ipynb

Y se generó este nuevo dataset Yelp_ETL con los siguientes archivos:
- xxx.csv
- xxxx.csv


