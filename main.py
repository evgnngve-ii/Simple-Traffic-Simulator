import random
from queue import PriorityQueue

# Probability fine tuners for: 0 <= N <= x and x < N <= x+y and x+y <= 1
x = 0.33333333333333
y = 0.33333333333333

# Counters
intervalLimit = 10  # Amount of intervals in a simulation run
totalNumberOfCarsPassed = 0  # Amount of cars that passed in the entire run
currentIntervalNumber = 1 #What current turn we are on


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
# Initialize the intersection
# intersection = [A,B,C,D]
intersection = [True, True, True, True]

# Initialize our cars
# Y and are just empty placeholders
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

# Given a car Ci, if it can pass through the intersect, with the given intent and current intersect state, returns T
# Returns false other wise
def checkIntersection(car):

    if car.direction == 'L':
        print("Car# " + str(car.carIndex) + " going LEFT")

    if car.direction == 'S':
        print("Car# " + str(car.carIndex) + " going STRAIGHT")

    if car.direction == 'R':
        print("Car# " + str(car.carIndex) + " going RIGHT")


#Run 10 times
def intervalRun(carOrdering): # ToDo
    pass

for x in range(intervalLimit): #ToDo
    intervalRun(carOrdering)

carLotState()
for i in range(len(carLot)):
    checkIntersection(carLot[i])




###############DEBUGGING STUFF################
# print("Directions assigned! The assigned directions are")
# for x in range(4):
#    print("Car # " + str(x) + " has direction " + carLot[x].direction)
# print (str(xPy))
