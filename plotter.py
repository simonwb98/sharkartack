import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.animation import FuncAnimation
import random

fig =plt.figure()                       #establish a figure
ax = fig.add_subplot(111, projection='3d')  #establish a 3D space
x=np.linspace(-5,50)            #Set up the x axis limits
y=np.linspace(-5,30)            #Set up the y axis limits
z=np.linspace(-5,50)            #Set up the z axis limits
graph,=ax.plot(x,y,z)    #create an empty line. (the comma means that we unpack the result and make it iterable)

def animate(i):             #i is the frame of our animation
    graph.set_data(x[:i],y[:i])     #filling in the x and y data
    graph.set_3d_properties(z[:i])  #filling in the z data
    return graph,

anim = FuncAnimation(fig, animate,frames=2*len(x)+1,interval=100)     #Enabling the animation 
#the number of frames should be equal to the length of our x array. We add 1 to make sure the index matches the number of values.
#interval is the time in milliseconds before the next point is displayed in the graph. lower = faster.
#blit=true means that the animation will only display the part of the line that is changed, not the total one
ax.view_init(azim=random.randint(0,90),elev=random.randint(0,90)) 
plt.show()              #displaying the graph
