length = float(input("Enter the the length of a zander in centimeters: "))
if length < 42:
    short = 42 - length
    print(f"Release it back into the lake. It is the {short:.2f} centimeters below the size limit")
else:
    print("Congratulation!")