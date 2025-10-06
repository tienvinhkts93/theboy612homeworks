months_in_year = ("January","February","March","April","May","June","July","August","September","October","November","December")
month_number = int(input("Enter the month number (1-12): "))
month = months_in_year[month_number-1]
weather_dictionary = {"January": "Winter", "February": "Winter"
    ,"March":"Spring","April":"Spring","May":"Spring"
    ,"June":"Summer","July":"Summer","August":"Summer"
    ,"September":"Autumn","October":"Autumn","November":"Autumn","December": "Winter"}
print(f"month number : {month_number} is {month} in {weather_dictionary[month]}")