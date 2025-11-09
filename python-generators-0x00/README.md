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
