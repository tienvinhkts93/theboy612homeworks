# Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

#A new elevator is always at the bottom floor
        self.current_floor = bottom_floor

#The methods run the elevator one floor up or down and tell what floor the elevator is after each move
# methods floor_down
    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"We are in {self.current_floor} floor")

# methods floor_up
    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"We are in {self.current_floor} floor")


# methods go_to_floor
    def go_to_floor(self,target_floor):
        while self.current_floor != target_floor:
            if target_floor > self.current_floor:
                self.floor_up()
            else:
                self.floor_down()

# Create elevator with floors from 1 to 10
h = Elevator(1, 10)
print(h.current_floor)


# Move to another floor
h.go_to_floor(9)
print(h.current_floor)

# Move back to the bottom
h.go_to_floor(3)