import random
def random_dice_roll():
    return random.randint(1, 6)

def roll_dice_game():
    result = 0
    roll_count = 0

    while result !=6:
        roll_count += 1
        result = random_dice_roll()
        print(f"Roll count is {roll_count} and result is {result}")

    print(f"You win! Roll count is {roll_count} and result is 6")

roll_dice_game()

