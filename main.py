import random

# Probability fine tuners for: 0 <= N <= x and x < N <= x+y and x+y <= 1
x = 0.33333333333333333333
y = 0.33333333333333333333
xPy = x + y


# Given a Car object c, we assign it a direction based off of a probability
# Lot number 0 = carOne, lotNumber 1 = carTwo, etc
# note to self; Python is pass by reference
def assignDirection(car):
    # print("Car#: " + str(car.carNumber))
    # print(random.random())

    # This is a random number between [0,1). Use it to determine direction
    n = random.random()  # this version of RNG excludes 1 as a possibility. Is that important?


    # if 0 <= n <= 100:
    if 0 <= n <= x:

        car.direction = 'L'
        print(str(car.carNumber) + " had random number: " + str(n) + " and direction " + car.direction)
        print(0 <= n <= x)
    elif x < n <= xPy:
        car.direction = 'S'
        print(str(car.carNumber) + " had random number: " + str(n) + " and direction " + car.direction)
        print(x < n <= xPy)
    elif xPy < n <= 1:
        car.direction = 'R'
        print(str(car.carNumber) + " had random number: " + str(n) + " and direction " + car.direction)
        print(xPy < n <= 1)
    else:
        print("ERROR: n = " + str(n) + " out of bounds?")


# Define a "car" w/ waitTime (w), direction (d), canGo(g)
class Car:
    def __init__(self, waitTime, direction, canGo, carNumber):
        self.waitTime = waitTime
        self.direction = direction
        self.canGo = canGo
        self.carNumber = carNumber  # this one is to just id the car


# Initialize our cars<--------------
# Y and are just empty placeholders
carOne = Car(0, 'D', 'G', 0)
carTwo = Car(0, 'D', 'G', 1)
carThree = Car(0, 'D', 'G', 2)
carFour = Car(0, 'D', 'G', 3)

# Put cars into array for easier programming
# 0,1,2,3
carLot = [carOne, carTwo, carThree, carFour]

# Initialize the intersection
# intersection = [A,B,C,D]
intersection = [True, True, True, True]

# Assign an initial direction for each car
for x in range(4):
    assignDirection(carLot[x])

print("Directions assigned! The assigned directions are")

for x in range(4):
    print("Car # " + str(x) + " has direction " + carLot[x].direction)

#print (str(xPy))
