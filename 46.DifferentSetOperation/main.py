#Python Program to Illustrate Different Set Operations like in mathematics :

A = {0,3,6,9,12,15};
B = {1,2,4,5,7,8,14}

print("Union of A and B is",A | B)

print("Intersection of A and B is",A & B)

print("Difference of A and B is",A - B)

print("Difference of B and A is",B - A)



# Output :

# Union of A and B is {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 14, 15}

# Intersection of A and B is set()
# Difference of A and B is {0, 3, 6, 9, 12, 15}

# Difference of B and A is {1, 2, 4, 5, 7, 8, 14}

# Symmetric difference of A and B is {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12,
#  14, 15}
