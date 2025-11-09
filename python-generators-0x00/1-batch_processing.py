#!/usr/bin/python3
import seed

def stream_users_in_batches(batch_size):
    """
    Generator that yields batches of users from the database
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    offset = 0

    while True:
        cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s;", (batch_size, offset))
        batch = cursor.fetchall()
        if not batch:
            break
        yield batch
        offset += batch_size

    cursor.close()
    connection.close()


def batch_processing(batch_size):
    """
    Process each batch and print users over the age of 25
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:  # second loop
            if user['age'] > 25:
                print(user)
