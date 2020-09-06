# Python Program to Print Even Numbers from 1 to N

maximum = int(input("Enter the Maximum Value : "))
for number in range(1, maximum+1):
    if(number % 2 == 0):
        print("{0}".format(number))

# Output :
#Enter the Maximum Value : 20
# 2 
# 4 
# 6 
# 8 
# 10
# 12
# 14
# 16
# 18
# 20