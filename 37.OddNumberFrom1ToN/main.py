# Python Program to Print Odd Numbers from 1 to N

maximum = int(input(" Enter any Maximum Value : "))

for number in range(1, maximum + 1, 2):
    print("{0}".format(number))

    # Output :
#     Enter any Maximum Value : 20
# 1 
# 3 
# 5 
# 7 
# 9 
# 11
# 13
# 15
# 17
# 19