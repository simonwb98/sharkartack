import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.animation import FuncAnimation
import random
import matplotlib.colors as colors
from custom_sim import *

food_size = 0.1
data = simulate(20, np.linspace(0, 300, 1001), 3, 0.5, 50, food_size)
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



anim = FuncAnimation(fig, animate,frames=300,interval=100)
# ax.view_init(azim=random.randint(0,90),elev=random.randint(0,90)) #Randomize the view
anim.save('20sharks.gif', writer='imagemagick')
# anim.save('20sharks.mp4', writer='ffmpeg')
plt.show() 

#the number of frames should be equal to the length of our x array. We add 1 to make sure the index matches the number of values.
#interval is the time in milliseconds before the next point is displayed in the graph. lower = faster.


