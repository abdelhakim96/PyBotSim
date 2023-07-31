import numpy as np
from model import drone_model_2d
from utils import plot_traj
import matplotlib.pyplot as plt
from simple_control import simple_PID

def simulate_drone(x,u,x_ref,params,n_iter,delta_t):
    for i in range(n_iter):
        x_t1 = drone_model_2d(x,u,params)
        x[0] = x[0] + x[1] * delta_t
        x[1] = x[1] + x_t1[0] * delta_t
        x[2] = x[2] + x[3] * delta_t
        x[3] = x[3] + x_t1[1] * delta_t
        x[4] = x[4] + x[5] * delta_t
        x[5] = x[5] + x_t1[2] * delta_t


        Kp_x = 1
        Kp_y = 1
        Kp_th = 7.0
        [u,T_d_y,T_d_x] = simple_PID (x,x_ref,Kp_x,Kp_y, Kp_th)
        plot_traj(x,u,x_ref,params,T_d_y,T_d_x)


    return x,T_d_y,T_d_x






