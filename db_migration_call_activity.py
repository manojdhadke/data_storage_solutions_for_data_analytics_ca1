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

# Function to generate the SQL insert statement for CallActivity table
def generate_sql_insert_call_activity(account_id, date_id, time_id, international_plan_id,
                                      voicemail_plan_id, numbervmailmessages, totaldayminutes, totaldaycalls,
                                      totaldaycharge, totaleveminutes, totalevecalls, totalevecharge,
                                      totalnightminutes, totalnightcalls, totalnightcharge,
                                      totalintlminutes, totalintlcalls, totalintlcharge, numbercustomerservicecalls,
                                      churn_id):
    return f"INSERT INTO CallActivity (account_id, date_id, time_id, international_plan_id, voicemail_plan_id, numbervmailmessages, totaldayminutes, totaldaycalls, totaldaycharge, totaleveminutes, totalevecalls, totalevecharge, totalnightminutes, totalnightcalls, totalnightcharge, totalintlminutes, totalintlcalls, totalintlcharge, numbercustomerservicecalls, churn_id) VALUES ({account_id}, {date_id}, {time_id}, {international_plan_id}, {voicemail_plan_id}, {numbervmailmessages}, {totaldayminutes}, {totaldaycalls}, {totaldaycharge}, {totaleveminutes}, {totalevecalls}, {totalevecharge}, {totalnightminutes}, {totalnightcalls}, {totalnightcharge}, {totalintlminutes}, {totalintlcalls}, {totalintlcharge}, {numbercustomerservicecalls}, {churn_id});"

# Replace 'data.csv' with the path to your CSV file containing the required columns
csv_file_path = r'C:\Users\ponna\OneDrive\Desktop\DSS CA1\churn.csv'

# Read data from the CSV file
csv_data = read_data_from_csv(csv_file_path)


# Generate the SQL insert statements for CallActivity table
sql_insert_statements = []

# Generate the SQL insert statements for CallActivity table
sql_insert_statements = []
for i, row in enumerate(csv_data, 1000):  # Start call_activity_id from 1000    
    sql_insert_statements.append(generate_sql_insert_call_activity(
        random_id(), random_id(), random_id(), random_id(),
        random_id(), row['numbervmailmessages'], row['totaldayminutes'], row['totaldaycalls'],
        row['totaldaycharge'], row['totaleveminutes'], row['totalevecalls'], row['totalevecharge'],
        row['totalnightminutes'], row['totalnightcalls'], row['totalnightcharge'], row['totalintlminutes'],
        row['totalintlcalls'], row['totalintlcharge'], row['numbercustomerservicecalls'], random_id()
    ))

# Write the SQL insert statements to the .sql file
with open(r"C:\Users\ponna\OneDrive\Desktop\DSS CA1\V9.0_call_activity_insert_table.sql", "w") as file:
    for statement in sql_insert_statements:
        file.write(statement + "\n")

print("Generated SQL insert statements for CallActivity table in call_activity_insert_table.sql.")
