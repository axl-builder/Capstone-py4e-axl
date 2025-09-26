Well, we begin with the project for the capstone.  
The project will be carried out with the websites https://datausa.io/ and https://data.gov/, and it will be related to the construction world.  

The idea is to work with both, since [the first one](https://datausa.io/) provides cleaner information to extract through an API, while [the second one](https://data.gov/) provides less processed information. And although it is apparently possible to extract information from certain statistical documents through an API, "Web Scraping" will also be used to practice these skills.  

What is Data USA?  
It is a project by MIT Media Lab and Deloitte.  
It integrates data from the U.S. Census, Bureau of Labor Statistics, Bureau of Economic Analysis, etc.  
Everything is presented with interactive visualizations and accessible APIs.  
It includes data on:  
- Demographics (age, sex, origin).  
- Education.  
- Income, poverty, employment.  
- Housing, economy, transportation.  
- Health and medical insurance.  

Advantages for your capstone:  
- Easy to use → The API is well documented, and you can also download CSV files.  
- Clean and structured data → You don’t have to deal with strange formats.  
- Integrated visualization → Useful as inspiration for your own charts.  
- Relevance to HomeScan →  
  - You can analyze how income relates to housing conditions.  
  - Study energy costs and energy poverty.  
  - Cross health data with housing conditions.  
  - Compare geographic areas (states/counties) and identify patterns.  

---

### Correct workflow (adapted to the capstone)

**Retrieving (API or Web Scraping)**  
- Get the data:  
  - If there is an API → urllib.request or requests + json.loads.  
  - If it is web scraping → urllib + BeautifulSoup.  
  - If it is a CSV file → urllib + csv.reader.  

**Parsing / Processing**  
- Convert what you receive into Python structures.  
- Clean data: strings → numbers, dates, missing fields.  
- Filter what matters to you (e.g.: keep Year, Population).  

**Database (Storing)**  
- Store the structured data in SQLite.  
- Normalized tables, with keys, simple relationships.  
- Example: raw_population(year, nation, population).  

**Visualization**  
- Export processed data to a JSON/JS.  
- Create HTML with <script> that reads those data and draws a simple chart (line, bar, timeline, etc.).  
- Same as you did in the examples from module 6 of the course.  

---

### FUNDAMENTAL NOTE  
To fully internalize the knowledge, the capstone will identify which concepts of the complete course are being used, to what extent, and which ones are not.  

**PY4E Concepts**  
- Variables, conditionals, loops  
- Functions  
- Strings (search, slicing, regex)  
- Files (read, write)  
- Lists / Tuples / Dictionaries  
- Networking (sockets, urllib)  
- Web scraping (BeautifulSoup)  
- JSON / XML  
- Databases (sqlite3)  
- Basic visualization in HTML/JS  

---

#### Variables / loops / functions
🟢 Data USA: Yes, used to loop through JSON results and structure data.  
🟢 data.gov: Yes, even more, with complex loops to clean CSV/XML.  

#### Strings
🟡 Data USA: Low usage, only for formatting outputs.  
🟢 data.gov: High usage: clean headers, parse odd text in CSV, work with dates.  

#### Regex
🔴 Data USA: Not needed (clean data).  
🟢 data.gov: Very useful to validate emails, addresses, or numbers.  

#### Files
🟢 Data USA: Generate JSON or JS for the final visualization.  
🟢 data.gov: Same, plus saving intermediate CSVs.  

#### Lists / Tuples / Dicts
🟢 Data USA: Direct use (JSON → dict/list → loops).  
🟢 data.gov: Also, with more variety if combining different tables.  

#### Networking (APIs)
🟢 Data USA: Yes, with urllib.request for the JSON API.  
🟡 data.gov: Sometimes yes, sometimes only manual download (less networking).  

#### Web scraping (BeautifulSoup)
🔴 Data USA: Not necessary.  
🟡 data.gov: May be needed if a dataset is only in HTML.  

#### JSON
🟢 Data USA: Central, heavily used.  
🟡 data.gov: Present in some cases, but others are CSV/XLS/XML.  

#### XML
🔴 Data USA: Does not appear.  
🟡 data.gov: Yes, some datasets still use XML.  

#### Databases (SQLite)
🟢 Data USA: Simple, one table with clear fields.  
🟢 data.gov: More complex, several tables and joins.  

#### Visualization in HTML/JS
🟢 Data USA: Quick, export clean JSON and plot.  
🟡 data.gov: Also possible, but requires more data cleaning before plotting.  

👉 With this format, you can read it quickly like a traffic light:  
🟢 = you will definitely practice it  
🟡 = depends on dataset, more effort  
🔴 = almost won’t touch it  

---

It will also include a thorough analysis of the code provided by Charles Severance in the course (gmane.py, gword.py, gbasic, gyear.py, gline.py) and also the functionality of the .htm / .html files.  

---

------------------------------------------------------------------------------------------------------------

### DETAILED DESCRIPTION – CAPSTONE ONE (DataUSA)

This first project was developed using **DataUSA**, a well-documented API with clean data, ideal for consolidating the full workflow of the course: data retrieval, storage, processing, and visualization.  

🔹 **Project Objective**  
Analyze the evolution of total employment in the United States and compare it with employment in the *Real Estate* sector. The goal is to observe how this industry behaves compared to the national average, given its direct connection to construction.  

---

#### 1. Retrieving (Data extraction)
- The script `retrieving.py` connects to the **official DataUSA API**, which returns information in JSON format.  
- Two specific queries were performed:  
  1. **National** → total employment in the economy.  
  2. **Real Estate** → employment in the real estate sector.  
- The function `get_api()` manages:  
  - Connection to the URL.  
  - Reading the response.  
  - Converting the text into Python structures with `json.loads()`.  

This step put into practice:  
- Use of `urllib.request`.  
- Exception handling.  
- Understanding how to navigate a JSON with dictionaries and lists.  

---

#### 2. Storing (Storage in SQLite)
- The retrieved data was saved in `database.sqlite`.  
- The table `Realstate_Jobs` was created with three columns:  
  - **Year**.  
  - **Industry_Jobs** (employment count).  
  - **Source** (“National” or “Real Estate”).  
- Thanks to this design, it was possible to compare both series in the same structure.  

---

#### 3. Processing (Data transformation)
- With the script `graficgen.py`, data was retrieved from the database and transformed into a **dictionary of dictionaries** organized by year.  
- Then, the file `capstone.js` was generated with an array in a format compatible with Google Charts, for example:  

```javascript
gline = [ ['year', 'National', 'Real Estate'],
['2006', 1437174, 1498900],
['2008', 1151898, 1485000],
...
];
```

This step required:  
- `for` loops to iterate and group data.  
- Nested dictionaries to structure the information.  
- Writing files with `.write()`.  

---

#### 4. Visualization (Google Charts)
- Finally, `capstone.js` was loaded in an HTML to graph the data using Google Charts.  
- Different types of interactive charts were generated:  
  - **LineChart** → trends of each series.  
  - **ComboChart** → bars + line, comparing both evolutions.  
  - **AreaChart and ColumnChart** → to experiment with different approaches.  

These charts clearly showed:  
- The overall employment evolution compared to real estate.  
- Differences in curves across the years.  
- The value of representing the same dataset in multiple formats.  

---

#### 5. Key Learnings
- How to work with **clean and well-documented APIs**, which simplify extraction.  
- Importance of storing data in a relational database to organize and compare.  
- How to prepare data with the **visualization goal in mind**: structuring it according to the chart you want to build.  
- Application of nearly all PY4E modules in an integrated workflow:  
  - Networking and JSON.  
  - Dictionaries, lists, and loops.  
  - Basic SQL with SQLite.  
  - File writing.  
  - Visualization with HTML/JS.  

---

------------------------------------------------------------------------------------------------------------

### DETAILED DESCRIPTION – CAPSTONE TWO (NYC Construction Incidents – Data.gov / NYC Open Data)

The second project was designed with a higher level of complexity, working with a **real, extensive, and less processed dataset**: construction incidents recorded in New York City.  
This allowed practicing web scraping, advanced SQL queries, and the creation of multiple comparative visualizations.  

🔹 **Project Objective**  
Analyze the occurrence of construction incidents in NYC, identifying:  
- Distribution by borough (Manhattan, Bronx, Brooklyn, Queens, Staten Island).  
- Monthly temporal evolution of incidents.  
- Main causes (incident types) and their impact in terms of injuries and fatalities.  

---

#### 1. Retrieving (Data extraction)
- The script `spider.py` connected to the **NYC Open Data API** (`bf97-mjsy/rows.json`).  
- A JSON dataset with thousands of records was downloaded.  
- Each record included:  
  - Incident date.  
  - Incident type.  
  - Number of fatalities and injuries.  
  - Location (borough).  
  - Latitude and longitude.  

**Initial transformation**:  
- The script normalized the information into three tables within `Construction-Related_Incidents.sqlite`:  
  - `Incidents_type` → catalog of incident types.  
  - `Ubication` → catalog of boroughs.  
  - `Construction_Incidents` → recorded events, with foreign keys.  

---

#### 2. Storing (Database)
- The SQLite structure allowed establishing relationships between tables through IDs.  
- This step was essential to perform complex queries with `JOIN` and `GROUP BY`, generating aggregations such as:  
  - Number of incidents per month and borough.  
  - Total injuries/fatalities by incident type.  
  - Cross-comparisons between locations and types.  

---

#### 3. Processing (Data transformation)
Different scripts were created to group and prepare the information:  

- **`generator-colchart1.py`**  
  Aggregation of **Fatalities and Injuries by borough** → exports `colchart.js`.  

- **`generator-colchart2.copy.py`**  
  Monthly time series of incidents by borough → exports `colchart2.js`.  
  - Advanced SQL with `strftime('%Y-%m', c.date)` for grouping by month.  
  - Nested Python dictionaries to organize by date and borough.  

- **`generator-donut.py`**  
  Proportion of incidents by type → generates two files:  
  - `donut.js` (Fatalities by type).  
  - `donut2.js` (Injuries by type).  

---

#### 4. Visualization (Google Charts)
Using the generated JS files, interactive charts were created:  

1. **Simple ColumnChart**: comparison of Fatalities vs Injuries by borough.  
   - Brooklyn and Manhattan had the highest incident counts.  

2. **Complex ColumnChart (time series)**: monthly evolution of incidents (2024–2025).  
   - Brooklyn and Bronx showed higher recurrence over time.  

3. **Donut Chart – Injuries**:  
   - Over 50% of injuries came from *Worker Fell (falls)*.  

4. **Donut Chart – Fatalities**:  
   - Over 55% of deaths also from *Worker Fell*.  
   - Other incident types were far less frequent.  

---

#### 5. Key Learnings
- Data extraction from **less structured sources**: how to handle real datasets with noise.  
- Normalization and modeling into multiple SQLite tables.  
- Use of **advanced SQL** (`JOIN`, `GROUP BY`, `SUM`, `strftime` for dates).  
- Handling nested dictionaries and data structures in Python to group results.  
- Creation of multiple visualizations showing:  
  - Comparisons between boroughs.  
  - Evolution over time.  
  - Percentage distribution of incident causes.  