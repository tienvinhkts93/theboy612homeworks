user_input = input("Enter the names (or Enter to quit): ")
cart = set()
while user_input != "":
    if user_input in cart:
        print(f"{user_input} is existing game")
    else:
        print(f"{user_input} is new name")
        cart.add(user_input)
    user_input = input("Enter the names (or Enter to quit): ")

for user_input in cart:
    print(user_input)