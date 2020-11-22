# Define a class named "Circle"
class Circle:
    # Assign "Circle" object using def__init__ function
    def __init__(self, radius:float=1.0, color:str="Red"):
        self.__radius = radius 
        self.__color = color

    # Fetch the current radius
    def getRadius(self)->float:
        return (self.__radius)

    # Change the radius
    def setRadius(self, radius:float):
        self.__radius = radius
        return ("Radius set to {}".format(radius))
    
    # Fetch the current color
    def getColor(self)->str:
        return (self.__color)
    
    # Change the color
    def setColor(self, color:str):
        self.__color = color
        return ("Color set to {}".format(color))
    
    # Print all infomation
    def __str__(self):
        return ("Circle radius: {}\nCircle color:{}".format(self.getRadius(),self.getColor()))

    # Calculate area
    def getArea(self)->float:
        return (self.getRadius()**2*3.14)

# Define a class named "Cylinder" and it is a subclass from "Circle" class
class Cylinder(Circle):
    # Assign "Circle" object using def__init__ function
    def __init__(self, height:float=1.0, radius:float=1.0, color:str="Red"):
        self.__height = height
        super().__init__(radius, color)

    # Fetch the current height
    def getHeight(self)->float:
        return (self.__height)
    
    # Change the height
    def setHeight(self, height:float):
        self.__height = height
        return ("Height set to {}".format(height))

    # Print all information
    def __str__(self):
        return ("Cylinder height: {}\nCylinder radius: {}\nCylinder color: {}".format(self.getHeight(), self.getRadius(), self.getColor()))

    # Calculate forum
    def getVolume(self)->float:
        return (self.getArea()*self.getHeight())

## UNCOMMENT THE CODE BELOW FOR TESTING THE CODE ##


# circle = Circle()
# cylinder = Cylinder()

# print(circle.getRadius())
# print(circle.setRadius(9.6))
# print(circle.getColor())
# print(circle.setColor("Green"))
# print(circle.__str__())
# print(circle.getArea(),"\n")
# print(cylinder.getHeight())
# print(cylinder.setHeight(3.7))
# print(cylinder.getRadius())
# print(cylinder.setRadius(7))
# print(cylinder.getColor())
# print(cylinder.setColor("blue"))
# print(cylinder.__str__())
# print(cylinder.getVolume())