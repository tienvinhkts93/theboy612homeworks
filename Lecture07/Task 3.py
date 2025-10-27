def sum_numbers(numbers):
    total = sum(numbers)
    return total

cart = []

input_user = int(input("Enter a positive number (0 to quit): "))
while input_user > 0:
    cart.append(input_user)
    input_user = int(input("Enter a positive number (0 to quit): "))
    if input_user == 0:
        break

print(f"Total number is {sum_numbers(cart)}")

