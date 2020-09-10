def is_automorphic(n):
    square = n * n

    while n:
        square_remainder = square%10
        number_remainder = n%10

        if square_remainder != number_remainder:
            return False

        n //= 10
        square //= 10

    return True

number = int(input('Enter number: '))

if is_automorphic(number):
    print('%d is AUTOMORPHIC' %(number))
else:
    print('%d is NOT AUTOMORPHIC' %(number))

    # Output :
    # Enter number: 45
    # 45 is NOT AUTOMORPHIC

    # Enter number: 5
    # 5 is AUTOMORPHIC


    # Note :
    # A number is called Automorphic or Cyclic number if and only if its square ends in 
    # the same digits as the number itself.

# Automorphic or Cyclic Number Examples: 52 = 25, 62 = 36, 762 = 5776, 3762 = 141376

# List of Automorphic Numbers: 0, 1, 5, 6, 25, 76, 376, 625, 9376, 90625, 
# # 109376, 890625, 2890625, 7109376, 12890625, 87109376
