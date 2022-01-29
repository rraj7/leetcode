#Create an elevator system: 
# Functionalities: 
#     1. Store the state => Still / going up /going down 
#     2. Capacity => Total number of people occupying at one time vs Total Capacity
#     3. Floor - Current number of floor vs Total floors 
#     4. Health => Broken/Functional 

# Operator => Functionalities 

class Elevator:
    elevator_id
    max_capacity = 10
    current_capacity
    current_state #0 - still, 1: going up , 2: going down
    current_floor

    #Constructor to initialize the elevator system 
    def __init__(self,elevator_id, current_capacity, current_state):
        self.current_state = 0
        self.current_capacity = 0

    def choseFloor(self,current_floor):
        while (this.current_capacity<= this.max_capacity):
            




class Building: 
    total_floor = 100 
    total_elevators = 5

    def selectElevator(self,elevator_id ):
        print("You're in no: "+elevator_id+"elevator")