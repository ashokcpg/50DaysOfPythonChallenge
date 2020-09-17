#Python Program to calculate age in days from date of birth in Python.
# particular_date = datetime(1996, 1, 1)


# from datetime import datetime, timedelta

# birth_date = int(input("Your date of birth(dd mm yyyy): "))

# new_date = datetime.today() - birth_date
# print (new_date.days)

# Online Python - IDE, Editor, Compiler, Interpreter

import datetime

# Take input for birth date
birth_date = input('Enter your date of birth (dd mm yyyy): ')

# Grab required fields from the input birth_date using list comprehension
birth_day = int(birth_date[0:2])
birth_month = int(birth_date[3:5])
birth_year = int(birth_date[6:])

# Grab required fields from todays date (Ref: https://docs.python.org/3/library/datetime.html)
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

