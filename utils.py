import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Import Axes3D for 3D plotting

from PIL import Image
import os

fig = plt.figure()



def plot_3Dtraj(x, u, x_ref, params, T_d_y, T_d_x):


    ax = fig.add_subplot(111, projection='3d')  # Create a 3D subplot

    ax.scatter(x[0], 0.0, x[2], color='black', label='Drone position')  # Use x[1] for the y-coordinate

    ax.scatter(x_ref[0], 0.0, x_ref[1], color='green', label='Goal position')  # Use x_ref[1] for the y-coordinate

    x_drone = [x[0] + np.cos(-x[4]) * params[0] / 2, x[0] - np.cos(-x[4]) * params[0] / 2]
    y_drone = [x[2] + np.sin(-x[4]) * params[0] / 2, x[2] - np.sin(-x[4]) * params[0] / 2]
    z_drone = [x[1], x[1]]  # Use x[1] for the z-coordinate

    ax.quiver(x_drone[0], y_drone[0], z_drone[0], -u[0] * np.sin(-x[4]),
              u[0] * np.cos(-x[4]), 0, color='red')  # Set the z-component of the arrow to 0
    ax.quiver(x_drone[1], y_drone[1], z_drone[1], -u[1] * np.sin(-x[4]),
              u[1] * np.cos(-x[4]), 0, color='red')  # Set the z-component of the arrow to 0

    ax.quiver(x[0], x[2], x[1], T_d_x, T_d_y, 0, color='green')  # Set the z-component of the arrow to 0

    ax.plot(x_drone, y_drone, z_drone, color='blue')  # Use x[1] and z_drone for the y and z-coordinates

    ax.set_xlim([-5, 5])
    ax.set_ylim([-2, 5])
    ax.set_zlim([-5, 5])  # Set the z-limits for the 3D plot

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')  # Set labels for the x, y, and z-axes

    plt.legend()
    plt.show(block=False)
    plt.pause(0.001)

    plt.clf()
    return


def plot_traj(x,u,x_ref,params,T_d_y,T_d_x):

    #fig = plt.figure()
    plt.scatter(x[0], x[2], color='black', label='Drone position')

    plt.scatter(x_ref[0], x_ref[1], color='green', label='Goal position')


    x_drone = [x[0] + np.cos(-x[4])*params[0]/2,x[0] - np.cos(-x[4])*params[0]/2]
    y_drone = [x[2] + np.sin(-x[4])*params[0]/2,x[2] - np.sin(-x[4])*params[0]/2]
    plt.quiver(x_drone[0],y_drone[0], -u[0] * np.sin(-x[4]),
               u[0]* np.cos(-x[4]),color='red',scale = 100)
    plt.quiver(x_drone[1], y_drone[1], -u[1]*np.sin(-x[4]),
               u[1]* np.cos(-x[4]),color='red',scale=100)

    plt.quiver(x[0],x[2], T_d_x ,T_d_y,color='green',scale = 500)
    plt.quiver(x_drone[1], y_drone[1], -u[1]*np.sin(-x[4]),
               u[1]* np.cos(-x[4]),color='red',scale=100)



    plt.xlim([-5, 5])
    plt.ylim([-2, 5])

    plt.plot(x_drone, y_drone, color='blue')
    plt.xlabel('x')
    plt.ylabel('y')
    #fig.savefig('drone_traj.png')

    plt.legend()
    plt.show(block=False)
    plt.pause(0.001)

    #plt.close(fig)
    #plt.close('all')
    plt.clf()
    return