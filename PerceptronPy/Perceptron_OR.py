#------ Libraries ------#
import random,os
import numpy as np

#------ Class implementation -----#
class Perceptron(object):
    """
    """

    def __init__(self, file_path=".",train=False):
        """
        """
        if train:
            self.training()

    def read(self):
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

    def training(self):
        DATA   = np.array([[0,0,0],[0,1,1],[1,0,1],[1,1,1]])
        WIGHT = np.array([random.random()*10, random.random()*10, random.random()*10])
        LEARN = True
        OUT = 2.50
        EPOCH = 0
        FILE = open("wight_OR.txt", "w")

        """
        """
        while LEARN:
            LEARN = False
            EPOCH += 1
            print(" Training: ", EPOCH, " wight -----> ", WIGHT)
        
            for i in range(len(DATA)):
        
                #Neuron
                Sum = DATA[i][0] * WIGHT[0] + DATA[i][1] * WIGHT[1] + WIGHT[2]
        
                #Activation Step Function 
                if Sum > 0:
                    out = 1
                else: out =0
        
                if out != DATA[i][2]:
                    WIGHT[0] = random.random() * 10 - random.random() * 10
                    WIGHT[1] = random.random() * 10 - random.random() * 10
                    WIGHT[2] = random.random() * 10 - random.random() * 10
                    LEARN = True
        print("\n")
        
        ######## Wight Save ##########
        FILE.write(str(WIGHT[0]) + "\n" + str(WIGHT[1]) + "\n" + str(WIGHT[2]))
        FILE.close()
        print("\n")

if __name__ == '__main__':
    or_gate = Perceptron()


