
  

import numpy as np
import random
import os

class DoblePercept:
    
    #Datos
    data = np.array([[0, 0],[0, 1],[1, 0],[1, 1]])
    dataTrain = np.array([[1, 1],[1, 0],[0, 1],[0, 0]])

    wight = np.array([random.random()*10, random.random()*10, random.random()*10, random.random()*10])
    bias  = np.array([random.random()*10, random.random()*10])

    LRate = 0.3
    file  = open("wight_OR.txt", "w")


    #StepFunction
    def StepFunc(Sum):
        if Sum > 0:
           out = 1
        else: out =0
        return out


#    def Train():
    def Train(wight,bias):
#        Datos
        data = np.array([[0, 0],[0, 1],[1, 0],[1, 1]])
#
        dataTrain = np.array([[1, 1],[1, 0],[0, 1],[0, 0]])

#        wight = np.array([random.random()*10, random.random()*10, random.random()*10, random.random()*10])
#        bias  = np.array([random.random()*10, random.random()*10])

        LRate   = 0.3
        file    = open("wight_OR.txt", "w")
        learn_1 = True
        learn_2 = True
        epoch   = 0

        #while (learn_1):
        while (learn_1 and learn_2):
    
            learn_1 = False
            learn_2 = False
 
            epoch += 1

            print(" Training: ", epoch, " wight -----> ", wight)


            for i in range(len(data)):

                #Neuron_1
                Sum = data[i][0] * wight[0] + data[i][1] * wight[1] + bias[0]
                out = DoblePercept.StepFunc(Sum) 
          
                E1=dataTrain[i][0]-out

                if E1 != 0:
                    wight[0]+=LRate*E1*data[i][0]
                    wight[1]+=LRate*E1*data[i][1]
                    bias [0]+=LRate*E1
                    learn_1  = True


                #Neuron_2
                Sum2 = data[i][0] * wight[2] + data[i][1] * wight[3] + bias[1]
                out2 = DoblePercept.StepFunc(Sum2)

                E2=dataTrain[i][1]-out2


                if E2 != 0:
                    wight[2]+=LRate*E2*data[i][0]
                    wight[3]+=LRate*E2*data[i][1]
                    bias [1]+=LRate*E2
                 #   learn_1  = True
                    learn_2  = True
        
            print("\n E1-----> ", E1, "Out-------> ",out)
            print(" E2-----> ", E2, "Out2------> ",out2)




    ######## Wight Save ##########
    file.write(str(wight[0]) + "\n" + str(wight[1]) + "\n" + str(wight[2])
               + "\n" + str(wight[3]) + "\n" + str(bias[0]) + "\n" + str(bias[1]))
    file.close()
 

    def Test():

        x1 = int(input("Intoduce In_1: "))
        x2 = int(input("Intoduce In_2: "))

        SumNet  = x1* DoblePercept.wight[0] + x2 * DoblePercept.wight[1] + DoblePercept.bias[0]
        Out_1 = DoblePercept.StepFunc(SumNet)
        SumNet2 = x1* DoblePercept.wight[2] + x2 * DoblePercept.wight[3] + DoblePercept.bias[1]
        Out_2 = DoblePercept.StepFunc(SumNet2)

        #Activation function

        print("{}, {} = {}, {}".format(x1,x2,Out_1,Out_2))

   

    def read():
        file = open("wight_OR.txt","r")
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


#DoblePercept.Train()
DoblePercept.Train(DoblePercept.wight,DoblePercept.bias)
DoblePercept.Test()


       

