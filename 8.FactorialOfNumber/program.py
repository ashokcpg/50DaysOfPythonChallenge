Number = 11

# To take input from the user

#Number = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if Number< 0:

   print("The factorial of given number doesnot exist")
   
elif Number == 0:
   print("The factorial of 0 is 1")

else:
   for i in range(1,Number + 1):
       factorial = factorial*i

   print("The factorial of",Number,"is",factorial)

#    Output :
# The factorial of 11 is 39916800



# 2.
# Note: To test the program for a different number, change the value of num.
# Here, the number whose factorial is to be found is stored in num, 
# and we check if the number is negative, zero or positive using if...elif...else statement. 
# If the number is positive, we use for loop and range() function to calculate the factorial.

# 1.
# The factorial of a number is the product of all the integers from 1 to that number.
# For example, the factorial of 6 is 1*2*3*4*5*6 = 720. 
# Factorial is not defined for negative numbers, and the factorial of zero is one, 0! = 1.