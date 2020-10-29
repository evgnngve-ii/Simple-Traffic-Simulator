import random
from queue import PriorityQueue

# intersection = [A,B,C,D]
intersection = [0, 0, 0, 0]

# Probability fine tuners for: 0 <= N <= x and x < N <= x+y and x+y <= 1
x = 0.33333333333333
y = 0.33333333333333

# Counters
intervalLimit = 10  # Amount of intervals in a simulation run
totalNumberOfCarsPassed = 0  # Amount of cars that passed in the entire run

# Tracker: Each list has their index correspond to each of the other list; Use these lists to build the data set
carIndex = []
waitTime = []
recordedInterval = []


################################ FUNCTIONS #############################

# Prints the current state of the cars at the intersection
def carLotState():
    for car in carLot:
        print("Car " + str(car.carIndex) + " W:" + str(car.waitTime) + " d:" + car.direction + " g:" + car.carPassed)


# Checks if the car going Left is at position c1,c2,c3,c4 and if it can go
def canTurnLeft(car):  # 2a ...(Can car at current position go, given intersection state?)
    if car.carIndex == 0:  # If car is C1 going left #0 == 0:
        if intersection[0] == intersection[1] == intersection[3] == 0:
            # print("Car C1 sucessfully turned Left")
            return True  # just set the field to True
    if car.carIndex == 1:  # If car is C2 going left
        if intersection[1] == intersection[2] == intersection[3] == 0:
            return True
    if car.carIndex == 2:  # If car is C3 going left
        if intersection[0] == intersection[2] == intersection[3] == 0:
            return True
    if car.carIndex == 3:  # If car is C4 going left
        if intersection[0] == intersection[1] == intersection[2] == 0:
            return True


# Checks if the car going Right is at position c1,c2,c3,c4 and if it can go
def canTurnRight(car):  # 2b
    if car.carIndex == 0:  # If car is C1 going right
        if intersection[3] == 0:
            return True
    if car.carIndex == 1:  # If car is C2 going right
        if intersection[2] == 0:
            return True
    if car.carIndex == 2:  # If car is C3 going right
        if intersection[0] == 0:
            return True
    if car.carIndex == 3:  # If car is C4 going right
        if intersection[1] == 0:
            return True


# Checks if the car going Straight is at position c1,c2,c3,c4 and if it can go
def canTurnStraight(car):  # 2c
    if car.carIndex == 0:  # If car is C1 going straight
        if intersection[1] == intersection[3] == 0:
            return True
    if car.carIndex == 1:  # If car is C2 going straight
        if intersection[2] == intersection[3] == 0:
            return True
    if car.carIndex == 2:  # If car is C3 going straight
        if intersection[0] == intersection[2] == 0:
            return True
    if car.carIndex == 3:  # If car is C4 going straight
        if intersection[0] == intersection[1] == 0:
            return True


# Checks the direction of the car, and will use a helper function to determine if the car can pass, from it's position.
# Returns false other wise
def checkDirection(car):  # (1) If we are going L (or S or R)...
    if car.direction == 'L':
        # print("Car# " + str(car.carIndex) + " going LEFT")
        # OK, we return True but dont do anything with it
        return canTurnLeft(car)

    if car.direction == 'S':
        # print("Car# " + str(car.carIndex) + " going STRAIGHT")
        return canTurnStraight(car)

    if car.direction == 'R':
        # print("Car# " + str(car.carIndex) + " going RIGHT")
        return canTurnRight(car)


# Update intersection occupied by a car going left (or right or straight) by setting them to 1's
def updateLeft(carPassed):
    if carPassed.carIndex == 0:  # If car is C1 going left #0 == 0:
        intersection[0] = 1
        intersection[1] = 1
        intersection[3] = 1
    if carPassed.carIndex == 1:  # If car is C2 going left
        intersection[1] = 1
        intersection[2] = 1
        intersection[3] = 1
    if carPassed.carIndex == 2:  # If car is C3 going left
        intersection[0] = 1
        intersection[2] = 1
        intersection[3] = 1
    if carPassed.carIndex == 3:  # If car is C4 going left
        intersection[0] = 1
        intersection[1] = 1
        intersection[2] = 1


def updateRight(carPassed):
    if carPassed.carIndex == 0:  # If car is C1 going right
        intersection[3] == 1
    if carPassed.carIndex == 1:  # If car is C2 going right
        intersection[2] == 1
    if carPassed.carIndex == 2:  # If car is C3 going right
        intersection[0] == 1
    if carPassed.carIndex == 3:  # If car is C4 going right
        intersection[1] == 1


