# LinkedIn Learning Python course by Joe Marini
# Example file for working with classes
#

class Vehicle: 
  def __init__(self, bodystyle):
    self.bodystyle = bodystyle
  
  def drive(self, speed):
    self.mode = "driving"
    self.speed = speed

class Car(Vehicle):
  def __init__(self, enginetype) :
    super().__init__("Car")
    self.wheels = 4
    self.doors = 4
    self.engine = enginetype
  
  def drive(self, speed):
    super().drive(speed)
    print("I drive my" + self.engine + " car at" + str(self.speed) + "mph")

class Motorcycle(Vehicle):
  def __init__(self, enginetype, hassidecar):
    super().__init__("Motorcycle")
    if (hassidecar): 
      self.wheels = 3
    else: 
      self.wheels = 2

    self.foors = 0 
    self.engine = enginetype

  def drive(self, speed):
    super().drive(speed)
    print("I drive my" + self.engine + " car at" + str(self.speed) + "mph")

car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)
print(car1.drive(30))
print(mc1.drive(10))
