class Vehicle: #initiate parent class
  def start_trip(self): #defines start stip method
    vehicle.move()  #makes vehicle move

class Car(Vehicle):  #defines class car
  def move(self):    #makes car drive
    print("The car drives on the road.")

class Boat(Vehicle):  #defines class boat
  def move(self):     #makes boat sail
    print("The boat sails on the water.")

class Drone(Vehicle): #defines class drone
  def move(self):     #makes drone fly
    print("The drone flies in the sky.")

#initiates all objects
v1 = Car()
v2 = Boat()
v3 = Drone()

#puts all objects in one list
vehicles = [v1,v2,v3]

#makes all objects move
for i in range(len(vehicles)):
  vehicles[i].move()
  
