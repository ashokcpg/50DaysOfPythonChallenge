Number = int(input("Enter any Positive Integer :"))

if((Number % 5 == 0)and(Number % 11 == 0)) :
    print(f"Given Number {Number} is Divisible by 5 and 11")
else :
    print("Given Number {0} is Not Divisible by 5 and 11".format(Number))

# Output :
#  Enter any Positive Integer :55
# Given Number 55 is Divisible by 5 and 11

# Enter any Positive Integer :111
# Given Number 111 is Not Divisible by 5 and 11