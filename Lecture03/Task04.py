Year = int(input("Please enter the year: "))

if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    print(f"{Year} is a leap year !")

else:
    print(f"{Year} is a common year !")