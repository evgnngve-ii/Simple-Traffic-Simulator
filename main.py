#Initialize the intersection
#intersection = [A,B,C,D]
intersection = [True,True,True,True]

#Define a "car" w/ waitTime (w), direction (d), canGo(g)
class Car:
    def __init__(self,waitTime,direction,canGo):
        self.waitTime = waitTime
        self.direction = direction
        self.canGo = canGo

#Initialize our cars
#noD and noG are just empty placeholders
carOne = Car(0,"noD","noG")
carTwo = Car(0,"noD","noG")
carThree = Car(0,"noD","noG")
carFour = Car(0,"noD","noG")

#Put cars into array for easier programming
#0,1,2,3
carLot = [carOne,carTwo,carThree,carFour]

for x in range(4):
    print(carLot[x].waitTime)

for x in range(4):
    print(carLot[x].direction)

for x in range(4):
    print(carLot[x].canGo)




