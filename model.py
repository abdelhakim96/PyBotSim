import numpy as np

x_t1 =np.zeros(3)

def drone_model_2d (x,u,params):
    g = 10
    x_t1[0] =  ((u[0]+u[1]) * np.sin(x[4]))/(params[1])
    x_t1[1] =  ((u[0]+u[1]) * np.cos(x[4]))/(params[1]) - g
    x_t1[2] = ((params[0]/2)*(u[0]-u[1]) )/(params[2])

    return x_t1
