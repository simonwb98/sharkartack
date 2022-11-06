import numpy as np
import random


def force_law(dist):
    return dist/(np.norm(dist))**3

class Shark:
    def __init__(self, position, velocity, alpha, zoo, zor, zoa, food_size):
        self.position = position
        self.velocity = velocity/np.linalg.norm(velocity)
        self.acceleration = np.array([0, 0, 0])
        self.alpha = alpha
        self.zoo = zoo
        self.zor = zor
        self.zoa = zoa
        #self.parameters = parameters

        self.hunger = random.random()
        self.hungry = False
        self.hunger_rate = -0.1*random.random()

        self.food_size = food_size




    def update_a(self, sharks):
        self.acceleration = 0
        
        # Changing acceleration due to food
        if self.hungry or np.linalg.norm(self.position) > 10:
            # Food is attractive 
            #print("hungry")
            self.acceleration -= 5*self.position/np.linalg.norm(self.position)

        elif not self.hungry and np.linalg.norm(self.position) < 3:
            # Food is repulsive
            #print("not hungry")
            self.acceleration += 10*self.position/np.linalg.norm(self.position)
    


        # Changing acceleration due to other sharks
        for shark in sharks: 
            # Disancd between sharks
            dis = shark.position - self.position
            # Angle between sharks
            angle = 0
            # Norm of distance between sharks
            norm = np.linalg.norm(dis)

            f_const = 1
            expon = 1

            # Check if other shark is in field of view
            
            if 0 < norm < self.zor:
                # Shark is in repulsive zone
                self.acceleration -= f_const*1/norm**expon * dis
                

            elif self.zor <= norm < self.zoo:# and not self.hungry:
                # Shark is in direction matching zone (zone of orientation)
                self.acceleration += f_const*shark.velocity/norm**expon/np.linalg.norm(shark.velocity)/5


            elif self.zoo <= norm <= self.zoa:# and not self.hungry:
                #print("Attracts:", f_const*1/norm**expon * dis)
                # Shark is in attractive zone
                self.acceleration += f_const*1/norm**expon * dis

            elif norm < 0:
                # Error with position
                print("Error in Shark position...")


    def update_v(self, dt):

        # Compute new velocity
        self.velocity = self.velocity + self.acceleration*dt
        # Normalize velocity
        self.velocity = self.velocity/np.linalg.norm(self.velocity)
        #print("Hunger:", self.hunger)       
        if not self.hungry:
            # Hunger increases at every time step
            self.hunger += self.hunger_rate*dt
            

            # Given probability shark can become hungry
            myrand = random.random()
            #print("Prob:", myrand)
            #print("Exponent:", np.exp(-self.hunger*4))
            if np.exp(-self.hunger*8) > myrand:#random.random():
                self.hungry = True



        if np.linalg.norm(self.position) < self.food_size: # Shark is on food
            #print("feeds")
            #print(self.position)
            self.hungry = False # Stops being hungry
            self.hunger = 1.0 

    def update_p(self, dt):
        self.position += self.velocity*dt 


def simulate(nb_sharks, time_array, zoo, zor, zoa, food_size):
     # Instantiate sharks

    sharks = []
    dt = time_array[1]-time_array[0]

    for i in range(nb_sharks):
        sharks.append(Shark(
            np.random.rand(3)*10 - 5,  # Positions
            np.random.rand(3)*10 - 5,      # Velocities
            0,                          # alpha
            zoo,                          # zoo
            zor,                        # zor
            zoa,                         # zoa
            food_size
            ))

    # Create data array
    data = np.zeros((nb_sharks, len(time_array), 3))

    for t_ind, time in enumerate(time_array):
        for i, v in enumerate(sharks):
            # Updating acceleration and velocity
            new_s = [j for j in np.delete(sharks, i)]
            v.update_a(new_s)
            v.update_v(dt)

        for i, shark in enumerate(sharks):
            # Updating position
            shark.update_p(dt)

            # Storing data into array
            data[i, t_ind, :] = shark.position

    return data




if __name__ == "__main__":

    import matplotlib.pyplot as plt

    food_size = 0.1
    data = simulate(20, np.linspace(0, 100, 1001), 3, 0.5, 50, food_size)
    # Plotting everything

    fig = plt.figure()

    ax = fig.add_subplot(111, projection = '3d')

    #print(data)

    for i in range(20):
        ax.plot(data[i,:,0], data[i,:,1], data[i,:,2])

    ax.scatter([0], [0], [0], s = 10)

    plt.show()
    
    '''
    # Instantiate sharks
    shark_nb = 20
    sharks = []
    for i in range(shark_nb):
        sharks.append(Shark(
            np.random.rand(3)*20 - 10,  # Positions
            np.random.rand(3)*2-1,          # Velocities
            0,                          # alpha
            3,                          # zoo
            0.5,                         # zor
            50,                         # zoa
            ))


    


'''
'''
for i in sharks:
    print("acceleration:", i.acceleration)
print()
for i in sharks:
    print("velo:", i.velocity)
print()
for i in sharks:
    print("pos:", i.position)
print()'''
#time_array = np.linspace(0, 10, 1001)
'''
data = np.zeros((shark_nb, len(time_array), 3))

for t_ind, time in enumerate(time_array):
    for i, v in enumerate(sharks):
        new_s = [j for j in np.delete(sharks, i)]
        v.update_a(new_s)
        v.update_v(0.1)
    for i, shark in enumerate(sharks):
        shark.update_p(0.1)

        data[i, t_ind, :] = shark.position

'''



    

    
    

'''print()

for i in sharks:
    print("acceleration:", i.acceleration)
print()

for i in sharks:
    print("velo:", i.velocity)
print()

for i in sharks:
    print("pos:", i.position)
print()'''

















