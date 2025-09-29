user_input = input("Enter the number that you want ( or enter to quit): ")
cart = []

while user_input != "":
    choice = int(user_input)
    if choice >= 0:
        cart.append(choice)
        print(f"{cart} added to the list")
    else:
        print("No cart has been added to the list")
    user_input = input("Enter the number that you want ( or enter to quit): ")

if len(cart) == 0:
        print("No number has been added to the list")
else:
    for i in cart:
        if i < 2:
            print(f"{i} is NOT a prime number")
        else:
            divisor_count = 0
            for j in range(2, i):
                if i % j == 0:
                    divisor_count = divisor_count + 1
            if divisor_count == 0:
                print(f"{i} is a prime number")
            else:
                print(f"{i} is NOT a prime number")







