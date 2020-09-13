# Python Program to Remove Punctuations From a String

# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and went."

# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)

# Output :
# Hello he said and went

# Note :
# In this program, we first define a string of punctuations. Then, we iterate over the provided string using a for loop.
# In each iteration, we check if the character is a punctuation mark or not using the membership test. 
# We have an empty string to which we add (concatenate) the character if it is not punctuation. Finally, we display the cleaned up string.

# This program removes all punctuations from a string. 
# We will check each character of the string using for loop. 
# If the character is a punctuation, empty string is assigned to it.