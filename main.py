import random
from queue import PriorityQueue

# Probability fine tuners for: 0 <= N <= x and x < N <= x+y and x+y <= 1
x = 0.33333333333333
y = 0.33333333333333

# Counters
intervalLimit = 10  # Amount of intervals in a simulation run
totalNumberOfCarsPassed = 0  # Amount of cars that passed in the entire run
currentIntervalNumber = 1  # What current turn we are on


################################ FUNCTIONS #############################

# Prints the current state of the cars at the intersection
def carLotState():
    for car in carLot:
        print("Car " + str(car.carIndex) + " W:" + str(car.waitTime) + " d:" + car.direction + " g:" + car.canGo)


# Given a random number, deduce the direction based off our current x,y parameters.
def assignDirection(n):
    d = 'D'

    if n <= x:
        # print("Left turn")
        d = 'L'

    if x < n and n <= x + y:
        # print("Straight")
        d = 'S'

    if x + y < n and n <= 1:
        # print("Right turn")
        d = 'R'

    return d


# Define a "car" w/ waitTime (w), direction (d), canGo(g)
class Car:
    def __init__(self, waitTime, direction, canGo, carIndex):
        self.waitTime = waitTime
        self.direction = direction
        self.canGo = canGo
        self.carIndex = carIndex  # this one is to just id the car


##################INITIALIZE PHASE:################################################
# Initialize the intersection; 0 is that part of the road isn't occupied; 1 means it is.
# intersection = [A,B,C,D]
intersection = [0,0,0,0]

# Initialize our cars
# D and G are just empty placeholders
carOne = Car(0, 'D', 'G', 0)
carTwo = Car(0, 'D', 'G', 1)
carThree = Car(0, 'D', 'G', 2)
carFour = Car(0, 'D', 'G', 3)

# Store cars into array for easier programming
#           0,      1,       2,         3
carLot = [carOne, carTwo, carThree, carFour]

# Assign an initial direction for each car
for i in range(len(carLot)):
    carLot[i].direction = assignDirection(random.random())

# Car rank will
# Do ordering of cars     #Stretch Goal: Implement the more robust way of the ordering
#
carOrdering = PriorityQueue(4)
for i in range(len(carLot)):
    adjustIndex = -(carLot[i].carIndex)  # make index value so that we can prioritize lower indexes
    carRank = (carLot[i].waitTime + adjustIndex)  # Calculate the rank of the given car; Wait time + lower index
    # print("CAR#"+str(i)+" has rank of " + str(carRank))
    # Multiply by -1 so that priority queue puts the "negative-most" values at top
    carOrdering.put(-carRank, str(i))  # More wait time => more negative => More priority


# carLotState(carLot)

##############SIMULATION PHASE###################################################
# Take note, index is also our position; AKA c1 on bottom, c2 on left, c3 on top, c4 on right.

# Checks if the car going Left is at position c1,c2,c3,c4 and if it can go
def canTurnLeft(car):  # 2a ...(Can car at current position go, given intersection state?)
    if car.carIndex == 0:  # If car is C1 going left #0 == 0:
        if intersection[0] == 0:
            print("A is free")
            if intersection[1] == 0:
                print("B is free")
                if intersection[3] == 0:
                    print("D is free")
                    print("Car C1 sucessfully turned Left")
                    return "True" #just set the field to True
    if car.carIndex == 1:  # If car is C2 going left
        pass
    if car.carIndex == 2:  # If car is C3 going left
        pass
    if car.carIndex == 3:  # If car is C4 going left
        pass


# Checks if the car going Right is at position c1,c2,c3,c4 and if it can go
def canTurnRight(car):  # 2b
    if car.carIndex == 0:  # If car is C1 going right
        pass
    if car.carIndex == 1:  # If car is C2 going right
        pass
    if car.carIndex == 2:  # If car is C3 going right
        pass
    if car.carIndex == 3:  # If car is C4 going right
        pass


# Checks if the car going Straight is at position c1,c2,c3,c4 and if it can go
def canTurnStraight(car):  # 2c
    if car.carIndex == 0:  # If car is C1 going straight
        pass
    if car.carIndex == 1:  # If car is C2 going straight
        pass
    if car.carIndex == 2:  # If car is C3 going straight
        pass
    if car.carIndex == 3:  # If car is C4 going straight
        pass


# Checks the direction of the car, and will use a helper function to determine if the car can pass, from it's position.
# Returns false other wise
def checkDirection(car):  # (1) If we are going L (or S or R)...
    if car.direction == 'L':
        # print("Car# " + str(car.carIndex) + " going LEFT")
        #OK, we return True but dont do anything with it
        return canTurnLeft(car)

    if car.direction == 'S':
        # print("Car# " + str(car.carIndex) + " going STRAIGHT")
        return canTurnStraight(car)

    if car.direction == 'R':
        # print("Car# " + str(car.carIndex) + " going RIGHT")
        return canTurnRight(car)


#print("car 1 is going " + str(carLot[0].direction) + ". It is: " + checkDirection(carLot[0]))
TestCarC1Left = Car(0, 'L', 'G', 0)

booleanCheck = (checkDirection(TestCarC1Left))
#didPass = str(checkDirection(TestCarC1Left))

print(booleanCheck)
#print(didPass)

#print("On an empty intersection, car 1 going left : " + didPass)


# Run 10 times A SIMULATION GOES HERE
# def intervalRun(carOrdering): # ToDo
# pass

# for x in range(intervalLimit): #ToDo
#   intervalRun(carOrdering)

###############DEBUGGING STUFF################
# print("Directions assigned! The assigned directions are")
# for x in range(4):
#    print("Car # " + str(x) + " has direction " + carLot[x].direction)
# print (str(xPy))
