#!/usr/bin/python3
import mysql.connector
from seed import connect_to_prodev

def stream_users_in_batches(batch_size):
    """Generator function that fetches rows from user_data table in batches"""
    connection = connect_to_prodev()
    if connection:
        cursor = connection.cursor(dictionary=True)
        offset = 0
        while True:
            cursor.execute(
                "SELECT * FROM user_data LIMIT %s OFFSET %s", (batch_size, offset)
            )
            batch = cursor.fetchall()
            if not batch:
                break
            yield batch
            offset += batch_size
        cursor.close()
        connection.close()

def batch_processing(batch_size):
    """Process each batch and print users over age 25"""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)
