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