class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def drive(self,hours):
        self.travelled_distance = self.current_speed * hours

    def print_information(self):
        print(f"Registration Number: {self.registration_number}")
        print(f"Maximum Speed: {self.maximum_speed}")

class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity

    def print_information(self):
        super().print_information()
        print(f"Battery capacity of the car: {self.battery_capacity} in kilowatt-hours")


class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, volume):
        super().__init__(registration_number, maximum_speed)
        self.volume = volume

    def print_information(self):
        super().print_information()
        print(f"Volume of the tank: {self.volume} in liters")


car1 = ElectricCar("ABC-15",180, 52.5)
car2 = GasolineCar("ACD-123", 165, 32.3)

car1.current_speed = 120
car2.current_speed = 130

car1.drive(3)
car2.drive(3)

car1.print_information()
print(f"Travelled distance: {car1.travelled_distance} km\n")

car2.print_information()
print(f"Travelled distance: {car2.travelled_distance} km")
