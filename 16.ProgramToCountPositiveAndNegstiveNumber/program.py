#PROGRAM TO COUNT POSITIVE AND NEGATIVE NUMBERS IN A LIST


listOfNumber = [20, 60, -2, 10, 20, -3, 20, 2, 1,31] 
  
pos_count, neg_count = 0, 0
  
# ITERATINF EACH NUMBER IN each number in list 
for num in listOfNumber: 
      
    # CHECKING CONDITION
    if num >= 0: 
        pos_count += 1
    else: 
        neg_count += 1
          
print("Positive numbers in the list: ", pos_count) 
print("Negative numbers in the list: ", neg_count) 