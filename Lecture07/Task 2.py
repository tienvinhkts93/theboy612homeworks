def convert_gallon_liters(gallon):
    formula = gallon * 3.78541
    return formula

def run_convert_program():
    while True:
        input_user = float(input("Enter a number of volume in gallons: "))
        if input_user >= 0:
            print(f"The value when converted to liters is: {convert_gallon_liters(input_user):.2f}")
        else:
            print("Enter a positive number")

run_convert_program()


