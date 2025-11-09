#!/usr/bin/python3
import seed

def stream_users_in_batches(batch_size):
    """Generator to fetch user_data rows in batches"""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)

    # Execute the query ONCE
    cursor.execute("SELECT * FROM user_data;")

    while True:
        count = 0
        while count < batch_size:
            row = cursor.fetchone()  # fetch one row at a time
            if row is None:
                break
            yield row
            count += 1
        if count == 0:  # no more rows
            break

    cursor.close()
    connection.close()


def batch_processing(batch_size):
    """Process each batch and print users over age 25"""
    for user in stream_users_in_batches(batch_size):
        if user['age'] > 25:
            print(user)

