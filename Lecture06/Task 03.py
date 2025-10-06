Airport_cart = {}
while True:
    print("Select one of the options:\n"
          "1-ENTER A NEW AIRPORT\n"
          "2-FETCH AIRPORT INFO\n"
          "3-QUIT THE PROGRAM\n")
    user_input = int(input("Please enter your choice (1, 2, 3): "))
    if user_input == 1:
        icao_code = input("Enter ICAO code: ").upper()
        if icao_code in Airport_cart:
            print(f"Airport '{icao_code}' already exists.")
        else:
            name = input("Enter airport name: ")
            Airport_cart[icao_code] = name
            print("Airport saved!")
    elif user_input == 2:
        icao_code = input("Enter ICAO code to fetch: ").upper()
        Airport_name = Airport_cart.get(icao_code)
        if icao_code in Airport_cart:
            print(f"Airport Name: {Airport_cart[icao_code]}")
        else:
            print(f"ICAO code '{icao_code}' not found.")
    elif user_input == 3:
        print("Goodbye!")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")