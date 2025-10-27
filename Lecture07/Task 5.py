def price_pizza(number):
    formula = 3.14 * (number/2)**2
    return formula


input_user1 = float(input("Enter a diameter of the 1st pizza (in centimeters): "))
input_user2 = float(input("Enter a diameter of the 2nd pizza (in centimeters): "))

print(f"The 1st pizza has value money {price_pizza(input_user1):.2f} euros")
print(f"The 2nd pizza has value money {price_pizza(input_user2):.2f} euros")

if input_user1 > input_user2:
    print("The 2nd pizza is better value money than the 1st pizza.")
elif input_user1 < input_user2:
    print("The 1st pizza is better value money than the 2nd pizza.")
else:
    print("The 1st pizza is equal to the 2nd pizza in the value money.")
