class Object:
    pass

class X (Object):
    pass

class Y (Object):
    pass

class Z (Object):
    pass

class A (X,Y):
    pass

class B (Y,Z):
    pass

class M (A,B,Z):
    pass