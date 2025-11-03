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

    def drive(self,hours):
        if hours > 0:
            self.travelled_distance += self.current_speed * hours
        else:
            print("Invalid input")

car1 = Car("ABC-123", 142)
car1.travelled_distance = 2000
car1.current_speed = 60
print(f"Travel distance of car is: {car1.travelled_distance} km")

car1.drive(1.5)
print(f"Travel distance of car is: {car1.travelled_distance} km")
