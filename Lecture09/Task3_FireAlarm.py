from Task1_Elevator import Elevator
from Task2_Building import Building


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

#class Building
Building.fire_alarm = fire_alarm

# Test
building = Building(0, 10, 3)
building.run_elevator(1, 5)
building.run_elevator(2, 8)
building.fire_alarm()