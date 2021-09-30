
#### Libraries ####
import random
import numpy as np
import os

######  Data_OR  #########
data  = np.array([[0,0,0],[0,1,1],[1,0,1],[1,1,1]])
wight = np.array([random.random()*10, random.random()*10, random.random()*10])
learn = True
out   = float(2.5)
epoch = 0
file  = open("wight_OR.txt", "w")

#########  Training  ##########
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
           
   
print("\n")



############## Neuoron test ###############
"""
for i in range(len(data)):
    
    Sum = data[i][0] * wight[0] + data[i][1] * wight[1] + wight[2]

    if Sum > 0:
        out = 1
    else: out = 0
    print(" In(1):", data2[i][0], " In(2)",data[i][1], "=", data[i][2], "------> Out = ", out, )"""




######## Wight Save ##########
file.write(str(wight[0]) + "\n" + str(wight[1]) + "\n" + str(wight[2]))
file.close()
print("\n")

####### Read file ###########
class readData:
    
    def read():
        file = open("wight_OR.txt","r")
        wightFile = file.read()
        file.close()
        wightGet = []

        for p in wightFile.split("\n"):
            wightGet.append(float(p))


        x1 = int(input("Intoduce In_1: "))
        x2 = int(input("Intoduce In_2: "))

        SumNet = x1 * wightGet[0] + x2 * wightGet[1] + wightGet[2]

        #Activation function
        if SumNet > 0:
            out1 = 1
        else: out1 =0

        print("{}, {} = {}".format(x1,x2,out1))

readData.read()






 