lowerNum = int(input("Enter the lower number: "))
upperNum = int(input("Enter the upper number: "))

print("Prime numbers between", lowerNum, "and", upperNum, "are:")

for num in range(lowerNum, upperNum + 1):
    # num = 4
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)