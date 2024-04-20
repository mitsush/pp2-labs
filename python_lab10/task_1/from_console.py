# Import necessary libraries
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Define a function to add a new contact into the database
def add_contact(first_name, second_name, phone):
    # Establish a connection to the PostgreSQL database using the provided credentials
    conn = psycopg2.connect(
        host="localhost",                    # Database host
        dbname="PhoneBook",                  # Database name
        user="postgres",                     # Database user
        password=os.getenv("PASSWORD"),      # Database password retrieved from environment variables
        port=5432                            # Database port
    )
    # Create a cursor object from the connection
    cur = conn.cursor()
    # SQL command to insert a new contact with given first name, second name, and phone number
    cur.execute("INSERT INTO contacts (first_name, second_name, phone) VALUES (%s, %s, %s)", 
                (first_name, second_name, phone))
    # Commit the transaction to make the changes permanent in the database
    conn.commit()
    # Close the connection to free up database resources
    conn.close()

# Collect input from the user for the first name, second name, and phone number of the new contact
first_name = input("Enter first name: ")
second_name = input("Enter second name: ")
phone = input("Enter phone number: ")

# Call the function with the collected information to add the new contact to the database
add_contact(first_name, second_name, phone)
