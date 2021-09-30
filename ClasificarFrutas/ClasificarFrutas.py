

#### Libraries ####
import random
import numpy as np
import os
   
######  Data  #########
data  = np.array([[1.5,-0.3,1],[0.9,0.05,1],[2.1,0.2,1.0],[0.24,-0.87,0],[0.45,-0.6,0],[0.15,-0.43,0]])
wight = np.array([random.random()*10, random.random()*10, random.random()*10])

class ClassFruts:

    def training():

        
        learn = True
        out   = float(2.5)
        epoch = 0

        while learn:
    
            learn = False
            epoch += 1
            print(" Training: ", epoch, " wight -----> ", wight)

            for i in range(len(data)):

                #Neuron
                Sum = data[i][0] * wight[0] + data[i][1] * wight[1] + wight[2]

                #Activation Step Function 
                if Sum > 0:
                    out = 1
                else: out =0

                if out != data[i][2]:
                    wight[0] = random.random() * 10 - random.random() * 10
                    wight[1] = random.random() * 10 - random.random() * 10
                    wight[2] = random.random() * 10 - random.random() * 10
                    learn = True

    file  = open("wight_Frutas.txt", "w")
    ######## Wight Save ##########
    file.write(str(wight[0]) + "\n" + str(wight[1]) + "\n" + str(wight[2]))
    file.close()
   

    def read():

        file = open("wight_Frutas.txt","r")
        wightFile = file.read()
        file.close()
        print(" In Data ")
        wightGet = []

        for p in wightFile.split("\n"):
            wightGet.append(float(p))

        x1 = float(input("Intoduce color: "))
        x2 = float(input("Intoduce peso:  "))

        SumNet = x1 * wight[0] + x2 * wight[1] + wight[2]

        #Activation function
        if SumNet > 0:
            out1 = "Sandia"
        else: out1 ="Manzana"

        print("{}, {} = {}".format(x1,x2,out1))


ClassFruts.training()
ClassFruts.read()


