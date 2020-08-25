#Python Program to find power of a number using while loop .

Number = int(input("Enter any Positive Integer :"))
exponent = int(input("Enter Exponent Value :"))

power = 1 
i = 1

while(i<= exponent) :
    power = power*Number
    i = i + 1

print("The Result of {0} Power {1} = {2}".format(Number, exponent, power))


# output :

# Enter any Positive Integer :2
# Enter Exponent Value :2
# The Result of 2 Power 2 = 4

# Enter any Positive Integer :22
# Enter Exponent Value :4
# The Result of 22 Power 4 = 234256