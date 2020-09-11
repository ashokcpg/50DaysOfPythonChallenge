#Python program to Reverse Order Natural Number :

Number = int(input("Enter any Number :"))
i =  Number

print("List of Numbers From {0} to 1 in Reverse Order :".format(Number))

while (i >= 1):
    print (i, end = '  ')
    i = i - 1

# Output :
#     Enter any Number :18
# List of Numbers From 18 to 1 in Reverse Order :
# 18  17  16  15  14  13  12  11  10  9  8  7  6  5  4  3  2  1