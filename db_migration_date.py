import random
import datetime

# Function to generate a random date after the year 2000
def random_date():
    start_date = datetime.date(2000, 1, 1)
    end_date = datetime.date.today()
    time_difference = (end_date - start_date).days
    random_days = random.randint(0, time_difference)
    return start_date + datetime.timedelta(days=random_days)

# Function to generate a random day of the week
def random_day_of_week():
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return random.choice(days_of_week)

# Function to generate the SQL insert statement
def generate_sql_insert(date, year, month, day, day_of_week):
    return f"INSERT INTO Date (date, year, month, day, day_of_week) VALUES ('{date}', {year}, {month}, {day}, '{day_of_week}');"

# Generate 5000 mock records
records = []
for i in range(1001, 6001):
    date_obj = random_date()
    records.append((date_obj, date_obj.year, date_obj.month, date_obj.day, random_day_of_week()))

# Write the records to the .sql file
with open(r"C:\Users\ponna\OneDrive\Desktop\DSS CA1\V7.0_date_insert_table.sql", "w") as file:
    for record in records:
        file.write(generate_sql_insert(*record) + "\n")

print("Generated 5000 mock records in date_insert_table.sql.")
