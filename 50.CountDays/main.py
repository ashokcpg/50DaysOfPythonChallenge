#Python Program to calculate age in days from date of birth in Python.


import datetime

birth_date = input('Enter your date of birth (dd mm yyyy): ')

birth_day = int(birth_date[0:2])
birth_month = int(birth_date[3:5])
birth_year = int(birth_date[6:])

todays_date = datetime.datetime.now()
current_day = todays_date.day
current_month = todays_date.month
current_year = todays_date.year

# Calculate current date in days
current_date_in_days = current_year * 365 + current_month * 30 + current_day

# Calculate birth date in days
birth_date_in_days = birth_year * 365 + birth_month * 30 + birth_day

# Calculate the number of leap years after the birth which is equal to the number of leap days
leap_days = (current_year - birth_year) // 4

# Calculate age in days
age = current_date_in_days - birth_date_in_days + leap_days

if (age == 1):
    print("Your age: " + str(age) + " day.")
else:
    print("Your age: " + str(age) + " days.")

