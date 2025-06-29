import random

random_number = random.randint(1,10)

while(True):
    guessed_number = int(input("Guess a number: "))
    if(guessed_number == random_number):
        print("Correct guess")
        break
    elif((random_number-guessed_number)>5):
        print("Your guess is too low")
    elif (( random_number-guessed_number) < (-4) ):
        print("Your guess is too high")