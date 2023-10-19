import csv
import sqlite3
# this launches when the bot first starts up -Gellator
csv_file = 'UnitDatabase.csv'
database_file = 'Troops.db'
table_name = 'Units'

# Specify the path to your CSV file and the desired SQLite database
    # Create a connection to the SQLite database
conn = sqlite3.connect(database_file)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Units 
            (Title text, Units_per_Command integer,
            Wood_Cost integer, Ore_Cost integer, Grain_Cost integer,Gold_Cost integer, Conscription_Duration time, Apothecary_Cost integer, Apothecary_Duration time
            )''')
        # Commit the transaction
conn.commit()

with open(csv_file, 'r', newline='') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
        # Read and insert the data rows into the table
    for row in csv_reader:
            # Generate the INSERT SQL statement
            insert_sql = f"INSERT INTO {table_name} VALUES ({', '.join(['?'] * len(row))})"
        
            # Execute the INSERT SQL statement with row data
            cursor.execute(insert_sql, row)

        # Commit the transaction
    conn.commit()

    # Close the database connection
    conn.close()


def StartUp():
    
    # Specify the path to your CSV file and the desired SQLite database
    # Create a connection to the SQLite database
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
    
        cursor.execute('''CREATE TABLE IF NOT EXISTS Units 
            (Title text, Units_per_Command integer,
            Wood_Cost integer, Ore_Cost integer, Grain_Cost integer,Gold_Cost integer, Conscription_Duration time, Apothecary_Cost integer, Apothecary_Duration time
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

        # Close the database connection
        conn.close()


def GetCostPerUnit(unit):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    for row in conn.execute('''SELECT * FROM Units WHERE unit = Title '''):
        print(row)
    conn.close()

#if __name__ == "__main__":
    #StartUp()
    #GetCostPerUnit("Fellbeast")