smallest = 0
largest = 0
User_input = input("Give me a number (or press `stop` to quit): ")

while User_input != "stop":
    numbers = int(User_input)
    if smallest == 0 or numbers < smallest:
        smallest = numbers
    if largest == 0 or numbers > largest:
        largest = numbers
    User_input = input("Give me a number (or press `stop` to quit): ")

if User_input == "stop":
    print("Smallest:", smallest)
    print("Largest:", largest)





