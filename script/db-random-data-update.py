import mysql.connector
from mysql.connector import Error
from faker import Faker

# Database connection details
host = 'localhost'  # Update if necessary
user = 'adminuser'  # Replace with your MariaDB username
password = 'REDACTED'  # Replace with your MariaDB password
database = 'testdb'

# Create a connection to the database
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        print("Connected to MariaDB")

        cursor = connection.cursor()

        # Initialize the Faker library
        fake = Faker()

        # Fetch the first 1,000 records to update
        cursor.execute("SELECT id FROM sample_table LIMIT 1000")
        records = cursor.fetchall()

        # Update the email field for each record
        update_data = []
        for record in records:
            new_email = fake.email()
            update_data.append((new_email, record[0]))

        cursor.executemany("""
        UPDATE sample_table
        SET email = %s
        WHERE id = %s
        """, update_data)

        connection.commit()
        print(f"Updated {cursor.rowcount} records.")

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MariaDB connection closed.")
