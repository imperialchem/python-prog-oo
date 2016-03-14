
from oo_functions import animate_trajectory
from my_simulation import Vector,Particle,Simulation

def test_box():
    box_length = 100
    no_steps = 300

    p1 = Particle(position = Vector(10,50), momentum=Vector(-1,0),radius=1,mass=1)
    p2 = Particle(position = Vector(50,90), momentum=Vector(0,1) ,radius=1,mass=1)
    p3 = Particle(position = Vector(50,10), momentum=Vector(0,-1),radius=1,mass=1)
    p4 = Particle(position = Vector(90,50), momentum=Vector(1,0) ,radius=1,mass=1)

    test_case = [p1,p2,p3,p4]
    s=Simulation(particles=test_case,box_length=100,dt=0.05)

    for i in range(500):
        s.step()
    animate_trajectory(s,loop=True)

def test_1d_collision():
    box_length = 100
    no_steps = 300

    p1 = Particle(position = Vector(10,10), momentum=Vector(1,0),radius=1,mass=1)
    p2 = Particle(position = Vector(20,10), momentum=Vector(0,0) ,radius=1,mass=1)
    
    test_case = [p1,p2]
    s=Simulation(particles=test_case,box_length=100,dt=0.05)

    for i in range(500):
        s.step()
    animate_trajectory(s,loop=True)


