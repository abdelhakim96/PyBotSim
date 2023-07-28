import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os




def plot_traj(x,u,params):

    plt.scatter(x[0], x[2], color='black', label='Drone position')

    x_drone = [x[0] + np.cos(x[4])*params[0]/2,x[0] - np.cos(x[4])*params[0]/2]
    y_drone = [x[2] + np.sin(x[4])*params[0]/2,x[2] - np.sin(x[4])*params[0]/2]
    plt.quiver(x_drone[0],y_drone[0], -u[0] * np.sin(x[4]),
               u[0]* np.cos(x[4]),color='red',scale=1)
    #print(u[0]* np.cos(x[4]))
    plt.quiver(x_drone[1], y_drone[1], -u[1]*np.sin(x[4]),
               u[1]* np.cos(x[4]),color='red',scale=1)
    plt.plot(x_drone, y_drone, color='blue')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    return