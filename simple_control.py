import numpy as np
from model import drone_model_2d
from utils import plot_traj
import matplotlib.pyplot as plt


def simple_PID (x,x_ref,Kp_x,Kp_y, Kp_th):
    Kd_y = Kp_y * 1.0
    Kd_x = Kp_x * 10.0

    Kd_th = Kp_th * 3
    Kp1_x = 3 * Kp_x
    Kd1_x = 6 * Kd_x

    #Compute errors in x and y
    e_x = x[0] - x_ref[0]
    e_y = x[2] - x_ref[1]

    e_d_x = x[1] -0.0
    e_d_y = x[3] -0.0
    e_d_th = x[5] - 0.0

    #Compute desired Thrust and angle
    T_d_y = - Kp_y * e_y - Kd_y * e_d_y
    T_d_x = - Kp_x * e_x - Kd_x * e_d_x

    Th_d = - Kp1_x * e_x - Kd1_x * e_d_x
    Th_d = np.clip(Th_d, -0.5, 0.5)
    e_th =  x[4] - Th_d
    M_d = - Kp_th * e_th - Kd_th * e_d_th

    #Transform desired thrust to body frame
    R = np.array([[np.cos(x[4]), - np.sin(x[4])], [np.sin(x[4]),  np.cos(x[4])]])
    print('R',R)
    R_T = np.transpose(R)
    T_d_b = R_T @ np.array([T_d_x, T_d_y])
    T_d_b = np.clip(T_d_b, -2., 2.0)
    TAM = np.array([[1, 1], [1, -1]])
    u = np.linalg.pinv(TAM) @ np.array([T_d_b[1],M_d])

    print('u = ', u)
    #print('x =',  x[0])
    print('ey =', e_y)
    print('ex =', e_x)
    print('theta =', x[4]*(180/np.pi))

    print('thrust =',(u[0]+u[1]))

    #print('theta =', x[4])


    return u





