# Python program to find students Grade

computerFundamental = float(input("Enter Marks in Computer Fundamental :"))
digitalLogic        = float(input("Enter Marks in Digital-Logic :"))
English             = float(input("Enter Marks in English : "))
Math                = float(input("Enter Marks in Math :"))
Programming         = float(input("Enter Marks in Programming :"))

total = computerFundamental + digitalLogic + English + Math + Programming

percentage = (total/500) * 100 

print("Total Marks = %.2f" %total)
print("Marks Percentage = %.2f" %percentage)

# Output :
# Enter Marks in Computer Fundamental :90
# Enter Marks in Digital-Logic :83
# Enter Marks in English : 88
# Enter Marks in Math :70
# Enther Marks in Programming :97
# Total Marks = 428.00    
# Marks Percentage = 85.60
