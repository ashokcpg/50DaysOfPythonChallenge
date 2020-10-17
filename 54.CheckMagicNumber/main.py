# Python Program for Magic Number.
# Note : A Magic number is that Number whose repeated 
# Sum if its digits till we get a single digit is equal to 1.

import math

num = int(input("Enter any number :"))
digit_count = int(math.log10(num))+1
sum_of_digit = 0

temp = num 

while(digit_count>1):

    sum_of_digit = 0

    while(temp > 0):
        sum_of_digit += temp%10
        temp = temp//10

    temp = sum_of_digit
    digit_count = int(math.log10(sum_of_digit))+1

if(sum_of_digit == 1):
    print("Magic Number")
else:
    print("Not a Magic Number")

    # Output :Enter any number :515124
        # Not a Magic Number

    #Enter any number :3232
        # Magic Number

# Example :
    # 3 2 3 2 = 10
    # 1+0
    # 1 , Here sum is equal to 1 so it is a magic number.

# 5 1 5 1 2 = 14
# 1 + 4 
# 5 Sum is not equal to 1 so, it is not magc number.

# calculate the sum of the digits until get a single-digit number as the sum. To count the number of digits we use math.log10()+1.
# if sum is equal to 1 then it is a Magic number else not.
