
Guess = 0
import random
FromComputer = random.randint(1, 10)

while Guess != FromComputer:
    Guess = int(input("Guess the number (from 1 to 10): "))
    if Guess < FromComputer:
        print ("too low")
    elif Guess > FromComputer:
        print ("too high")
    else:
        print ("right, the number is ", FromComputer)
