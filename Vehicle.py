class Vehicle:

    def __init__(self, brand, color, speed):
        
        self.brand = brand
        self.color = color
        self.speed = speed

myVehicle = Vehicle('BMW', 'red', '320')

print(' The speed of the vehicle', myVehicle.speed,' and the color is', myVehicle.color)