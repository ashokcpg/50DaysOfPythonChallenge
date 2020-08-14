#Python3 Program to find sum of square of first n nature numbers.

# Function to return the sum of square of first n natural numbers:
def squareSum(num):
    sum = 0
    for i in range(1, num+1):
        sum = sum + (i * i)
    return sum
#Main Function
number = int(input("Enter the number: "))
print(f"The sum of square of numbers from 1 to {number} is : ")
print(squareSum(number))

#Output :
# Enter the number: 4
# The sum of square of numbers from 1 to 4 is : 
# 30