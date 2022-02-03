import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib.collections import EllipseCollection
import numpy as np 

def animate_simulation(s,loop=False,display_step=False,interval=10):
    '''Animates the trajectory of a simulation object.'''
    def add_dots():
        frame.add_collection(dots)
        return dots,
    
    def update_frame(i, dots,text=None):
        dots.set_offsets([(p.position.x, p.position.y) for p in s.trajectory[i]])

        if display_step:
            text.set_text(str(i))
    
        if text:
            return dots,text
        else:
            return dots,

    particle_sizes = [2*p.radius for p in s.particles]
    if len(set(particle_sizes))==1:
        particle_sizes = particle_sizes[0]
    no_steps = len(s.trajectory)
    
    fig,frame = plt.subplots()
    frame.set(aspect=1,xlim=(0,s.box_length),ylim=(0,s.box_length))
    dots=EllipseCollection(widths=particle_sizes,heights=particle_sizes,angles=0,
                       units='x',
                       offsets=[],
                       transOffset=frame.transData)

    if display_step:
        text = frame.text(0.9*s.box_length,0.9*s.box_length,'')
    else:
        text = None

    #on some systems, particularly macOS, blit option below may cause display glitches
    #change to blit=False if needed
    frame_ani = animation.FuncAnimation(fig, update_frame, no_steps, init_func=add_dots,
                                        fargs=(dots,text), interval=interval, blit=True, repeat=loop)

    return frame_ani


def display_particle(p):
    '''Simple function that displays one particle object p in a vacuum.'''
    
    min_x,max_x=(p.position.x-10*p.radius,p.position.x+10*p.radius)
    min_y,max_y=(p.position.y-10*p.radius,p.position.y+10*p.radius)
    ax=plt.axes(aspect=1,xlim=(min_x, max_x), ylim=(min_y, max_y))
    ax.add_artist(plt.Circle((p.position.x,p.position.y),radius=p.radius))
    plt.show()

    
def display_particle_motion(particles):
    '''
    Animate a list of particle objects, effectively showing
    the trajectory of a single particle.
    '''

    no_steps = len(particles)
    rad = particles[0].radius
    min_x,max_x = min([p.position.x for p in particles]), max([p.position.x for p in particles])
    min_y,max_y = min([p.position.y for p in particles]), max([p.position.y for p in particles])
    
    fig=plt.figure()
    frame=plt.gca()
    frame.set(aspect=1,xlim=(min_x-2*rad,max_x+2*rad),ylim=(min_y-2*rad,max_y+2*rad))
    dot=plt.Circle((0,0),radius=rad)
    
    def first_dot():
        frame.add_artist(dot)
        return dot,
        
    def update_frame(i,dot):
        dot.set_center((particles[i].position.x,particles[i].position.y))
        return dot,

    frame_ani = animation.FuncAnimation(fig, update_frame, no_steps, init_func=first_dot,
                                        fargs=(dot,), interval=10, blit=True, repeat=False)
    return frame_ani


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