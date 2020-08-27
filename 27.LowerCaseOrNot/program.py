
#Python Program to check character is Lowercase or Uppercase.

ch = input("Enter Your Character :  ")

if(ch>='a' and ch<='z'):
    print("The Given Character",ch,"is a Lowercase Alphabet.")

else:
    print(f"The Given Character {ch} is Uppercase Alphabet.")

    #Output :
# Enter Your Character :hello world
# The Given Character hello world is a Lowercase Alphabet. 

# Enter Your Character :  A            
# The Given Character A is Uppercase Alphabet.
