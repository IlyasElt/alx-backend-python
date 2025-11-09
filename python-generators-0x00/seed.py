import mysql.connector
from mysql.connector import Error
import csv
import uuid

def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your_mysql_user',
            password='Tyour_mysql_password'
        )
        if connection.is_connected():
            print("Connected to MySQL server")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
    cursor.close()

def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your_mysql_user',
            password='your_mysql_password',
            database='ALX_prodev'
        )
        if connection.is_connected():
            print("Connected to ALX_prodev databse")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL,
            UNIQUE KEY (email)
            )
    """)
    cursor.close()
    print("Table user_data created successfully")

def insert_data(connection, data):
    cursor = connection.cursor()
    with open(data, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user_id = str(uuid.uuid4())
            name = row['name']
            email = row['email']
            age = row['age']
            cursor.execute("""
                INSERT IGNORE INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
                """, (user_id, name, email, age))

    connection.commit()
    cursor.close()

def stream_rows(connection):
    cursor = connection.cursor(dictionary = True)
    cursor.execute("SELECT * FROM user_data;")
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        yield row
    cursor.close()

