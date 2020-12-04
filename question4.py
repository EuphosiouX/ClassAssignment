class Shape:
    def __init__(self, color:"red", **kwargs):
        self.color = str(color)

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def __str__(self):
        return ("Shape(color={})".format(self.color))

class Circle(Shape):
    def __init__(self, radius:1.0, color):
        self.radius = float(radius)
        super().__init__(color)
    
    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius 
 
    def __str__(self):
        return ("Circle({}, radius={})".format(super().__str__(),self.radius))

    def get_area(self):
        return (self.radius**2*3.14)

class Cylinder(Circle):
    def __init__(self, heigth:1.0, radius, color):
        self.heigth = float(heigth)
        super().__init__(radius, color)
    
    def getHeigth(self):
        return self.heigth

    def setHeigth(self, heigth):
        self.heigth = heigth 
 
    def __str__(self):
        return ("Cylinder({},heigth={})".format(super().__str__(),self.heigth))   
    
    def get_area(self):
        return (super().get_area()*2 + (self.radius*2*3.14*self.heigth))

    def  get_volume(self):
        return (super().get_area()*self.heigth)

class Rectangle(Shape):
    def __init__(self, length:1.0, width:1.0, color):
        self.length = float(length)
        self.width = float(width)
        super().__init__(color) 
    
    def getLength(self):
        return self.length

    def setLength(self, length):
        self.length = length 

    def getWidth(self, width):
        return self.width

    def setWidth(self, width):
        self.width = width 

    def __str__(self):
        return 'Rectangle({}, length={}, width={})'.format(super().__str__(), self.length, self.width)
 
    def get_area(self):
        return (self.width*self.length)
 
class Square(Rectangle):
    def __init__(self, side, color):
        super().__init__(side, side, color)

    def __str__(self):
        return 'Square({})'.format(super().__str__())
   
s1 = Shape('orange')
c1 = Circle(1.2, color='orange')
r1 = Rectangle(1.2, 3.4, color='orange')
sq1 = Square(5.6, color='blue')

assert s1.color == 'orange'
assert str(s1) == 'Shape(color=orange)'
assert c1.get_area() == 4.5216
assert c1.color== 'orange'
assert c1.radius== 1.2
assert str(c1) == 'Circle(Shape(color=orange), radius=1.2)'
assert r1.get_area()==4.08
assert r1.color=='orange'
assert r1.length==1.2
assert r1.width==3.4
assert str(r1)=='Rectangle(Shape(color=orange), length=1.2, width=3.4)'
assert sq1.get_area()==31.359999999999996
assert sq1.color =='blue'
assert sq1.length==5.6
assert sq1.width ==5.6
assert str(sq1)=='Square(Rectangle(Shape(color=blue), length=5.6, width=5.6))'
