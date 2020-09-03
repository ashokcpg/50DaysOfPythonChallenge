# For Colorful Output and Warnings.
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    OKBLUE = '\033[94m'
    ENDC = '\033[0m'

# Function for displaying Welcome Message
def welcomeMessage():
    print(f"""{colors.YELLOW}
-------------------------
| ***Guess To Win!!!*** |
-------------------------
""")
    print(f"""
*************************************
| Please Guess a Number from 1 to 20 |
*************************************{colors.ENDC}
""")
# Main Program Starts...
import random
welcomeMessage()        #Function Call

randomNumber = random.randrange(1,20,1)     #Generating random number.
guesses = 0
while guesses < 5:
    userNumber = int(input("Your Guess: "))
    # print(randomNumber)
    if userNumber > 20 or userNumber < 1:
        print(f"{colors.RED}You must enter a number between 1 and 20. {colors.ENDC}")
    elif userNumber < randomNumber:
        print(f"{colors.OKBLUE}The winning number is GREATER than {userNumber}. {colors.ENDC}")
        guesses += 1
    elif userNumber > randomNumber:
        print(f"{colors.OKBLUE}The winning number is LESS than {userNumber}. {colors.ENDC}")
        guesses += 1
    else:
        print(f"{colors.GREEN}Congratulations!!! You Guessed it right! The Winning Number is {userNumber}. {colors.ENDC}")
        break
if not guesses < 5:
    print(f"{colors.RED}YOU LOSE!!! The winning number is {randomNumber} {colors.ENDC}")