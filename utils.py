import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from PIL import Image
import os




def plot_traj(x,u,params):

    #fig = plt.figure()
    plt.scatter(x[0], x[2], color='black', label='Drone position')

    x_drone = [x[0] + np.cos(x[4])*params[0]/2,x[0] - np.cos(x[4])*params[0]/2]
    y_drone = [x[2] + np.sin(x[4])*params[0]/2,x[2] - np.sin(x[4])*params[0]/2]
    plt.quiver(x_drone[0],y_drone[0], -u[0] * np.sin(x[4]),
               u[0]* np.cos(x[4]),color='red',scale = 10)
    plt.quiver(x_drone[1], y_drone[1], -u[1]*np.sin(x[4]),
               u[1]* np.cos(x[4]),color='red',scale=10)

    plt.xlim([-5, 5])
    plt.ylim([-2, 5])

    plt.plot(x_drone, y_drone, color='blue')
    plt.xlabel('x')
    plt.ylabel('y')
    #fig.savefig('drone_traj.png')

    plt.show(block=False)
    plt.pause(0.001)
    #plt.close(fig)
    #plt.close('all')
    plt.clf()
    return
plt.legend()

