
# Program to sort alphabetically the words form a string provided by the user
my_str = "Hello I Am Aakrity Chapagai "

# To take input from the user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = my_str.split()

# sort the list
words.sort()

# display the sorted words
print("The sorted words are:")
for word in words:
   print(word)

#    Note :

# To test the program, change the value of my_str.
# In this program, we store the string to be sorted in my_str. Using the split() method 
# the string is converted into a list of words. The split() method splits the string at whitespaces.
# The list of words is then sorted using the sort() method, and all the words are displayed.