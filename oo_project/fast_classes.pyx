#This file redefines a 2D Vector and Particle classes using some tricks to make the code run faster
#You may recognise some of the syntax but do not worry if there are things you don't understand
#For these classes to work, you must have Cython installed on your system

from cpython cimport bool

# fast Vector class similar to base Python class but defines the types explicitly
# allowing the compiler to optimise the code
cdef class Vector: 
    cdef float x, y
    def __init__(self, float x, float y):
        self.x = x
        self.y = y
    
    def __add__(self,other):
        return (Vector(self.x+other.x,self.y+other.y))

    def __sub__(self,other):
        return (Vector(self.x-other.x,self.y-other.y))

    def __mul__(self,number):
        return Vector(self.x*number,self.y*number)

    def __rmul__(self,number):
        return Vector(self.x*number,self.y*number)
   
    def __truediv__(self,number):
        return Vector(self.x/number,self.y/number)

    def __repr__(self):
        return '{x} {y}'.format(x=self.x, y=self.y)

    cpdef float dot(self,Vector other):
        return self.x*other.x + self.y*other.y
   
    #faster to use properties than to enable public access    
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

    # could be used within a fast Particle class
    cdef Vector fast_subtract(self, Vector other):
        return Vector(self.x-other.x,self.y-other.y)
            
    cpdef float norm(self):
        return (self.x**2+self.y**2)**0.5

    # so that our fast vector can be pickled
    def __reduce__(self):
        return (rebuild_vec, (self.x,self.y))
    
#enables pickling
def rebuild_vec(x,y):
    return Vector(x,y)  

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
    
    property radius:
        def __get__(self):
            return self.radius
        def __set__(self,r):
            self.radius=r

    property mass:
        def __get__(self):
            return self.mass
        def __set__(self,m):
            self.mass=m

    cpdef Vector velocity(self):
        return self.momentum/self.mass

    cpdef Particle copy(self):
        return Particle(self.position, self.momentum, self.radius, self.mass)

    cpdef bool overlap(self, Particle other):
        cdef Vector displacement
        displacement = self.position.fast_subtract(other.position)

        return displacement.norm() < (self.radius + other.radius)

    #enables pickling
    def __reduce__(self):
        return (build_particle, (self.position,self.momentum,self.radius,self.mass))

#enables pickling
def build_particle(position,momentum,radius,mass):
    return Particle(position,momentum,radius,mass)
