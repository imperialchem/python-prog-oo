# This is the vector class we are using but we recommend you import Vector
# from oo_functions as that version has a few more advanced additions that make
# its execution considerably faster

class Vector():
    def __init__(self, i1,i2):
        self.x = i1
        self.y = i2

    def __add__(self,other):
        return (Vector(self.x+other.x,self.y+other.y))

    def __sub__(self,other):
        return (Vector(self.x-other.x,self.y-other.y))

    #multiply by a number on the left
    def __mul__(self,number):
        return Vector(self.x*number,self.y*number)

    #multiply by a number on the right
    def __rmul__(self,number):
        return Vector(self.x*number,self.y*number)

    def __truediv__(self,number):
        return Vector(self.x/number,self.y/number)

    def __repr__(self):
        return '{x} {y}'.format(x=self.x, y=self.y)

    def dot(self,other):
        return self.x*other.x + self.y*other.y

    def norm(self):
        return (self.x**2+self.y**2)**0.5

class Particle():
    def __init__(self):
        pass

class Simulation():
    def __init__(self):
        pass
