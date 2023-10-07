import random

# Function to generate a random time (hour, minute, second)
def random_time():
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return hour, minute, second

# Function to generate the SQL insert statement for Time table
def generate_sql_insert_time(hour, minute, second):
    return f"INSERT INTO Time (hour, minute, second) VALUES ({hour}, {minute}, {second});"

# Generate 5000 mock records for Time table
time_records = []
for _ in range(5000):
    time_values = random_time()
    time_records.append(time_values)

# Write the Time records to the .sql file
with open(r"C:\Users\ponna\OneDrive\Desktop\DSS CA1\V8.0_time_insert_table.sql", "w") as file:
    for record in time_records:
        file.write(generate_sql_insert_time(*record) + "\n")

print("Generated 5000 mock records for Time table in mock_data_time.sql.")
