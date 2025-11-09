#!/usr/bin/python3
seed = __import__('seed')

connection = seed.connect_db()
if connection:
    seed.create_database(connection)
    connection.close()
    print("Connection successful")

    connection = seed.connect_to_prodev()
    if connection:
        seed.create_table(connection)
        seed.insert_data(connection, 'user_data.csv')

        # Check database
        cursor = connection.cursor()
        cursor.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'ALX_prodev';")
        result = cursor.fetchone()
        if result:
            print("Database ALX_prodev is present")
        cursor.close()

        # Stream first 5 rows
        print("First 5 rows from user_data:")
        for i, row in enumerate(seed.stream_rows(connection)):
            print(row)
            if i >= 4:  # only 5 rows
                break

        connection.close()
