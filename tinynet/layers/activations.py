from .base import Layer
from tinynet.core import Backend as np

class ReLu(Layer):
    '''
    ReLu layer performs rectifier linear unit opertaion.
    '''
    def __init__(self, name):
        super().__init__(name)
        self.type='ReLu'

    def forward(self, input):
        '''
        In the forward pass, the output is defined as :math:`y=max(0, x)`.
        '''
        self.input = input
        return input * (input > 0)

    def backward(self, in_gradient):
        return in_gradient * 1.0 * (self.input > 0)


class LeakyReLu(Layer):
    '''
    '''
    def __init__(self, name, k):
        super().__init__(name)
        self.k = k
        self.type = 'LeakyReLu'
    
    def forward(self, input):
        self.input = input
        return np.where(input > 0, input, input * self.k)
    
    def backward(self, in_gradient):
        return np.where(self.input > 0, in_gradient * 1.0, in_gradient * self.k)