import psycopg2
import csv

# Function to create PostgreSQL table
def create_table(cursor, table_name):
    if table_name == "table1":
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS table1 (
            column1 data_type,
            column2 data_type,
            ...
        );
        """)
    elif table_name == "table2":
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS table2 (
            column1 data_type,
            column2 data_type,
            ...
        );
        """)
    # Add more tables as needed

# Function to insert data from CSV file into PostgreSQL table
def insert_data(cursor, table_name, file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        
        for row in reader:
            print(row)
            row = [None if value == 'NULL' else value for value in row]
            cursor.execute(f"""
            INSERT INTO {table_name}
            VALUES (%s, %s,%s);
            """, row)

# Main function to connect to PostgreSQL, create tables, and insert data
def main():
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="minamina",
            host="localhost",
            port="5432"
        )

        # Create a cursor object
        cursor = conn.cursor()

        # Create the database if it doesn't exist
       # cursor.execute("CREATE DATABASE operativna_baza")

        # Switch to the newly created database
        conn.close()
        conn = psycopg2.connect(
            dbname="operativna_baza",
            user="postgres",
            password="minamina",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

     
        
        insert_data(cursor, "stocks", "archive\\stocks.csv")
        
        # Commit changes
        conn.commit()
        print("Data inserted successfully!")

    except (Exception, psycopg2.Error) as error:
        print("Error:", error)

    finally:
        # Close database connection
        if conn:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    main()
