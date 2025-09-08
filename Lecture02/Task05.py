A_talents = float (input("Enter talents : "))
B_pounds = float (input("Enter pounds : "))
C_lots = float (input("Enter lots : "))

total_lots = (A_talents * 20 * 32) + (B_pounds * 32) + C_lots
total_grams = total_lots * 13.3

ChangeUnit_kilograms = int(total_grams * 0.001 )
ChangeUnit_grams = float (total_grams % 1000)

print(f"\nThe weight is modern unit : {ChangeUnit_kilograms} and {ChangeUnit_grams:.2f}")
