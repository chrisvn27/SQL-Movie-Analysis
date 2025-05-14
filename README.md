# SQL Movie Analysis Project 🎬

This project is an exploratory SQL analysis of The Movie Database (TMDB) 5000 dataset using SQLite and Python. It involves querying data about movies, their budgets, revenues, genres, and cast information.

## 📊 Dataset
- **tmdb_5000_movies.csv**: Contains movie metadata (budget, revenue, genres, vote average, etc.).
- **tmdb_5000_credits.csv**: Contains cast and crew information.

## 🛠️ Tools Used
- SQLite (via SQLite Viewer in VS Code)
- Python (for loading CSV to SQLite)
- SQL queries for data exploration and analysis

## 📂 Project Folder Structure
SQL-Movie-Analysis/
├── data/ # Raw CSV files
├── db/ # SQLite database (movies.db)
├── notebooks/ # Python script to load data
├── queries/ # SQL scripts
├── results/ # Query outputs (optional)
├── README.md # This file
├── .gitignore


## ✅ Key Analyses & Queries

### 1. Top Movies by Revenue-to-Budget Ratio
Identified movies with the highest profitability ratios.

### 2. Average Revenue per Genre (Action & Drama)
Computed average revenues for Action and Drama genres using string matching techniques.

### 3. Most Expensive Movies Released After 2010
Queried high-budget movies released post-2010.

### 4. Movies with Most Cast Members
Calculated number of cast members using string tricks on JSON-like data in SQLite.

### 5. Classified Movies as 'Hit' or 'Flop'
Used CASE WHEN logic to classify movies where revenue > 2 × budget as 'HIT', others as 'FLOP'.

### 6. Tribute to Daniel Day-Lewis
Special query to analyze Daniel Day-Lewis movies, showing:
- Revenue-to-budget ratio
- Audience score (vote average)

#### Example Result:
| Movie Title                   | Revenue/Budget Ratio | Score |
|-------------------------------|---------------------:|------:|
| There Will Be Blood            | 3.09                | 7.9   |
| Lincoln                        | 4.24                | 6.7   |
| Gangs of New York              | 1.94                | 7.1   |
| The Last of the Mohicans       | 1.89                | 7.1   |

## 🚀 How to Run This Project
1. Load CSVs into SQLite using the provided Python script.
2. Open `movies.db` with SQLite extension in VS Code.
3. Execute queries from `/queries/analysis_queries.sql`.

## 📝 Notes
- Genres were handled via simple string matching (LIKE '%Action%').
- JSON parsing was approximated using SQL string functions.
- Ideal for small-scale SQL exercises and portfolio projects.

## 🧑‍💻 Author
- Christian Valencia Narva
- [GitHub Profile](https://github.com/chrisvn27)
