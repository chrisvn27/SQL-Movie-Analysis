import pandas as pd
import sqlite3
import os

# Define paths
movies_csv = os.path.join('..', 'data', 'tmdb_5000_movies.csv')
credits_csv = os.path.join('..', 'data', 'tmdb_5000_credits.csv')
db_file = os.path.join('..', 'db', 'movies.db')

# Load CSVs into DataFrames
df_movies = pd.read_csv(movies_csv)
df_credits = pd.read_csv(credits_csv)

# Connect to SQLite DB (creates it if it doesn't exist)
conn = sqlite3.connect(db_file)

# Write DataFrames to SQL tables
df_movies.to_sql('movies', conn, if_exists='replace', index=False)
df_credits.to_sql('credits', conn, if_exists='replace', index=False)

# Close connection
conn.close()

print("Database created and CSVs loaded successfully.")
