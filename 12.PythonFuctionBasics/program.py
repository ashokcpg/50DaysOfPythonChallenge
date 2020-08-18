def simpleInterest(P,T,R):
    # Function Body
    return(P*T*R/100)

principle = int(input("Enter the Principle :"))
year = int(input("Enter the Year :"))
rate = int(input("Enter the Rate :"))
print("The interest is: ")
interest = simpleInterest(principle,year,rate) #Function Calling 
print(interest)

# Enter the Principle :1000
# Enter the Year :5
# Enter the Rate :10
# The interest is: 
# 500.0
   