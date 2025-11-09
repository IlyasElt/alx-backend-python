#!/usr/bin/python3
import seed

def stream_users_in_batches(batch_size):
    """Generator to fetch user_data rows in batches lazily"""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    
    while True:
        batch_count = 0
        while batch_count < batch_size:
            row = cursor.fetchone()
            if row is None:
                break
            yield row
            batch_count += 1

        if batch_count == 0:
            break  # No more rows in DB

    cursor.close()
    connection.close()


def batch_processing(batch_size):
    """Process users over age 25 using generator"""
    for user in stream_users_in_batches(batch_size):
        if user['age'] > 25:
            print(user)
