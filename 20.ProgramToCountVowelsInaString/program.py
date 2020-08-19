#Program to count vowels and Consonants in string

strl = input("Enter Your Own String :")
vowels = 0
consonants = 0

for i in strl:
    if(i =='a' or i =='e' or i =='i' or i =='o' or i =='u' or i =='A' or  i =='E' or i =='I' or i =='O' or i =='U' ):
        vowels = vowels + 1
    else:
        consonants = consonants + 1

print(f"Total Number of Vowels is {vowels} and Number of Consonants is {consonants}")

#Output :Enter Your Own String: Aakrity Chapagai 
#  Total Number of Vowels is 7 and Number of Consonants is 9