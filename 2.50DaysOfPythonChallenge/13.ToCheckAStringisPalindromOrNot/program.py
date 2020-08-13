 my_str = input("Enter a string: ")
 
#Make it suitable for caseless comparison
my_str = my_str.casefold()
 
#Reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse

if list(my_str) == list(rev_str):
   print("It is palindrome")

else:
   print("It is not palindrome")

# Output:
# Enter a string: repaper
# It is palindrome

# Enter a string: aakrity 
# It is not palindrome

# Enter a string: 112211
# It is palindrome

# Enter a string: 2058
# It is not palindrome
