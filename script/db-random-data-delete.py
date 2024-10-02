import mysql.connector
from mysql.connector import Error

# Database connection details
host = 'localhost'  # Update if necessary
user = 'adminuser'  # Replace with your MariaDB username
password = 'REDACTED'  # Replace with your MariaDB password
database = 'testdb'

def delete_records(record_count):
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

            # Delete the specified number of records from sample_table
            delete_query = f"DELETE FROM sample_table LIMIT {record_count}"
            cursor.execute(delete_query)
            connection.commit()

            print(f"Deleted {record_count} records from 'sample_table'.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MariaDB connection closed.")

# Example usage
if __name__ == "__main__":
    record_count = int(input("Enter the number of records to delete: "))
    delete_records(record_count)
