User_Sex = input("Enter your gender? ").lower()

Value_hemoglobin = int(input("Enter your hemoglobin level (g/L)? "))

#For adult females:
if User_Sex == "female":
    if 117 <= Value_hemoglobin <= 155:
        print("Your hemoglobin level (g/L) is normal.")
    elif Value_hemoglobin < 117:
        print("Your hemoglobin level (g/L) is low.")
    else:
        print("Your hemoglobin level (g/L) is high.")

#For adult males:
elif User_Sex == "male":
    if 134 <= Value_hemoglobin <= 167:
        print("Your hemoglobin level (g/L) is normal.")
    elif Value_hemoglobin < 134:
        print("Your hemoglobin level (g/L) is low.")
    else:
        print("Your hemoglobin level (g/L) is high.")