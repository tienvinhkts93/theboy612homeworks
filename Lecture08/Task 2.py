class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self,change_of_speed):
        self.current_speed += change_of_speed

        if self.current_speed > self.maximum_speed:
           self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
             self.current_speed = 0

car1 = Car("ABC-123", 142)
car1.accelerate(30)
print(f"Current speed of Car is: {car1.current_speed} km/h")

car1.accelerate(70)
print(f"Current speed of Car is: {car1.current_speed} km/h")

car1.accelerate(50)
print(f"Current speed of Car is: {car1.current_speed} km/h")

car1.accelerate(-200)
print(f"final speed is: {car1.current_speed} km/h")

