#PYTHON PROGRAM TO MULTIPLY TWO MATRICES USING NESTED LOOPS HAVING CENTAIN VALUES:

# MATRICS MULTIPLICATION :

# MATRIX MULTIPLICATION IS A Binary OPERATION THAT USES A PAIR MATRICES TO PRODUCE ANOTHER MATRIX
# THE ELEMENTS WITHIN THE MATRIX ARE MULTIPLIED ACCORDING TO ELEMENTARY AIRTHMETIC.

#3*3
X = [[9,8,7],  
       [5,6,8],  
       [9,9,9]]

# 3*4 
Y = [[1,11,12,22],  
      [13,22,15,2],  
      [16,37,38,3]]  

# RESULT IS 3*4
result = [[0,0,0,0],  
               [0,0,0,0],  
              [0,0,0,0]]  
 
#  ITERATE THROUGH ROWS OF X
for i in range(len(X)):  

    #ITERATE THROUGH COLUMNS OF Y
   for j in range(len(Y[0])):  

    #    ITERATE THROUGH ROWS OF Y
       for k in range(len(Y)):  
           result[i][j] += X[i][k] * Y[k][j]
             
for r in result:  
   print(r)  

#    Output :
# [225, 534, 494, 235]
# [211, 483, 454, 146]
# [270, 630, 585, 243]
