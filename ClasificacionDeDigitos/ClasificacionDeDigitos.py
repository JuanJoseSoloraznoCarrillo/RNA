

import numpy as np
import matplotlib.pyplot as plt

inputs=np.array([[1,1,1,1,1,1,0,1],
                 [0,1,1,0,0,0,0,1],
                 [1,1,0,1,1,0,1,1],
                 [1,1,1,1,0,0,1,1],
                 [0,1,1,0,0,1,1,1],
                 [1,0,1,1,0,1,1,1],
                 [1,0,1,1,1,1,1,1],
                 [1,1,1,0,0,0,0,1],
                 [1,1,1,1,1,1,1,1],
                 [1,1,1,1,0,1,1,1]])#entradas

y=np.array([[1,0,0], #0
            [0,1,0], #1
            [1,0,0], #2
            [0,1,0], #3
            [1,0,0], #4
            [0,1,0], #5
            [1,0,0], #6
            [0,1,1], #7
            [1,0,1], #8
            [0,1,1]])#9   #Salidas

class NeuralNet():
    ''' Red neuronal'''
    def __init__(self,input_size,hidden_size,output_size):
        self.input_size=input_size
        self.hidden_size=hidden_size
        self.output_size=output_size
        'Pesos asociados a las capas ocultas y de salidas'
        self.w1=np.random.randn(self.input_size,  self.hidden_size)
        self.w2=np.random.randn(self.hidden_size, self.output_size)

    def forward(self, x):
        self.z1=np.dot(x, self.w1)
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

'---------fin de la clase NeuralNet--------------'

def redondear(Ins):
    '''Covierte el resultado float a bool'''
    Out = nn.forward(Ins)
    for i in range(len(Out)):
        for j in range(np.size(Out[0])):
            if Out[i][j] < 0.5:
                Out[i][j] = 0
            else:
                Out[i][j] = 1
    return Out

def entrenar(tol,lr,datosIN):
    '''reajuste de los pesos'''
    errors=[]
    error=1
    while error>tol:
        error=nn.backpropagation(datosIN,y,lr)
        errors.append(error)
    return errors

def salida():
    '''Interpreta la salida de la red neuronal'''
    print("\nLa interpretación es: \n")
    for v in range(len(values)):
        if(values[v][0]==1 and values[v][2]==0):
            print("El número: ",v," Es par")
        if(values[v][1]==1 and values[v][2]==0):
            print("El número: ",v," Es impar")
        if(values[v][2]==1 and values[v][0]==1):
            print("El número: ",v," Es par y mayor o igual a 7")
        if(values[v][2]==1 and values[v][1]==1):
            print("El número: ",v," Es impar y mayor o igual a 7")

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'objecto'
nn=NeuralNet(8,8,3)

print("Antes del ajuste de pesos:\n")
print(nn.forward(inputs))

errors = entrenar(0.01,0.1,inputs)
print("\nÉpocas = ", len(errors))
values = redondear(inputs)

print("\n Despues: \n\n ",values)
salida()

'plot'
x_axis=range(0, len(errors))
plt.plot(x_axis, errors)
plt.show()