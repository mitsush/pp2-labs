# Import necessary libraries
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",                    # Database host address
    dbname="PhoneBook",                  # Database name
    user="postgres",                     # Database user
    password=os.getenv("PASSWORD"),      # Database password retrieved from environment variables
    port=5432                            # Database port number
)

# Create a cursor object from the connection
cur = conn.cursor()

# Open the CSV file in read mode
with open('data.csv', 'r') as f:
    next(f)  # Skip the header row of the CSV file
    # Use the cursor's copy_from method to copy data from the CSV file to the database
    cur.copy_from(f, 'contacts', sep=',', columns=('first_name', 'second_name', 'phone'))

# Commit the transaction to the database to make the changes permanent
conn.commit()

# Close the connection to release database resources
conn.close()
