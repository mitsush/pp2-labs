# Import necessary libraries
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",           # Database host address
    dbname="PhoneBook",         # Database name
    user="postgres",            # Database user
    password=os.getenv("PASSWORD"),  # Database password retrieved from environment variables
    port=5432                   # Database port number
)

# Create a cursor object from the connection
cur = conn.cursor()

# SQL command to create a new table if it doesn't already exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,       # 'id' column, auto-increments and serves as the primary key
        first_name VARCHAR(50) NOT NULL,  # 'first_name' column, holds a string up to 50 characters
        second_name VARCHAR(50) NOT NULL, # 'second_name' column, also holds a string up to 50 characters
        phone VARCHAR(20) NOT NULL        # 'phone' column, holds a string up to 20 characters
    )
""")

# Commit the transaction to the database
conn.commit()

# Close the cursor and the connection to release database resources
cur.close()
conn.close()
