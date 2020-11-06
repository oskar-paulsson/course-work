import numpy as np

class ObjectiveFunction:
    def __init__(self):
        self.objective = 'minimize' # a string, minimize or maximize

    def Function(self, x):
        x1 = x[0]
        x2 = x[1]
        
        return x2*x1**2 + 4*x1*x2**2 - x1*x2**3
        
    def Evaluate(self, x):
        
        if self.objective.lower() == 'minimize':
            fitness = 1/self.Function(x)
            
        if self.objective.lower() == 'maximize':
            fitness = self.Function(x)
            
        return fitness