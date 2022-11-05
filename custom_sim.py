import numpy as np
import random


def force_law(dist):
    return dist/(np.norm(dist))**3

class Shark:
    def __init__(self, position, velocity, alpha, zoo, zor, zoa):
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
        self.hunger_thresh = 0.5
        self.hunger_rate = -0.1

        self.food_size = 0.1




    def update_a(self, sharks):
        self.acceleration = 0

        # Changing acceleration due to food
        if self.hungry:
            # Food is attractive 
            self.acceleration -= self.position/np.linalg.norm(self.position)**3
        else:
            # Food is not attractive
            self.acceleration += self.position/np.linalg.norm(self.position)**3


        # Changing acceleration due to other sharks
        for shark in sharks: 
            # Disancd between sharks
            dis = shark.position - self.position
            # Angle between sharks
            angle = 0
            # Norm of distance between sharks
            norm = np.linalg.norm(dis)


            if angle < self.alpha:
                # Check if other shark is in field of view

                if 0 < norm < self.zoo:
                    # Shark is in repulsive zone
                    self.acceleration -= 1/norm**3 * dis
                    

                elif self.zoo <= norm < self.zor and not self.hungry:
                    # Shark is in direction matching zone (zone of orientation)
                    self.acceleration += shark.velocity/norm**2/np.linalg.norm(shark.velocity)


                elif self.zor <= norm <= self.zoa and not self.hungry:
                    # Shark is in attractive zone
                    self.lin_acceleration += 1/norm**3 * dis

                elif norm < 0:
                    # Error with position
                    print("Error in Shark position...")


    def update_v(self, dt):

        # Compute new velocity
        self.velocity = self.velocity + self.acceleration*dt
        # Normalize velocity
        self.velocity = self.velocity/np.linalg.norm(self.velocity)

        if not self.hungry:
            # Hunger increases at every time step
            self.hunger += self.hunger_rate*dt

            # Given probability shark can become hungry
            if np.exp(-self.hunger*2) > random.random():
                self.hungry = True



        if np.linalg.norm(self.position) < self.food_size: # Shark is on food
            self.hungry = False # Stops being hungry
            self.hunger = 1 

    def update_p(self, dt):
        self.position += self.velocity*dt 






if __name__ == "__main__":

    import matplotlib.pyplot as plt

    # Instantiate sharks
    sharks = []
    for i in range(3):
        sharks.append(Shark(
            np.random.rand(3)*20 - 10,  # Positions
            np.random.rand(3),          # Velocities
            0,                          # alpha
            3,                          # zoo
            0.5,                         # zor
            10,                         # zoa
            ))


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
time_array = np.linspace(0, 10, 101)
shark_nb = 3

data = np.zeros((shark_nb, len(time_array)))

for t_ind, time in enumerate(time_array):
    for i, v in enumerate(sharks):
        new_s = [j for j in np.delete(sharks, i)]
        v.update_a(new_s)
        v.update_v(0.1)
    for i, shark in enumerate(sharks):
        shark.update_p(0.1)

        data[i, t_ind] = shark.position

    
    

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

















