# Pyhton Program to check character is Alphabet or not 

ch = input("Enter Your Character :")

if((ch>='a' and ch<='z') or (ch>'A' and ch<='Z')) :
    print("The GIven Character", ch,"is an Alphabet")

else :
         print("The Given Character", ch,"is Not an Alphabet")

#  Output :
# Enter Your Character :MaNgO
# The GIven Character MaNgO is an Alphabet

# Enter Your Character :123
# The Given Character 123 is Not an Alphabet
