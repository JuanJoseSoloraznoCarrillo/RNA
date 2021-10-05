


import numpy as np
import random
import os

#Datos
wight = np.array([random.random()*10, random.random()*10, random.random()*10, random.random()*10,
                  random.random()*10, random.random()*10, random.random()*10, random.random()*10])

bias  = np.array([random.random()*10,random.random()*10])
data  = np.array([[0.7, 3, 1.5, 5],[2.0, 9, 0.9, 11],[4.2, 0, 2.2, 1],[3.6, 7,4.5,6]])
dataTrain = np.array([[0, 0],[0, 1],[1, 0],[1, 1]])
LRate = 0.3
file  = open("wight_Biblioteca.txt", "w")

class Biblioteca:
    
    #StepFunction
    def StepFunc(Sum):
        if Sum > 0:
           out = 1
        else: out =0
        return out


    def Train(wight,bias):
        data  = np.array([[0.7, 3, 1.5, 5],[2.0, 9, 0.9, 11],[4.2, 0, 2.2, 1],[3.6, 7,4.5,6]])
        dataTrain = np.array([[0, 0],[0, 1],[1, 0],[1, 1]])
        LRate = 0.3
        file  = open("wight_Biblioteca.txt", "w")
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
                Sum  = data[i][0] * wight[0] + data[i][1] * wight[2] + data[i][2] * wight[4]+ data[i][3] * wight[5] + bias[0]

                #Activation Step Function
                out = Biblioteca.StepFunc(Sum) 
                E1=dataTrain[i][0]-out
         
                if E1 != 0:
                    wight[0]+=LRate*E1*data[i][0]
                    wight[1]+=LRate*E1*data[i][1]
                    bias [0]+=LRate*E1
                    learn_1  = True


                #Neuron_2
                Sum2 = data[i][0] * wight[1] + data[i][1] * wight[3] + data[i][2] * wight[6] + data[i][3] * wight[7] + bias[1]

                out2 = Biblioteca.StepFunc(Sum2)
                E2=dataTrain[i][1]-out2

                if E2 != 0:
                    wight[2]+=LRate*E2*data[i][0]
                    wight[3]+=LRate*E2*data[i][1]
                    bias [1]+=LRate*E2
                    learn_2  = True



    ######## Wight Save ##########
    file.write(str(wight[0]) + "\n" + str(wight[1]) + "\n" + str(wight[2])
               + "\n" + str(wight[3]) + "\n" + str(bias[0]) + "\n" + str(bias[1]))
    file.close()



                    
    def Test():

        x1 = float(input("Intoduce In_1: "))
        x2 = float(input("Intoduce In_2: "))

        SumNet  = x1 * wight[0] + x2 * wight[2] + bias[0]
        Out_1 = DoblePercept.StepFunc(SumNet)
        SumNet2 = x1 * wight[1] + x2 * wight[3] + bias[1]
        Out_2 = DoblePercept.StepFunc(SumNet2)

        #Activation function

        print("{}, {} = {}, {}".format(x1,x2,Out_1,Out_2))

class readData:
    
    def read():
        file = open("wight_Biblioteca.txt","r")
        wightFile = file.read()
        file.close()
        wightGet = []

        for p in wightFile.split("\n"):
            wightGet.append(float(p))


        x1 = int(input("Intoduce In_1: "))
        x2 = int(input("Intoduce In_2: "))

        SumNet  = x1 * wightGet[0] + x2 * wightGet[2] + wightGet[4]
        Out_1 = DoblePercept.StepFunc(SumNet)
        SumNet2 = x1 * wightGet[1] + x2 * wightGet[3] + wightGet[5]
        Out_2 = DoblePercept.StepFunc(SumNet2)

        #Activation function
        if SumNet > 0:
            out1 = 1
        else: out1 =0

        print("{}, {} = {}, {}".format(x1,x2,Out_1,Out_2))

Biblioteca.Train();
Biblioteca.Test();