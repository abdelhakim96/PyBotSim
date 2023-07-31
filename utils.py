import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from PIL import Image
import os




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


