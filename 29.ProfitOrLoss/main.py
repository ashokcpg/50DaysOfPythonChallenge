#Program to calculate profit or loss .

cp = float(input("Enter the Cost Price : "))
sp = float(input("Enter the Selling Price : "))

if sp>cp :
    amount = sp - cp
    print(f"Total Profit Amount is",amount)

elif cp>sp :
    amount = cp - sp
    print(f"Total Loss Amount is",amount)
else:
    print("No Profit No Loss!!!")

# Enter the Cost Price : 100
# Enter the Selling Price : 120
# Total Profit Amount is 20.0

# Enter the Cost Price : 100
# Enter the Selling Price : 90
# Total Loss Amount is 10.0

# Enter the Cost Price : 1000
# Enter the Selling Price : 1000
# No Profit No Loss!!!

