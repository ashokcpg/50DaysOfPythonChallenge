# Python Program for Magic Number.

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
