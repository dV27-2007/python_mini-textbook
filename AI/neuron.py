import numpy as np


class Neuron: # sarqum enq class Neuron
    def __init__(self, w):
        self.w = w

    def y(self, x):                 # avelacnoxe
        s = np.dot(self.w, x)       # gumarum enq mutqere | Wi[0]*Xi[0 ]+ ... + Wi[n]*Xi[n]
        return s                    # aktivacman funkcyan


Xi = np.array([2, 3]) # trvac nshanere mtneluc | [2 3]
Wi = np.array([1, 1]) # motqi senseri qashere | [1 1]
n = Neuron(Wi) # sarqum enq obyekt Neuron classi

print('S1 =', n.y(Xi)) # dimum enq neuronin
# S1 = 5

Xi = np.array([5, 6]) # motqi senseri qashere | [5 7]

print('S2 =', n.y(Xi)) # dimum enq neuronin
# S2 = 11

# Wi arajin andame bazamapatkvuma Xi arjin andami u etenc minjev
# n-erord andam u boloer gumarvum e talis e mi hat @ndhanur tiv - S

