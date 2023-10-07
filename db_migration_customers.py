import csv

# Function to read data from CSV file
def read_data_from_csv(csv_file):
    data = []
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

# Function to generate the SQL insert statement for Customers table
def generate_sql_insert_customer(churn, account_length, international_plan, voicemail_plan):
    return f"INSERT INTO Customers (churn, account_length, international_plan, voicemail_plan) VALUES ('{churn}', {account_length}, '{international_plan}', '{voicemail_plan}');"

# Replace 'data.csv' with the path to your CSV file containing the required columns
csv_file_path = r'C:\Users\ponna\OneDrive\Desktop\DSS CA1\churn.csv'

# Read data from the CSV file
csv_data = read_data_from_csv(csv_file_path)

# Generate the SQL insert statements for Customers table
sql_insert_statements = []
for row in csv_data:
    sql_insert_statements.append(generate_sql_insert_customer(
        row['churn'], int(row['account_length']), row['international_plan'], row['voicemail_plan']
    ))

# Write the SQL insert statements to the .sql file
with open(r'C:\Users\ponna\OneDrive\Desktop\DSS CA1\V10.0_customers_insert_table.sql', "w") as file:
    for statement in sql_insert_statements:
        file.write(statement + "\n")

print("Generated SQL insert statements for Customers table in mock_data_customers.sql.")
