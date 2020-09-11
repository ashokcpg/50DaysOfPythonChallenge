# Python Program To Find Cartesian (Cross) Product Of Multiple List.

import itertools

multiple_list = [
    [1, 2, 3],
    ['a', 'b', 'c'],
    ['d', 'e', 'f']
]

result = []
for item in itertools.product(*multiple_list):
    result.append(item)

print(result)

# Output :

# [(1, 'a', 'd'), (1, 'a', 'e'), (1, 'a', 'f'), (1, 'b', 'd'), (1, 'b', 'e'),
#  (1, 'b', 'f'), (1, 'c', 'd'), (1, 'c', 'e'), (1, 'c', 'f'), (2, 'a', 'd'),(2, 'a', 'e'), 
#  (2, 'a', 'f'), (2, 'b', 'd'), (2, 'b', 'e'), (2, 'b', 'f'), (2, 'c', 'd'), (2, 'c', 'e'), 
# (2, 'c', 'f'), (3, 'a', 'd'), (3, 'a', 'e'), (3, 'a', 'f'), (3, 'b', 'd'), (3, 'b', 'e'),
#  (3, 'b', 'f'), (3, 'c', 'd'), (3, 'c', 'e'), (3, 'c', 'f')]


# Note : This python Program Calculates Cratesian (cross) Product of multiple list
# using (intertools.product.)
