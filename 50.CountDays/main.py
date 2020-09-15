
from datetime import date

birth_date = date(2002, 1, 31)
current_date = date(2020, 9, 15)

delta = current_date - birth_date

print("Number of days from your Birthdays = ",delta.days)
