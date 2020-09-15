number = int(input("Enter number: "))

# Finding sum
total_sum = 0
step = 1

condition = True

while condition:
    
    while number:
        total_sum += number%10
        number //= 10
    
    print("Step-%d Sum: %d" %(step, total_sum))
    number = total_sum
    total_sum = 0
    step += 1
    condition = number > 9

    # Output :

    # Enter number: 222222
    # Step-1 Sum: 12
    # Step-2 Sum: 3

    # Note :
    # This Python program calculates sum of digit of a given
    #  number until number reduces to single digit.

    # In this program, we first read number from user.
    #  Then we use nested while loop to calculate sum of 
    # digit until number reduces to single digit. 
    # We also display sum at each step.