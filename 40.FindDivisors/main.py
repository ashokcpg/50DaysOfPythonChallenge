# Python Program To Print All Divisors Of An Integer Number

number = int(input("Enter any Number: "))

print("Divisors of %d are: " %(number))
for i in range(1, number+1):
    if number%i == 0:
        print(i, end=" ")

#Output :
# Enter any Number: 18
# Divisors of 18 are:
# 1 2 3 6 9 18

# In this Python program, we first read number from user. 
# Then we print all divisors using for loop and if statement.