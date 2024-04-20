# Import necessary libraries
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Define a function to delete a contact by name from the database
def delete_contact_by_name(name):
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        dbname="PhoneBook",                # Database name
        user="postgres",                   # Database user
        password=os.getenv("PASSWORD"),    # Database password retrieved from environment variables
        host="localhost"                   # Database host
    )
    # Create a cursor object from the connection
    cur = conn.cursor()
    # SQL command to delete contact where the first or second name matches the provided name
    cur.execute("DELETE FROM contacts WHERE first_name = %s OR second_name = %s", (name, name))
    # Commit the transaction to the database
    conn.commit()
    # Close the connection to free up resources
    conn.close()

# Define a function to delete a contact by phone number from the database
def delete_contact_by_phone(phone):
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        dbname="PhoneBook",                # Database name
        user="postgres",                   # Database user
        password=os.getenv("PASSWORD"),    # Database password retrieved from environment variables
        host="localhost"                   # Database host
    )
    # Create a cursor object from the connection
    cur = conn.cursor()
    # SQL command to delete contact where the phone number matches the provided number
    cur.execute("DELETE FROM contacts WHERE phone = %s", (phone,))
    # Commit the transaction to the database
    conn.commit()
    # Close the connection to free up resources
    conn.close()

# Call the function to delete a contact by name
delete_contact_by_name('name')
# Call the function to delete a contact by phone number
delete_contact_by_phone('phone')
