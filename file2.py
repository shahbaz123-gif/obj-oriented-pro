class Vehicle:
    def __init__(self, max_speed, mileage):
       self.max_speed = max_speed
       self.mileage = mileage

modelX = Vehicle(240, 18)
modelY = Vehicle(250, 19)
print("Model Max Speed:",modelY.max_speed)
print("Model Max Speed:",modelX.max_speed)
print("Model Mileage:", modelX.mileage)