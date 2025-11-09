# Python Generators - 0x00

## Objective
Create a Python generator that streams rows from an SQL database (`user_data` table) one by one, enabling memory-efficient access to large datasets.

## Files
- `seed.py` - Contains functions to:
  - Connect to MySQL
  - Create the database and table
  - Insert data from `user_data.csv`
  - Stream rows using a generator

- `0-main.py` - Demonstrates the usage of the functions in `seed.py`.

- `user_data.csv` - Sample CSV file used to populate the database.

## Usage
1. Update `seed.py` with your MySQL credentials:

```python
user='your_mysql_user'
password='your_mysql_password'

# Python Generators - Batch Processing

## Objective
Create a generator to fetch rows from the `user_data` table in batches and process each batch to filter users over the age of 25.

## Files
- `1-batch_processing.py` - contains two functions:
  - `stream_users_in_batches(batch_size)` - fetches users in batches
  - `batch_processing(batch_size)` - processes each batch and prints users over age 25
- `2-main.py` - tests the batch processing generator

## Usage
1. Ensure MySQL is running and the database `ALX_prodev` exists with the `user_data` table populated.
2. Run the test file:
```bash
python3 2-main.py
