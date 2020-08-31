#Python program to count vowels and Consonants in a string.

strl = input("Enter your string : ")
vowels = 0 
consonants = 0

for i in strl:
    if(i == 'a' or i =='e' or i =='o' or i =='u' or i == 'i'or i =='A' or i =='E' or i =='I' or i =='O' or i == 'U') :
        vowels = vowels + 1
    else :
        consonants = consonants + 1


print("Total Number Of Vowels in this String :  ",vowels)
print("Total Number Of Consonants in this String :  ", consonants)


# Enter your string : Aakrity Chapagai 
# Total Number Of Vowels in this String :   7   
#  Total Number Of Consonants in this String :   9

# Enter your string : helloWorld
# Total Number Of Vowels in this String :   3
# Total Number Of Consonants in this String :   7



