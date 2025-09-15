age = int(input("Enter age: "))
if 15 <= age < 18:
    weight = float(input("Enter weight (kg): "))
elif age >=18:
    print("The medicine can be used.")
elif (age >= 15 and weight >= 55):
    print("The medicine can be used.")
else:
    print("You cant use the medicine.")