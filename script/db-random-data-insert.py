
#pip3 install mysql-connector-python faker

import mysql.connector
from mysql.connector import Error
from faker import Faker

# Database connection details
host = 'localhost'  # Update if necessary
user = 'adminuser'  # Replace with your MariaDB username
password = 'REDACTED'  # Replace with your MariaDB password
database = 'testdb'

def insert_data(total_records):
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

            # Create a sample table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS sample_table (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(100),
                age INT,
                address TEXT
            )
            """)
            print("Table 'sample_table' created or already exists.")

            # Initialize the Faker library
            fake = Faker()

            # Determine batch size (for performance optimization)
            batch_size = 1000

            # Calculate number of full batches and remaining records
            full_batches = total_records // batch_size
            remaining_records = total_records % batch_size

            # Insert records in full batches
            for _ in range(full_batches):
                batch_data = []
                for _ in range(batch_size):
                    name = fake.name()
                    email = fake.email()
                    age = fake.random_int(min=18, max=80)
                    address = fake.address()
                    batch_data.append((name, email, age, address))
                
                cursor.executemany("""
                INSERT INTO sample_table (name, email, age, address)
                VALUES (%s, %s, %s, %s)
                """, batch_data)

                connection.commit()
                print(f"Inserted {len(batch_data)} records.")

            # Insert any remaining records
            if remaining_records > 0:
                batch_data = []
                for _ in range(remaining_records):
                    name = fake.name()
                    email = fake.email()
                    age = fake.random_int(min=18, max=80)
                    address = fake.address()
                    batch_data.append((name, email, age, address))
                
                cursor.executemany("""
                INSERT INTO sample_table (name, email, age, address)
                VALUES (%s, %s, %s, %s)
                """, batch_data)

                connection.commit()
                print(f"Inserted {len(batch_data)} records.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MariaDB connection closed.")

# Example usage
if __name__ == "__main__":
    total_records = int(input("Enter the total number of records to insert: "))
    insert_data(total_records)
