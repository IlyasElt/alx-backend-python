#!/usr/bin/python3
import seed

def stream_users_in_batches(batch_size):
    """Generator to fetch user_data rows in batches"""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    offset = 0

    while True:
        cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (batch_size, offset))
        batch = cursor.fetchall()
        if not batch:
            break
        yield batch
        offset += batch_size

    cursor.close()
    connection.close()


def batch_processing(batch_size):
    """Process batches and print users over 25"""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)
