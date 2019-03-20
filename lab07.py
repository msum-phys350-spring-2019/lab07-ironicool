# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 11:02:23 2019

@author: il8122jj
"""
import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2, -1],
              [-1, 2]])

def calc_frequencies_and_modes(matrix, k_over_m):
    
    eigenvalue, eigenvector = np.linalg.eigh(matrix)
    omega = np.sqrt(k_over_m * eigenvalue)
    
    return omega, eigenvector

def calc_components_from_initial_conditions(x_init, modes):
    
    a = x_init @ modes[:,0]
    b = x_init @ modes[:,1]
    return a, b

init_vec = np.array([12,1])
norm_init_vec = init_vec / np.sqrt(init_vec @ init_vec)

freq, vec = calc_frequencies_and_modes(A, 1)
a, b = calc_components_from_initial_conditions(norm_init_vec, vec)

#
# Erick Quntana
#

# add appropriate imports here

t_init = 0
t_end = 50
N_times = 1000

time = np.linspace(t_init, t_end, num=N_times)

# So that we can multiply the array of times by two dimensinoal vectors
# later.
time = time.reshape(N_times, 1)

def plot_motion_of_masses(x, time, title='bad title'):
    """
    Function to make a plot of motion of masses as a function of time. The time
    should be on the vertical axis and the position on the horizontal axis.
    Parameters
    ----------
    x : array of position, N_times by 2 elements
        The array of positions, set up so that x[:, 0] is the position of mass
        1 relative to equilibrium and x[:, 1] is the position of mass 2.
    time : array of times
        Times at which the positions have been calculated.
    title : str
        A descriptive title for the plot to make grading easier.
    """
    
    # Nothing special about these, but they look nice
    x1_equilibrium_pos = 3
    x2_equilibrium_pos = 6

    x1 = x[:, 0] + x1_equilibrium_pos
    x2 = x[:, 1] + x2_equilibrium_pos

    plt.plot(x1, time, label='Mass 1')
    plt.plot(x2, time, label='Mass 2')
    plt.xlim(0, 9)
    plt.legend()
    plt.title(title)

x1 = a * np.cos(freq[0] * time) * vec[:, 0]
x2 = b * np.cos(freq[1] * time) * vec[:, 1]
x = x1 + x2

plot_motion_of_masses(x, time, title='Hope')