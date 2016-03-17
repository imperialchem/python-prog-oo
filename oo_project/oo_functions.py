from IPython.display import display, clear_output 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
import time 
import numpy as np 
import pyximport; pyximport.install() 
from oo_fast_functions import Vector
from oo_fast_functions import Particle

def animate_trajectory(s,loop=False):    
    def update_frame(i, frame):
        if equal_size:
            x = [p.position.x for p in s.trajectory[i]]
            y = [p.position.y for p in s.trajectory[i]]
            frame.set_data([x,y])
        else:
            xy = [(p.position.x, p.position.y) for p in s.trajectory[i]]
            frame.set_offsets(xy)
        return frame,

    particle_size = s.particles[0].radius * 12
    particle_sizes = [(p.radius*12)**2 for p in s.particles]
    equal_size = len(set(particle_sizes))==1 
    no_steps = len(s.trajectory)
    
    try: 
        length = s.box_length /10
    except AttributeError:
        length = 10
    
    if not equal_size:
        length = length/1.5
        particle_sizes = [((p.radius*12)**2)/1.5**2 for p in s.particles]
        
    fig = plt.figure(figsize=(length,length))

    #plt.plot is faster than scatter but can only plot points of equal size
    if equal_size:
        frame, = plt.plot([],[],  c='b',linestyle='', marker='o',markersize=particle_size ) # initialise plot
    else:
        frame = plt.scatter([],[], s=particle_sizes ) # initialise plot

    try:
        plt.xlim(-2, s.box_length+2) # set x and y limits with a bit of extra padding
        plt.ylim(-2, s.box_length+2)
    except AttributeError:
        plt.xlim(-2, 102) # set x and y limits with a bit of extra padding
        plt.ylim(-2, 102)

    frame_ani = animation.FuncAnimation(fig, update_frame, no_steps, fargs=(frame,),
                                       interval=10, blit=True, repeat=loop)

    plt.show()



def clunky_display_frame(s):
    clear_output(wait=True)
    try:
        fig = s.fig
        ax = s.ax
        frame = s.frame
    except AttributeError:
        plt.ion()
        s.fig = plt.figure(figsize=(10,10))
        s.ax = s.fig.add_subplot(111)
        s.ax.set_xlim(-2, s.box_length+2) # set x and y limits with a bit of extra padding
        s.ax.set_ylim(-2, s.box_length+2)
        s.frame, = s.ax.plot([],[],c='b',linestyle='', marker='o',markersize=16.5)
        fig=s.fig
        ax=s.ax
        frame=s.frame
        plt.show(False)

    particle_x = [p.position.x for p in s.particles]
    particle_y = [p.position.y for p in s.particles]

    frame.set_data([particle_x,particle_y])
    #fig.canvas.draw()
    plt.show()
    display(fig)

def display_particle(p):
    plt.figure(figsize=(10,10))
    plt.plot([p.position.x],[p.position.y],marker='o',linestyle='', markersize=12)
    plt.show()

def display_trajectory(particles):
    def update_frame(i, frame):
        x=[particles[i].position.x]
        y=[particles[i].position.y]
        frame.set_data([x,y])
        return frame,

    fig = plt.figure(figsize=(10,10))
    no_steps = len(particles) 
    frame, = plt.plot([],[],marker='o',linestyle='', markersize=12)
   
    min_x,max_x = min([p.position.x for p in particles]), max([p.position.x for p in particles])
    min_y,max_y = min([p.position.y for p in particles]), max([p.position.y for p in particles])

    if min_x != max_x:
        plt.xlim(min_x,max_x)
    else:
        plt.xlim(min_x-5, max_x+5)

    if min_y != max_y:
        plt.ylim(min_y,max_y)
    else:
        plt.ylim(min_y-5,max_y+5)

    frame_ani = animation.FuncAnimation(fig, update_frame, no_steps, fargs=(frame,), interval=5, blit=True, repeat=False)
    plt.show()

from ipywidgets import interactive
def display_vecs():
    def interactive_display(directionx=1.0, directiony=0.0):
        plt.figure(figsize=(8,8))
        vec = Vector(np.float64(3),np.float64(2))

        direction = Vector(directionx,directiony)
        normal = direction/direction.norm()

        normal_component = vec.dot(normal)
    
        remainder = vec - (normal*normal_component)
        tangent = remainder/remainder.norm()
    
        np_vec =np.array( [ [0,0,vec.x,vec.y]]) 
        np_components = np.array( [ [0,0,normal_component*normal.x, normal_component*normal.y], 
                                  [0,0,remainder.x,remainder.y]])

        X1,Y1,U1,V1 = zip(*np_vec)
        X2,Y2,U2,V2 = zip(*np_components)

        ax = plt.gca()
        ax.quiver(X1,Y1,U1,V1,angles='xy',scale_units='xy',scale=1, color='r')
        ax.quiver(X2,Y2,U2,V2,angles='xy',scale_units='xy',scale=1, linestyle='--', color='b')

        ax.set_xlim([-5,5])
        ax.set_ylim([-5,5])
        plt.draw()
        plt.show() 

    return interactive(interactive_display, directionx=(-1,1,0.1), directiony=(-1,1,0.1))
