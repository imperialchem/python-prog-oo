from cpython cimport bool

cdef class Vector: 
    cdef float x, y
    def __init__(self, float x, float y):
        self.x = x
        self.y = y
    
    def __add__(self,other):
        return (Vector(self.x+other.x,self.y+other.y))

    def __sub__(self,other):
        return (Vector(self.x-other.x,self.y-other.y))

    def __mul__(self,other):
        return Vector(self.x*other,self.y*other)
    
    def __truediv__(self,other):
        return Vector(self.x/other,self.y/other)

    def __pow__(self,other, ignore):
        return Vector(self.x**other,self.y**other)
    
    def __repr__(self):
        return '{x} {y}'.format(x=self.x, y=self.y)

    cpdef float dot(self,other):
        cdef float d
        d = self.x*other.x + self.y*other.y
        return d
    
    property x:
        def __get__(self):
            return self.x
        def __set__(self,x):
            self.x = x
    
    property y:
        def __get__(self):
            return self.y
        def __set__(self, y):
            self.y = y
            
    cpdef float norm(self):
        cdef float l
        l = self.dot(self)**0.5
        return l

cdef class Particle:
    cdef Vector position, momentum
    cdef float radius, mass
    
    def __init__(self, Vector position not None, Vector momentum not None, float radius, float mass):

        self.position = position
        self.momentum = momentum
        self.radius = radius
        self.mass = mass

    property position:
        def __get__(self):
            return self.position
        def __set__(self,p):
            self.position = p
 
    property momentum:
        def __get__(self):
            return self.momentum
        def __set__(self,m):
            self.momentum=m

    cpdef Vector velocity(self):
        cdef Vector v
        v = self.momentum/self.mass
        return v

    cpdef bool overlap(self, Particle other):
        cdef Vector displacement
        displacement = self.position - other.position
        return displacement.norm() < (self.radius + other.radius)

