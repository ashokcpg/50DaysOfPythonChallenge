#Python program to print palindrome numbers from 1 to 100 using loop:

maximum = int(input(" Enter the Maximum Value : "))
minimum = int(input(" Enter the minimum Value : "))

print("Palindrome Numbers between %d and %d are : " %(minimum, maximum))
print(f"Palindrome Numbers  Are : ")

for num in range(1, maximum + 1):
    temp = num
    reverse = 0
    
    while(temp > 0):
        Reminder = temp % 10
        reverse = (reverse * 10) + Reminder
        temp = temp //10

    if(num == reverse):
        print("%d " %num, end = '  ')

    #  Output :

# Enter the Maximum Value : 100
#  Enter the minimum Value : 1
# Palindrome Numbers between 1 and 100 are :
# 1   2   3   4   5   6   7   8   9   11   22   33   44   55   66   77   88   99   