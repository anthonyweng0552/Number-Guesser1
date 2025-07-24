import math
import random
def Line():
    print("-"*30)
def main():
    print("I'm thinking of a number between 1 and 10\nYou have 3 attempts to guess the number")
    Attempts = 0
    Max_Attempts = 3
    Number = round(random.random() * 9)
    Number += 1
    Line()
    while Attempts < Max_Attempts:
        guess = int(input(f"Guess {Attempts + 1}: "))
        Attempts += 1

        if guess > 10:
            print("Please pick one between 1-10")
        if guess == Number:
            print("You got it!")
            break
        elif guess < Number:
            print("Your number is too low!")
        elif guess > Number:
            print("Your number is too high!")
        else:
            print("Give an answer that is an integer.") 

        print(f"You have {(Max_Attempts - Attempts)} attempts left!")
        Line()
        
    if Attempts >= 3 and guess != Number:
        print(f"You've hit the max number of Attempts\nYou lost!\nThe number was {Number}")
while True:
    main()
    while True:
        Again = str(input("Would you like to play again? (Yes/No)\n"))
        if Again.lower() == "yes":
            Line()
            break
        elif Again.lower() == "no":
            Line()
            print("Goodbye")
            Line()
            exit()
        else:
            Line()
            print("Please type Yes or No")
            Line()
