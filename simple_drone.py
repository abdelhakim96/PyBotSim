import numpy as np
from model import model_2d
from utils import plot_traj
import matplotlib.pyplot as plt
from simulation import simulate_drone
from simple_control import simple_PID

if __name__ == '__main__':
    # drone params
    l = 1
    m = 0.5
    J = 1
    params = [l, m , J]

    n_states = 6
    n_inputs = 2


    x_init = np.zeros(n_states )
    u_init = np.zeros(n_inputs)
    x= x_init
    u = [0., 0.]

    a=1

    # reference
    x_ref = [-4.0,-5.0]

    # simation settings
    n_iter = 500
    delta_t = 0.1

    xt = simulate_drone(x,u,x_ref,params,n_iter,delta_t)
    plot_traj(x, u, params)
    #x = xt













