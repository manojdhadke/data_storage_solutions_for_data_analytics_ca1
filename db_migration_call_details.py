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

# Function to generate the SQL insert statement for CallDetails table
def generate_sql_insert_call_details(account_id, number_vmail_messages, total_day_minutes, total_day_calls,
                                     total_day_charge, total_eve_minutes, total_eve_calls, total_eve_charge,
                                     total_night_minutes, total_night_calls, total_night_charge,
                                     number_customer_service_calls):
    return f"INSERT INTO CallDetails (account_id, number_vmail_messages, total_day_minutes, total_day_calls, total_day_charge, total_eve_minutes, total_eve_calls, total_eve_charge, total_night_minutes, total_night_calls, total_night_charge, number_customer_service_calls) VALUES ({account_id}, {number_vmail_messages}, {total_day_minutes}, {total_day_calls}, {total_day_charge}, {total_eve_minutes}, {total_eve_calls}, {total_eve_charge}, {total_night_minutes}, {total_night_calls}, {total_night_charge}, {number_customer_service_calls});"

# Replace 'data.csv' with the path to your CSV file containing the required columns
csv_file_path = r'C:\Users\ponna\OneDrive\Desktop\DSS CA1\churn.csv'

# Read data from the CSV file
csv_data = read_data_from_csv(csv_file_path)

# Generate the SQL insert statements for CallDetails table
sql_insert_statements = []
for row in csv_data:
    sql_insert_statements.append(generate_sql_insert_call_details(
        int(random_id()), int(row['number_vmail_messages']), float(row['total_day_minutes']),
        int(row['total_day_calls']), float(row['total_day_charge']), float(row['total_eve_minutes']),
        int(row['total_eve_calls']), float(row['total_eve_charge']), float(row['total_night_minutes']),
        int(row['total_night_calls']), float(row['total_night_charge']), int(row['number_customer_service_calls'])
    ))

# Write the SQL insert statements to the .sql file
with open(r'C:\Users\ponna\OneDrive\Desktop\DSS CA1\V11.0_call_deatils_insert_table.sql', "w") as file:
    for statement in sql_insert_statements:
        file.write(statement + "\n")

print("Generated SQL insert statements for CallDetails table in mock_data_call_details.sql.")

