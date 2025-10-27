def even(numbers):
    cart_even = []
    for a in numbers:
        if a % 2 == 0:
            cart_even.append(a)
    return cart_even

cart_original = []

input_user = int(input("Enter a positive number (0 to quit): "))
while input_user > 0 :
    cart_original.append(input_user)
    input_user = int(input("Enter a positive number (0 to quit): "))
    if input_user == 0:
        break

cart_even = even(cart_original)

print(f"List number is {cart_original}")
print(f"List even number is {cart_even}")

