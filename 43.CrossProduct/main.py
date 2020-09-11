# 

setA = [1,2,3,4]
setB = ['a','b','c']

cross_product = [(i,j) for i in setA for j in setB]

print(cross_product)

# Output :
# [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'),
#  (3, 'a'), (3, 'b'), (3, 'c'), (4, 'a'), (4, 'b'), (4, 'c')]

# Note :
# Cartesian product example: if setA = [1, 2, 3] and setB = [a, b]
#  then output setA X setB = [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]