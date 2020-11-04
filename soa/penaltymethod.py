import numpy as np
from gradientdescent import RunGradientDescent

def RunPenaltyMethod():
    T = 1e-6
    step_length = 0.0001
    penalty_parameter = [1, 2, 4, 8, 16, 32, 128, 256, 512, 1024]

    x0 = np.array([1, 2])
    xMin = np.zeros([len(penalty_parameter), 3])
    i = 0

    for mu in penalty_parameter:

        x = RunGradientDescent(x0, mu, step_length, T)
        xMin[i,:] = np.append(mu, x)
        i+=1

    return 0

RunPenaltyMethod()
