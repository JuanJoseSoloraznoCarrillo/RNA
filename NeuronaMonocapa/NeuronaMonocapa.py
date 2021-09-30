

import numpy as np
import random

#Datos
wight = np.array([random.random()*10, random.random()*10, random.random()*10, random.random()*10])
bias  = np.array([random.random()*10,random.random()*10])
data = np.array([[0, 0],[0, 1],[1, 0],[1, 1]])
dataTrain = np.array([[1, 1],[1, 0],[0, 1],[0, 0]])

class DoblePercept:
    
    #StepFunction
    def StepFunc(Sum):
        if Sum > 0:
           out = 1
        else: out =0
        return out


    def Train():

        learn   = True
        learn01 = True
        learn02 = True
        out     = float(2.5)
        epoch   = 0

        while (learn01 & learn02):
    
            learn = False
            learn01 = False
            learn02 = False
            epoch += 1
            print(" Training: ", epoch, " wight -----> ", wight)

            for i in range(len(data)):

                #Neuron_1
                Sum  = data[i][0] * wight[0] + data[i][1] * wight[2] + bias[0]

                #Activation Step Function
                out = DoblePercept.StepFunc(Sum) 
          

                if out != dataTrain[i][0]:
                    wight[0] = random.random() * 10 - random.random() * 10
                    wight[2] = random.random() * 10 - random.random() * 10
                    learn01  = True


            for i in range(len(data)):
                #Neuron_2
                Sum2 = data[i][0] * wight[1] + data[i][1] * wight[3] + bias[1]

                out2 = DoblePercept.StepFunc(Sum2)

                if out2 != dataTrain[i][1]:
                    wight[1] = random.random() * 10 - random.random() * 10
                    wight[3] = random.random() * 10 - random.random() * 10
                    learn02  = True

    
                    
    def Test():

        x1 = int(input("Intoduce In_1: "))
        x2 = int(input("Intoduce In_2: "))

        SumNet  = x1 * wight[0] + x2 * wight[2] + bias[0]
        Out_1 = DoblePercept.StepFunc(SumNet)
        SumNet2 = x1 * wight[1] + x2 * wight[3] + bias[1]
        Out_2 = DoblePercept.StepFunc(SumNet2)

        #Activation function

        print("{}, {} = {}, {}".format(x1,x2,Out_1,Out_2))



DoblePercept.Train()
DoblePercept.Test()

       

