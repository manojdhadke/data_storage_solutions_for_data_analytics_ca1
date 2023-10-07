import csv

# Function to generate SQL INSERT statement for a specific column
def generate_insert_query(table_name, column_name, values):
    query = f"INSERT INTO {table_name} ({column_name}) VALUES "
    value_list = [f"('{value}')" for value in values]
    query += ", ".join(value_list) + ";"
    return query

# Replace 'your_file.csv' with the path to your CSV file
csv_file_path = r'C:\Users\ponna\OneDrive\Desktop\DSS CA1\churn.csv'

# Replace 'your_table_name' with the name of your table
table_name = "VoicemailPlan"

# Replace 'your_column_name' with the column name you want to extract
column_name = "voicemail_plan"

# Extract the desired column from the CSV file
values_to_insert = []
with open(csv_file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        value = row[column_name]
        values_to_insert.append(value)

# Generate the SQL INSERT queries and write them to an SQL file
sql_file_path = r'C:\Users\ponna\OneDrive\Desktop\DSS CA1\V6.0_voicemail_plan_insert_table.sql'
with open(sql_file_path, 'w') as sqlfile:
    for value in values_to_insert:
        insert_query = generate_insert_query(table_name, column_name, [value])
        sqlfile.write(insert_query + "\n")

print(f"SQL insert queries have been written to '{sql_file_path}'.")