# Import necessary libraries
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Define a function to query all contacts from the database and print them
def query_contacts():
    # Establish a connection to the PostgreSQL database using credentials loaded from environment variables
    conn = psycopg2.connect(
        host="localhost",                    # Database host address
        dbname="PhoneBook",                  # Database name
        user="postgres",                     # Database user
        password=os.getenv("PASSWORD"),      # Database password retrieved from environment variables
        port=5432                            # Database port number
    )
    # Create a cursor object from the connection
    cur = conn.cursor()
    # Execute a SQL query to select all entries from the 'contacts' table
    cur.execute("SELECT * FROM contacts")
    # Fetch all rows returned by the executed query
    rows = cur.fetchall()
    # Iterate through each row and print it
    for row in rows:
        print(row)
    # Close the connection to free up database resources
    conn.close()

# Call the function to query all contacts and display them on the screen
query_contacts()