def updateStraight(carPassed):
    if carPassed.carIndex == 0:  # car C1
        intersection[1] = 1
        intersection[3] = 1
    if carPassed.carIndex == 1:  # car c2
        intersection[2] = 1
        intersection[3] = 1
    if carPassed.carIndex == 2:  # car C3
        intersection[0] = 1
        intersection[2] = 1
    if carPassed.carIndex == 3:  # car C4
        intersection[0] = 1
        intersection[1] = 1


# Works similar to checkDirection, except we want to update the space taken up by an intersection in an interval
def updateIntersection(carPassed):
    if carPassed.direction == 'L':
        updateLeft(carPassed)
    if carPassed.direction == 'S':
        updateStraight(carPassed)
    if carPassed.direction == 'R':
        updateRight(carPassed)


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


# Will return a priority que with ordered cars in the current state
# Do ordering of cars     #Stretch Goal: Implement the more robust way of the ordering

#Calculate next order
# ToDo
# Essentially, we have
# Remove all the stuff inside.
# Really, just need to sort based off of the car's wait time and indexing (car 1 prioritizes over car 2, even if they both
#   have a wait time of two. So to account for this we can just add 1/i, where i is the index from car i)
def calculateNextOrder():

    #Can just ignore and delete all this code; plan to rewrite it; simple array ordering, just need to calculate the
        #order of the cars by their wait time and index position.

 #   carOrdering = PriorityQueue(4)
 #   for i in range(len(carLot)):
 #       index = i;
 #       adjustIndex = -(carLot[i].carIndex)  # make index value so that we can prioritize lower indexes
 #       carRank = (carLot[i].waitTime + adjustIndex)  # Calculate the rank of the given car; Wait time + lower index
 #       # print("CAR#"+str(i)+" has rank of " + str(carRank))
 #       # Multiply by -1 so that priority queue puts the "negative-most" values at top



#        print("Rank: " + str(-carRank) + ", Assigned index: " + str(i))
#        carOrdering.put(-carRank, str(index))  # More wait time => more negative => More priority
#   return carOrdering
    pass


# Define a "car" w/ waitTime (w), direction (d), canGo(g)
class Car:
    def __init__(self, waitTime, direction, carPassed, carIndex, totalPasses):
        self.waitTime = waitTime
        self.direction = direction
        self.carPassed = carPassed
        self.carIndex = carIndex  # this one is to just id the car
        self.totalPasses = totalPasses  # Count amount of times crossed intersection for entirety of run


##################INITIALIZE PHASE:################################################
# intersection intialized at beggining of program

# Initialize our cars
# D is just an empty placeholder
carOne = Car(0, 'D', False, 0, 0)
carTwo = Car(0, 'D', False, 1, 0)
carThree = Car(0, 'D', False, 2, 0)
carFour = Car(0, 'D', False, 3, 0)

# Store cars into array for easier programming
#           0,      1,       2,         3
carLot = [carOne, carTwo, carThree, carFour]

# Assign an initial direction for each car
for i in range(len(carLot)):
    carLot[i].direction = assignDirection(random.random())

carOrdering = calculateNextOrder()


# carLotState(carLot)

##############SIMULATION PHASE###################################################
# Take note, index is also our position; AKA c1 on bottom, c2 on left, c3 on top, c4 on right.

# print("On an empty intersection, car 1 going left : " + didPass)


# Run 10 times A SIMULATION GOES HERE

def processACycle(carOrdering, intervalTracker):
    test = 1
    while not carOrdering.empty():  # While still cars in the order/heap

        next_car_index = carOrdering.get()  # Get the nth car
        # print(str(next_car_index))
        next_car = carLot[next_car_index] ##bug here......

        if checkDirection(next_car):  # If car is able to pass
            # store data
            carIndex.append(next_car.carIndex + 1)  # Store car ID; Add 1 for easier use outside of program
            waitTime.append(next_car.waitTime)
            recordedInterval.append(intervalTracker)
            next_car.totalPasses = next_car.totalPasses + 1

            # Update data
            next_car.carPassed = True  # set g to true
            next_car.waitTime = 0  # reset wait time to 0 for next iteration
            next_car.direction = assignDirection(random.random())  # Assign a new direction for next iteration

            # If car passed, update the intersection state
            # If the car passed, all tiles necessary are zero, thus, we just change corresponding tiles to 1
            updateIntersection(next_car)

        else:
            next_car.waitTime = next_car.waitTime + 1
            next_car.carPassed = False


intervalTracker = 1

for x in range(intervalLimit):  # run the simulation interval limit = 10 times...
    processACycle(carOrdering, intervalTracker)
    carOrdering = calculateNextOrder()
    intervalTracker = intervalTracker + 1

print("FINSIHED")
