#Using nested loop

X = [[20,58,10],
    [17 ,0,0],
    [2002,1,31]]
 
Y = [[1, 1,11],
    [-8,7,-1],
    [9,522,222]]
 
result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]
 
for r in result:
   print(r)



# Ouput:
#  [21, 59, 21]
# [9, 7, -1]
# [2011, 523, 253]