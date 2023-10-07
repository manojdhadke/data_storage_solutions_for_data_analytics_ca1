import csv
import random

# Function to generate a random value between 1001 and 5000 (inclusive)
def random_id():
    return random.randint(1001, 5000)

# Function to read data from CSV file
def read_data_from_csv(csv_file):
    data = []
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

# Function to generate the SQL insert statement for InternationalCalls table
def generate_sql_insert_international_calls(account_id, total_intl_minutes, total_intl_calls, total_intl_charge):
    return f"INSERT INTO InternationalCalls (account_id, total_intl_minutes, total_intl_calls, total_intl_charge) VALUES ({account_id}, {total_intl_minutes}, {total_intl_calls}, {total_intl_charge});"

# Replace 'data.csv' with the path to your CSV file containing the required columns
csv_file_path = r'C:\Users\ponna\OneDrive\Desktop\DSS CA1\churn.csv'

# Read data from the CSV file
csv_data = read_data_from_csv(csv_file_path)

# Generate the SQL insert statements for InternationalCalls table
sql_insert_statements = []
for row in csv_data:
    sql_insert_statements.append(generate_sql_insert_international_calls(
        random_id(), row['total_intl_minutes'],
        row['total_intl_calls'], row['total_intl_charge'])
    )

# Write the SQL insert statements to the .sql file
with open(r"C:\Users\ponna\OneDrive\Desktop\DSS CA1\V12.0_international_calls_insert_table.sql", "w") as file:
    for statement in sql_insert_statements:
        file.write(statement + "\n")

print("Generated SQL insert statements for InternationalCalls table in mock_data_international_calls.sql.")
