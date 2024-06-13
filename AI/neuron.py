import numpy as np


class Neuron: # sarqum enq class Neuron
    def __init__(self, w):
        self.w = w

    def y(self, x):                 # avelacnoxe
        s = np.dot(self.w, x)       # gumarum enq mutqere
        return s                    # aktivacman funkcyan


Xi = np.array([2, 3]) #
Wi = np.array([1, 1])
n = Neuron(Wi)

print('S1 =', n.y(Xi))

Xi = np.array([5, 6])

print('S2 =', n.y(Xi))
