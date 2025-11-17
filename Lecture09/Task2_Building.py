from Task1_Elevator import Elevator

#Creating a Building class
#The initializer parameters for the class are the numbers of the bottom and top floors and the number of elevators in the building.
class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.number_of_elevators = number_of_elevators

#The list of elevators is stored as a property of the building.
        self.elevators = []

#When a building created, the building creates the required number of elevators
        for i in range(number_of_elevators):
            elevator_id = i + 1
            print("Creating elevator number:", elevator_id)
            new_elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(new_elevator)

        print("All elevators have been created.")
        print("-------------------------------------")

#accepts the number of the elevator and the destination floor as its parameters.
    def run_elevator(self, elevator_number, target_floor):
        print("\n=====================================")
        print("The system is preparing to run elevator number:", elevator_number)

        # Getting the value index of elevator
        elevator_index = elevator_number - 1
        selected_elevator = self.elevators[elevator_index]

        # Moving selected_elevator to target_floor
        print(f"Now using elevator number {elevator_number}.")
        selected_elevator.go_to_floor(target_floor)

#Task3
#Not receive any parameters and moves all elevators to the bottom floor
    def fire_alarm(self):
        print("\n FIRE ALARMING! ALL ELEVATORS MOVE TO THE BOTTOM FLOOR!")
        for i in range(len(self.elevators)):   #Check list
            elevator_number = i + 1            #Assign value in list
            elevator_selection = self.elevators[i]       #Assessing the required value into list
            print(f" Moving the elevator number {elevator_number} to the bottom floor {self.bottom_floor}...")
            elevator_selection.go_to_floor(self.bottom_floor)
        print("ALL ELEVATORS ALREADY MOVED AT BOTTOM FLOOR\n")


# -------- MAIN PROGRAM --------
print("\n=== TASK 2 TEST ===")
building = Building(1, 10, 2)   # 2 thang máy

# Elevator_number1 go to 8th floor
building.run_elevator(1, 8)

# Elevator_number3 go to 3rd floor
building.run_elevator(2, 3)