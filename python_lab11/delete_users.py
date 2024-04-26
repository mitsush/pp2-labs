# Import necessary libraries
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Define a function to delete records based on a name or phone number
def delete_record_by_name_or_phone(name=None, phone=None):
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
        
        if name:
            # Deleting records by user name, using case-insensitive matching
            cur.execute("DELETE FROM contacts WHERE first_name ILIKE %s", (name,))
        elif phone:
            # Deleting entries by phone number
            cur.execute("DELETE FROM contacts WHERE phone = %s", (phone,))
        
        # Commit the transaction to make the changes permanent in the database
        conn.commit()
        # Close the cursor and the connection
        cur.close()
        conn.close()
        
        # Print confirmation that the entries have been deleted
        print("The entries have been deleted successfully.")
    except Exception as e:
        # Print any errors that occur during the database operations
        print("An error has occurred:", e)

# Example usage of the function to delete records by user name
# delete_record_by_name_or_phone(name="John")

# Example usage of the function to delete records by phone number
# delete_record_by_name_or_phone(phone="1234567890")
