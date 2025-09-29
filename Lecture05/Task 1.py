import random

while True:
    choice = int(input("How many dice do you want? "))
    if choice == 0:
        print ("Bye Bye! ")
    elif choice > 0:
        dice = []
        for i in range(choice):
            dice.append(random.randint(1, 6))
            print ("Dice: ", dice)
            print("Sum: ", sum(dice))
    else:
        print("I can't do that!")





