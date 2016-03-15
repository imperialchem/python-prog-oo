class Vector():
    def __init__(self, i1,i2):
        self.x = i1
        self.y = i2

    def __add__(self,other):
        return (Vector(self.x+other.x,self.y+other.y))

    def __sub__(self,other):
        return (Vector(self.x-other.x,self.y-other.y))

    def __mul__(self,other):
        return Vector(self.x*other,self.y*other)

    def __truediv__(self,other):
        return Vector(self.x/other,self.y/other)

    def __pow__(self,other):
        return Vector(self.x**other,self.y**other)

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
