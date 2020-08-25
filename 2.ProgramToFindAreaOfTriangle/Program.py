#Python program to find Area of triangle

#Three sides of triangle a ,b and c are provided by the user


First = float(input('Enter First Side : '))
Second = float(input('Enter Second Side : '))
Third = float(input('Enter Third Side : '))

#Calculate The Semi-Parameter
S = (First + Second + Third)/2

 #Calculate the area
Area = (S*(S-First)*(S-Second)*(S-Third))**0.5
print('The Area Of The Triangle Is %0.2f' %Area)

#output :
#Enter First Side : 33
#Enter Second Side : 22 
#Enter Third Side : 11.1
#The Area Of The Triangle Is 20.02
