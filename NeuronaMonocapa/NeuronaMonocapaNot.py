import numpy as np
import random
import os


#Datos
data = np.array([[0, 0],[0, 1],[1, 0],[1, 1]])
dataTrain = np.array([[1, 1],[1, 0],[0, 1],[0, 0]])


class DoublePerceptron:
    
    #StepFunction
    def StepFunc(Sum):
        if Sum > 0:
           out = 1
        else: out =0
        return out

    def Train(dataIN,dataTrainIN):

        #wight for neuron one and two
        wight1 = np.array([random.random()*10, random.random()*10, random.random()*10])
        wight2 = np.array([random.random()*10, random.random()*10, random.random()*10])
        
        LRate   = 0.3
        file    = open("wight_DoubleNot.txt", "w")
        learn = True
        epoch   = 0

        while learn:
            
            learn = False
    
            epoch += 1

            print(" Training: ", epoch, " wight1 -----> ", wight1, " wight2----> ",wight2)
            
        

            for i in range(len(dataIN)):

                #Neuron_1
                Sum  = dataIN[i][0] * wight1[0] + dataIN[i][1] * wight1[1] + wight1[2]
                out  = DoublePerceptron.StepFunc(Sum)
                E1=dataTrainIN[i][0]-out

                #Neuron_2
                Sum2 = dataIN[i][0] * wight2[0] + dataIN[i][1] * wight2[1] + wight2[2] 
                out2 = DoublePerceptron.StepFunc(Sum2)               
                E2=dataTrainIN[i][1]-out2
                
                print("Error_1------> ", E1, "Error_2------> ",E2)
                
                if E1!=0:
                    wight1[0]+=LRate*E1*dataIN[i][0]
                    wight1[1]+=LRate*E1*dataIN[i][1]
                    wight1[2]+=LRate*E1
                    learn = True

                if E2!=0:
                    wight2[0]+=LRate*E2*dataIN[i][0]
                    wight2[1]+=LRate*E2*dataIN[i][1]
                    wight2[2]+=LRate*E2
                    learn = True
                
                    
        print("\n------------End Train---------------\n")
        return wight1,wight2

        ######## Wight Save ##########
        file.write(str(wight1[0]) + "\n" + str(wight1[1]) + "\n" + str(wight2[0])
                    + "\n" + str(wight2[1]) + "\n" + str(wight1[2]) + "\n" + str(wight2[2]))
        file.close()

 

    def Test(Wight_1, Wight_2):

        x1 = int(input("Intoduce In_1: "))
        x2 = int(input("Intoduce In_2: "))

        SumNet  = x1 * Wight_1[0] + x2 * Wight_1[1] + Wight_1[2]
        Out_1 = DoublePerceptron.StepFunc(SumNet)
        SumNet2 = x1 * Wight_2[0] + x2 * Wight_2[1] + Wight_2[2]
        Out_2 = DoublePerceptron.StepFunc(SumNet2)

       

        print("{}, {} = {}, {}".format(x1,x2,Out_1,Out_2))
   

    def read():
        file = open("wight_DoubleNot.txt","r")
        wightFile = file.read()
        file.close()
        wightGet = []

        for p in wightFile.split("\n"):
            wightGet.append(float(p))


        x1 = int(input("Intoduce In_1: "))
        x2 = int(input("Intoduce In_2: "))

        SumNet  = x1 * wightGet[0] + x2 * wightGet[2] + wightGet[4]
        Out_1 = DoublePerceptron.StepFunc(SumNet)
        SumNet2 = x1 * wightGet[1] + x2 * wightGet[3] + wightGet[5]
        Out_2 = DoublePerceptron.StepFunc(SumNet2)

        print("{}, {} = {}, {}".format(x1,x2,Out_1,Out_2))

WIGHT = DoublePerceptron.Train(data,dataTrain)
DoublePerceptron.Test(WIGHT[0],WIGHT[1])