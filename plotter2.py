import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.animation import FuncAnimation
import random
from custom_sim import *

data = simulate(20, np.linspace(0, 10, 101), 3, 0.5, 50)
# print(data)
# print(len(np.linspace(0,10,101)))

fig =plt.figure()                       #establish a figure
ax = fig.add_subplot(111, projection='3d')  #establish a 3D space
x=np.linspace(-10,10)            #Set up the x axis limits
y=np.linspace(-10,10)            #Set up the y axis limits
z=np.linspace(-10,10)            #Set up the z axis limits
ax.plot(0,0,0, marker=".", markersize=10, color="red") #setting the piece of meat at 0,0,0

def animate(i):             #i is the frame of our animation
    for j in range(20):
        ax.plot(data[j,:i,0], data[j,:i,1], data[j,:i,2])
        # graph.set_data(x[:i],y[:i])     #filling in the x and y data
        # graph.set_3d_properties(z[:i])  #filling in the z data

    
anim = FuncAnimation(fig, animate,frames=100,interval=5)
# ax.view_init(azim=random.randint(0,90),elev=random.randint(0,90)) 
plt.show() 

#Enabling the animation 
#the number of frames should be equal to the length of our x array. We add 1 to make sure the index matches the number of values.
#interval is the time in milliseconds before the next point is displayed in the graph. lower = faster.
#blit=true means that the animation will only display the part of the line that is changed, not the total one


