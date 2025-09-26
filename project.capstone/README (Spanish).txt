Bueno, iniciamos con el proyecto para el capstone.
El proyecto se realizara con las paginas https://datausa.io/ y https://data.gov/, y estara relacionado al mundo de la construccion.

La idea es realizarlo con ambas, ya que [la primera](https://datausa.io/) cuenta con la informacion mas limpia para extraer con API, por otro lado [la segunda](https://data.gov/) cuenta con informacion menos procesada, y si bien aparentemente es posible extraer la informacion de ciertos documentos estadisticos por API, se utilizara "Web Scrapping" para poder entrenar estas habilidades tambien.

¿Qué es Data USA?:
Es un proyecto del MIT Media Lab y Deloitte.
Integra datos del censo de EE. UU., Bureau of Labor Statistics, Bureau of Economic Analysis, etc.
Todo está presentado con visualizaciones interactivas y APIs accesibles.
Tiene datos sobre:
    Demografía (edad, sexo, origen).
    Educación.
    Ingresos, pobreza, empleo.
    Vivienda, economía, transporte.
    Salud y seguros médicos.

Ventajas para tu capstone:
Fácil de usar → La API está bien documentada, y también podés descargar CSV.
Datos limpios y estructurados → No tenés que lidiar con formatos raros.
Visualización integrada → Te sirve de inspiración para tus propios gráficos.
Relevancia con HomeScan →
    Podés analizar cómo se relacionan ingresos y condiciones de vivienda.
    Estudiar costos de energía y pobreza energética.
    Cruzar datos de salud con condiciones habitacionales.
    Comparar zonas geográficas (estados/condados) y ver patrones.


Flujo correcto (adaptado al capstone)

Retrieving (API o Web Scraping)
    Obtener los datos:
        Si hay API → urllib.request o requests + json.loads.
        Si es web scraping → urllib + BeautifulSoup.
        Si es archivo CSV → urllib + csv.reader.

Parsing / Processing
    Convertir lo que recibís a estructuras de Python.
    Limpiar datos: strings → números, fechas, campos faltantes.
    Filtrar lo que te importa (ej: quedarte con Year, Population).

Database (Storing)
    Guardar los datos estructurados en SQLite.
    Tablas normalizadas, con claves, relaciones simples.
    Ejemplo: raw_population(year, nation, population).

Visualization
    Exportar datos procesados a un JSON/JS.
    Crear HTML con < script > que lea esos datos y pinte un gráfico simple (línea, barras, timeline, etc.).
    Igual que lo hacés en los ejemplos de módulos 6 del curso.

DATO FUNDAMENTAL: Para interiorizar a fondo todos los conocimientos, se identificara que conceptos del curso completo se estarian utilizando en el capstone, en que profundidad, y cuales no.

Conceptos de PY4E
    Variables, condicionales, loops
    Funciones
    Strings (búsqueda, slicing, regex)
    Files (leer, escribir)
    Lists / Tuples / Dictionaries
    Networking (sockets, urllib)
    Web scraping (BeautifulSoup)
    JSON / XML
    Databases (sqlite3)
    Visualización básica en HTML/JS


Variables / loops / funciones

🟢 Data USA: Sí, se usan para recorrer resultados del JSON y estructurar datos.
🟢 data.gov: Sí, incluso más, con bucles complejos para limpiar CSV/XML.

Strings

🟡 Data USA: Poco uso, solo para formatear outputs.
🟢 data.gov: Mucho uso: limpiar headers, parsear texto raro en CSV, trabajar con fechas.

Regex

🔴 Data USA: No lo necesitarías (datos limpios).
🟢 data.gov: Muy útil para validar emails, direcciones o números.

Files

🟢 Data USA: Generar JSON o JS para la visualización final.
🟢 data.gov: Igual, pero además podés guardar CSV intermedios.

Lists / Tuples / Dicts

🟢 Data USA: Uso directo (JSON → dict/list → loops).
🟢 data.gov: También, y estructuras más variadas si combinás tablas distintas.

Networking (APIs)

🟢 Data USA: Sí, con urllib.request para la API JSON.
🟡 data.gov: A veces sí, a veces solo descarga manual (menos networking).

Web scraping (BeautifulSoup)

🔴 Data USA: No hace falta.
🟡 data.gov: Puede ser necesario si un dataset solo está en HTML.

JSON

🟢 Data USA: Central, se usa mucho.
🟡 data.gov: Presente en algunos, pero otros son CSV/XLS/XML.

XML

🔴 Data USA: No aparece.
🟡 data.gov: Sí, hay datasets que todavía usan XML.

Databases (SQLite)

🟢 Data USA: Sencillo, una tabla con campos claros.
🟢 data.gov: Más completo, varias tablas y joins.

Visualización en HTML/JS

🟢 Data USA: Rápido, exportás un JSON limpio y graficás.
🟡 data.gov: También, pero requiere más limpieza previa antes de graficar.

👉 Con este formato, lo podés leer rápido como un semáforo:

🟢 = vas a practicarlo sí o sí
🟡 = depende del dataset, más esfuerzo
🔴 = casi no lo vas a tocar


TAMBIEN SE ANALIZARA A FONO LAS LINEAS DE CODIGO DE LO PRESENTADO POR CHARLES SEVERANCE EN EL CURSO. ESPECIFICAMENTE (gmane.py, gword.py, gbasic, gyear.py, gline.py) y tambien se analizara el funcionamiento del .htm / .html

------------------------------------------------------------------------------------------------------------

DESCRIPCIÓN DETALLADA – CAPSTONE ONE (DataUSA)

Este primer proyecto se desarrolló sobre la base de **DataUSA**, una API bien documentada y con datos limpios, ideal para consolidar el flujo completo del curso: extracción, almacenamiento, procesamiento y visualización de información.

🔹 **Objetivo del proyecto**  
Analizar la evolución del empleo total en los Estados Unidos y compararlo con el empleo en el sector inmobiliario (*Real State*). La idea es observar cómo se comporta esta industria frente al promedio nacional, dado su vínculo directo con la construcción.

---

### 1. Retrieving (Extracción de datos)
- El script `retrieving.py` conecta a la **API oficial de DataUSA**, que devuelve la información en formato JSON.
- Se realizaron dos consultas específicas:
  1. **National** → todos los empleos de la economía en general.  
  2. **Real State** → empleos dentro del sector inmobiliario.  
- La función `get_api()` gestiona:
  - Conexión con la URL.  
  - Lectura de la respuesta.  
  - Conversión del texto a estructuras Python con `json.loads()`.  

Con esto se puso en práctica:
- Uso de `urllib.request`.  
- Manejo de excepciones.  
- Comprensión de cómo navegar un JSON con diccionarios y listas.  

---

### 2. Storing (Almacenamiento en SQLite)
- Los datos obtenidos se guardaron en `database.sqlite`.  
- Se creó la tabla `Realstate_Jobs` con tres columnas:
  - **Year** (año).  
  - **Industry_Jobs** (cantidad de empleos).  
  - **Source** (origen: “National” o “Real State”).  
- Gracias a este diseño, fue posible comparar ambas series en una misma estructura.  

---

### 3. Processing (Transformación de datos)
- Con el script `graficgen.py`, los datos fueron recuperados de la base y transformados en un **diccionario de diccionarios** organizado por año.  
- Luego, se generó el archivo `capstone.js` con un array en formato compatible con Google Charts, por ejemplo:  

```javascript
gline = [ ['año', 'National', 'Real State'],
['2006', 1437174, 1498900],
['2008', 1151898, 1485000],
...
];
Este paso implicó trabajar con:

Ciclos for para recorrer y agrupar datos.

Diccionarios anidados para estructurar la información.

Escritura en archivos con .write().

### 4. Visualization (Visualización con Google Charts)
- Finalmente, se cargó capstone.js en un HTML para graficar los datos con Google Charts.
- Se generaron diferentes tipos de gráficos interactivos:
- LineChart → tendencias de cada serie.
- ComboChart → barras + línea, comparando ambas evoluciones.
- AreaChart y ColumnChart → para experimentar con distintos enfoques de visualización.
- Estos gráficos mostraron de forma clara:
- La evolución general del empleo en comparación con el inmobiliario.
- Diferencias en las curvas según los años.
- El valor de representar un mismo dataset con múltiples formatos.

### 5. Aprendizajes Clave
- Cómo trabajar con APIs limpias y bien documentadas, que simplifican la extracción.
- Importancia de almacenar los datos en una base de datos relacional para organizar y comparar.
- Cómo preparar los datos pensando en la visualización final: es decir, estructurarlos de acuerdo al gráfico que se quiere lograr.
- Aplicación de casi todos los módulos de PY4E en un flujo integrado:
- Networking y JSON.
- Diccionarios, listas y loops.
- SQL básico con SQLite.
- Escritura de archivos.
- Visualización con HTML/JS.


------------------------------------------------------------------------------------------------------------

DESCRIPCIÓN DETALLADA – CAPSTONE TWO (NYC Construction Incidents – Data.gov / NYC Open Data)

El segundo proyecto se propuso un nivel de complejidad mayor, trabajando con un dataset **real, extenso y menos procesado**: los incidentes en obras de construcción registrados en la ciudad de Nueva York.  
Esto permitió entrenar habilidades de web scraping, consultas SQL avanzadas y generación de múltiples visualizaciones comparativas.

🔹 **Objetivo del proyecto**  
Analizar la ocurrencia de incidentes de construcción en NYC, identificando:
- Distribución por borough (Manhattan, Bronx, Brooklyn, Queens, Staten Island).  
- Evolución temporal mensual de los incidentes.  
- Principales causas (tipos de incidentes) y su impacto en términos de lesiones e incluso fatalidades.  

---

### 1. Retrieving (Obtención de datos)
- El script `spider.py` se conectó a la API de **NYC Open Data** (`bf97-mjsy/rows.json`).
- Se descargó un dataset en formato JSON con miles de registros.
- Cada registro incluía:
  - Fecha del incidente.
  - Tipo de incidente.
  - Número de fatalidades y lesiones.
  - Ubicación (borough).
  - Latitud y longitud.  

**Transformación inicial**:  
- El script normalizó la información en tres tablas dentro de la base `Construction-Related_Incidents.sqlite`:
  - `Incidents_type` → catálogo de tipos de incidentes.  
  - `Ubication` → catálogo de ubicaciones (boroughs).  
  - `Construction_Incidents` → hechos registrados, con claves foráneas.  

---

### 2. Storing (Base de datos)
- La estructura en SQLite permitió establecer relaciones entre tablas mediante IDs.  
- Este paso fue clave para poder realizar consultas complejas con `JOIN` y `GROUP BY`, generando agregaciones como:
  - Número de incidentes por mes y borough.  
  - Total de lesiones/fatalidades por tipo de incidente.  
  - Comparaciones cruzadas entre ubicaciones y tipos.  

---

### 3. Processing (Transformación de datos)
Se crearon distintos scripts para agrupar y preparar la información:

- **`generator-colchart1.py`**  
  Agrupación de **Fatalities e Injuries por borough** → exporta `colchart.js`.  

- **`generator-colchart2.copy.py`**  
  Serie temporal mensual de incidentes por borough → exporta `colchart2.js`.  
  - Uso avanzado de SQL para agrupar con `strftime('%Y-%m', c.date)`.  
  - Diccionarios anidados en Python para organizar por fechas y barrios.  

- **`generator-donut.py`**  
  Proporciones de incidentes por tipo → genera dos archivos:  
  - `donut.js` (Fatalities por tipo).  
  - `donut2.js` (Injuries por tipo).  

---

### 4. Visualization (Visualización con Google Charts)
A partir de los archivos JS generados, se realizaron gráficos interactivos:

1. **ColumnChart simple**: comparación de Fatalities vs Injuries por borough.  
   - Brooklyn y Manhattan con la mayor cantidad de incidentes.  

2. **ColumnChart complejo (time series)**: evolución mensual de incidentes (2024–2025).  
   - Brooklyn y Bronx con más recurrencia a lo largo del tiempo.  

3. **Donut Chart – Injuries**:  
   - Más del 50% de las lesiones provienen de *Worker Fell (caídas de trabajadores)*.  

4. **Donut Chart – Fatalities**:  
   - Más del 55% de las muertes también por *Worker Fell*.  
   - Los demás tipos de incidentes quedan muy por detrás en proporción.  

---

### 5. Aprendizajes Clave
- Extracción de datos **menos estructurados**: cómo enfrentarse a datasets reales con ruido.  
- Normalización y modelado de datos en múltiples tablas SQLite.  
- Uso de **SQL avanzado** (`JOIN`, `GROUP BY`, `SUM`, `strftime` para fechas).  
- Manejo de diccionarios y estructuras anidadas en Python para agrupar resultados.  
- Creación de distintas visualizaciones que muestran:
  - Comparaciones entre barrios.  
  - Evolución en el tiempo.  
  - Distribución porcentual de causas de incidentes.  

---

✅ **En conclusión**:  
El **Capstone Two** lleva el aprendizaje un paso más allá: desde datos limpios a datos reales y complejos.  
Este proyecto demuestra cómo **Python, SQLite y Google Charts** se pueden combinar para crear un análisis completo y visualmente atractivo de un problema real, en este caso la seguridad en la construcción.
