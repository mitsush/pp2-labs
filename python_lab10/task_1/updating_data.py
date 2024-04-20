# Import necessary libraries
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Define a function to update the name of a contact
def update_contact_name(old_name, new_name):
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        dbname="PhoneBook",                # Database name
        user="postgres",                   # Database user
        password=os.getenv("PASSWORD"),    # Database password retrieved from environment variables
        host="localhost"                   # Database host
    )
    # Create a cursor object from the connection
    cur = conn.cursor()
    # Update the first name of the contact where it matches the old name
    cur.execute("UPDATE contacts SET first_name = %s WHERE first_name = %s", (new_name, old_name))
    # Update the second name of the contact where it matches the old name
    cur.execute("UPDATE contacts SET second_name = %s WHERE second_name = %s", (new_name, old_name))
    # Commit the transaction to make the changes permanent in the database
    conn.commit()
    # Close the connection to free up database resources
    conn.close()

# Define a function to update the phone number of a contact
def update_contact_phone(name, new_phone):
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        dbname="PhoneBook",                # Database name
        user="postgres",                   # Database user
        password=os.getenv("PASSWORD"),    # Database password retrieved from environment variables
        host="localhost"                   # Database host
    )
    # Create a cursor object from the connection
    cur = conn.cursor()
    # Update the phone number of the contact where the first or second name matches the given name
    cur.execute("UPDATE contacts SET phone = %s WHERE first_name = %s OR second_name = %s", (new_phone, name, name))
    # Commit the transaction to make the changes permanent in the database
    conn.commit()
    # Close the connection to free up database resources
    conn.close()

# Call the function to update a contact's name
update_contact_name('old_name', 'new_name')
# Call the function to update a contact's phone number
update_contact_phone('name', 'new_phone')
