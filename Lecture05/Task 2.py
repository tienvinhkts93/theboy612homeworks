user_input = input("Enter the number that you want ( or enter to quit): ")
cart = []

while user_input != "":
    choice = int(user_input)
    if choice >= 0:
        cart.append(choice)
        print (f"Here is the number in your list: {cart}")
    elif choice < 0:
        print("Please enter a number greater than 0")
    user_input = input("Enter the number that you want ( or enter to quit): ")

if len(cart) == 0:
    print ("No numbers in your list")
else:
    cart.sort(reverse=True)
    sorted_cart = cart[:5]
    print(sorted_cart)









