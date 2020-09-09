# Function to print binary number using recursion
def convertToBinary(n):

    #The function converts decimal number to binary and prints it 
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

#Decimal Number
dec = 333
convertToBinary(dec)
print()

# Output :
# 101001101


#  we have defined a function decimalToBinary() for the conversion. 
# This function takes the decimal number as an input parameter and converts it into an equivalent binary number.