#----- imports ------#
import numpy as np
import matplotlib.pyplot as plt

#---- Class implementation ----#
class Neural(object):
    """
    """
    def __init__(self,input_size,hidden_size,output_size):
        """
        """
        print('>> Creating neuron...')
        self.input_size=input_size
        self.hidden_size=hidden_size
        self.output_size=output_size
        #----- Create a matrix -----#
        print('>> weights creation...')
        self.w1=np.random.randn(self.input_size, self.hidden_size)
        self.w2=np.random.randn(self.hidden_size, self.output_size)
        print('Weight_1 lenght %s' %str(len(self.w1)))
        print('Weight_2 lenght %s' %str(len(self.w2)))
        print('>> [*] Neuron net created.')

    def forward(self, inputs):
        #---- Performing the dot product between the input matriz and the weights matrix -----#
        self.z1=np.dot(inputs, self.w1)

        self.a1=self.sigmoide(self.z1)
        self.z2=np.dot(self.a1, self.w2)
        self.output=self.sigmoide(self.z2)
        return self.output

    def backpropagation(self, x,y,lr):
        output=self.forward(x)
        error_out=output-y
        delta_out=error_out * self.sigmoide_der(output)
        derivative_w2=np.dot(self.a1.T,delta_out)
        error_hidden=np.dot(delta_out,self.w2.T)
        delta_hidden=error_hidden * self.sigmoide_der(self.a1)
        derivative_w1=np.dot(inputs.T,delta_hidden)
        #gradiente descendiente
        self.w2-=derivative_w2*lr
        self.w1-=derivative_w1*lr
        return self.mse(output, y)

    def sigmoide(self, x):
        return 1/(1+np.exp(-x))

    def sigmoide_der(self, x):
        return x*(1-x)
    def mse(self, output, target):
        return np.mean((output-target)**2)/2

def start():
    #----- constants -----#
    inputs=np.array([[0,0,1],
                     [0,1,1],
                     [1,0,1],
                     [1,1,1]])
    y=np.array([[1],
                [0],
                [0],
                [1]])
    nn=NeuralNet(3,3,1)
    print("antes:")
    print(nn.forward(inputs))
    errors=[]
    error=1

    while error>0.01:
        error=nn.backpropagation(inputs,y, 1)
        errors.append(error)

    print("despues")
    print(nn.forward(inputs))
    x_axis=range(0, len(errors))
    plt.plot(x_axis, errors)
    plt.show()

