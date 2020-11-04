import numpy as np
from gradient import ComputeGradient

def norm(x):
    x_length = len(x)
    x_i = 0

    for i in range(x_length):
        x_i = x_i + x[i]**2

    x_normed = np.sqrt(x_i)

    return x_normed


def RunGradientDescent(x0, penalty_degree, learning_rate, termination_condition):

    eta = learning_rate
    mu = penalty_degree
    T = termination_condition

    x = np.zeros([2,1])

    converged = False

    while not converged:

        gradF = ComputeGradient(x0[0], x0[1], mu)

        x[0] = x0[0] - eta*gradF[0]
        x[1] = x0[1] - eta*gradF[1]

        # print(x)

        if norm(gradF) < T:
            converged = True

        x0 = x

    output = x
    return output
