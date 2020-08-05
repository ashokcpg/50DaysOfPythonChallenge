#Python program to find the largest number among the three input numbers given by user.

#The Three Numbers are Stored in Number1 , Number2 and Number3 Respectively,

Number1 = float(input("Enter first number: "))
Number2 = float(input("Enter second number: "))
Number3 = float(input("Enter third number: "))
 
if (Number1 >= Number2) and (Number1 >= Number3):
   largest = Number1
   
elif (Number2 >= Number1) and (Number2 >= Number3):
   largest = Number2

else:
   largest = Number3

print("The largest number is", largest)

#Output :
#Enter first number: 45
#Enter second number: 50
#Enter third number: 55
#The largest number is 55.0