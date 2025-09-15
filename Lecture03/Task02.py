User = input("What is your cabin class? ").upper()
if User == "LUX":
    print("Upper-deck cabin with a balcony")
elif User == "A":
    print("Cabin above the car deck with a window")
elif User == "B":
    print("Windowless cabin above the car deck")
elif User == "C":
    print("Windowless cabin below the car deck")
else:
    print("Invalid cabin class")
