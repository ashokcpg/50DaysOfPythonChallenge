largeNum = int(input("Max Number: "))
smallNum = int(input("Small Number: "))

print(f"Palindrome Numbers between {smallNum} and {largeNum} are: ")
for i in range(smallNum, largeNum+1):
    num = str(i)
    if (num[::-1] == num):
        print(f"{num}", end = " ")

# Output

# Max Number: 100
# Small Number: 8
# Palindrome Numbers between 8 and 100 are: 
# 8 9 11 22 33 44 55 66 77 88 99