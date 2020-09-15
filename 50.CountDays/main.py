#Python Program to calculate age in days from date of birth in Python.
# particular_date = datetime(1996, 1, 1)


from datetime import datetime, timedelta

birth_date = int(input("Your date of birth(dd mm yyyy): "))

new_date = datetime.today() - birth_date
print (new_date.days)

