# Import necessary libraries
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Define a function to search for records based on a pattern
def search_records(pattern):
    try:
        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(
            host="localhost",                    # Database host
            dbname="PhoneBook",                  # Database name
            user="postgres",                     # Database user
            password=os.getenv("PASSWORD"),      # Database password retrieved from environment variables
            port=5432                            # Database port
        )
        # Create a cursor object from the connection
        cur = conn.cursor()
        
        # SQL query to find records where any of the specified fields match the pattern
        query = "SELECT * FROM contacts WHERE first_name ILIKE %s OR second_name ILIKE %s OR phone LIKE %s"
        # Execute the query with pattern matching for first name, second name, or phone
        cur.execute(query, ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%'))
        
        # Fetch all matching rows
        rows = cur.fetchall()
        
        # Close the cursor and the connection
        cur.close()
        conn.close()
        
        # Return the fetched rows
        return rows
    except Exception as e:
        # Print any errors that occur during the database operations
        print("An error occurred:", e)

# Collect input from the user for the search pattern
pattern = input("Enter search pattern: ")
# Call the function to search for records matching the pattern
matching_records = search_records(pattern)
# Check if there are any matching records and print them
if matching_records:
    for record in matching_records:
        print(record)
else:
    # Inform the user if no records are found that match the pattern
    print("No matching records found.")
