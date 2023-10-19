import csv
import sqlite3

# Specify the path to your CSV file and the desired SQLite database
csv_file = 'UnitDatabase.csv'
database_file = 'Troops.db'
table_name = 'Units'

# Create a connection to the SQLite database
conn = sqlite3.connect(database_file)
cursor = conn.cursor()

# Open the CSV file and read the header row to create the table schema
with open(csv_file, 'r', newline='') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Units 
            ("Title" text, "Units per Command" integer,
            "Wood Cost" integer, "Ore Cost" integer, "Grain Cost" integer,"Gold Cost" integer, "Conscription Duration" time, "Apothecary Cost" integer, "Apothecary Duration" time
            )''')
    
    # Commit the transaction
    conn.commit()
    
    # Read and insert the data rows into the table
    for row in csv_reader:
        # Generate the INSERT SQL statement
        insert_sql = f"INSERT INTO {table_name} VALUES ({', '.join(['?'] * len(row))})"
        
        # Execute the INSERT SQL statement with row data
        cursor.execute(insert_sql, row)

    # Commit the transaction
    conn.commit()
    for row in conn.execute('''SELECT * FROM Units'''):
        print(row)

# Close the database connection
conn.close()

print(f"Table '{table_name}' created successfully in '{database_file}'.")
