import numpy as np
import random
import os

#Datos
data  = np.array([[0.7, 3, 0, 0],[1.5, 5, 0, 0],[2.0, 9, 0, 1],[0.9, 11, 0, 1],[4.2, 0, 1, 0],[ 2.2, 1, 1, 0],[3.6, 7, 1, 1],[4.5,6, 1, 1]])
#dataTrain = np.array([[0, 0, 0, 0],[0, 1, 0, 1],[1, 0, 1, 0],[1, 1, 1, 1]])


class Biblioteca:
    
    #StepFunction
    def StepFunc(Sum):
        if Sum > 0:
           out = 1
        else: out =0
        return out


    def Train(dataIN):

        LRate = 0.3
        file  = open("wights_Biblioteca.txt", "w")
        learn   = True
        epoch   = 0

        #wight for neuron one and two
        """ Cuatro pesos de entrada para cada neurona, más el peso del "bias" """
        wight1 = np.array([random.random()*10, random.random()*10, random.random()*10, random.random()*10, random.random()*10])
        wight2 = np.array([random.random()*10, random.random()*10, random.random()*10, random.random()*10, random.random()*10])


        while (learn):
    
            learn = False
            epoch += 1
            print(" Training: ", epoch, " wight1 -----> ", wight1, " wight2----> ",wight2)

            for i in range(len(data)):

                #Neuron_1
                """  """
                Sum = dataIN[i][0] * wight1[0] + dataIN[i][1] * wight1[1] + dataIN[i][0] * wight1[2]+ dataIN[i][1] * wight1[3] + wight1[4]
                out = Biblioteca.StepFunc(Sum) 
                E1=data[i][2]-out

                #Neuron_2
                Sum2 = dataIN[i][0] * wight2[0] + dataIN[i][1] * wight2[1] + dataIN[i][0] * wight2[2] + dataIN[i][1] * wight2[3] + wight2[4]
                out2 = Biblioteca.StepFunc(Sum2)
                E2=data[i][3]-out2

                print("Error_1------> ", E1, "Error_2------> ",E2)
         
                if E1 != 0:
                    wight1[0]+=LRate*E1*dataIN[i][0]
                    wight1[1]+=LRate*E1*dataIN[i][1]
                    wight1[2]+=LRate*E1*dataIN[i][0]
                    wight1[3]+=LRate*E1*dataIN[i][1]
                    wight1[4]+=LRate*E1
                    learn  = True

                if E2 != 0:
                    wight2[0]+=LRate*E2*dataIN[i][0]
                    wight2[1]+=LRate*E2*dataIN[i][1]
                    wight2[2]+=LRate*E2*dataIN[i][0]
                    wight2[3]+=LRate*E2*dataIN[i][1]
                    wight2[4]+=LRate*E2
                    learn  = True


        print("\n------------End Train---------------\n")

        ######## Wight Save ##########
        file.write(str(wight1[0]) + "\n" + str(wight1[1]) + "\n" + str(wight1[2]) + "\n" + str(wight1[3]) + "\n" + str(wight1[4]) 
          + "\n" + str(wight2[0]) + "\n" + str(wight2[1]) + "\n" + str(wight2[2]) + "\n" + str(wight2[3]) + "\n" + str(wight2[4]))
        file.close()

        return wight1,wight2



                    
    def Test(wight_1, wight_2):

        print("\n<<<------------IN TEST----------->>>\n")
        Train = "1"

        while Train == "1":

            x1 = float(input("Intoduce el peso: "))
            x2 = float(input("Intoduce la frec. de uso: "))

            SumNet  = x1 * wight_1[0] + x2 * wight_1[1] + x1 * wight_1[2] + x2 * wight_1[3] + wight_1[4]
            Out_1 = Biblioteca.StepFunc(SumNet)

            SumNet2 = x1 * wight_2[0] + x2 * wight_2[1] + x1 * wight_2[2] + x2 * wight_2[3] + wight_2[4]
            Out_2 = Biblioteca.StepFunc(SumNet2)
            print("\nResultado: ")
            if(Out_1==Out_2):
              if(Out_1==0):
                print(" Ligero y poco usado")
              else: print("Pesado y muy usado \n")
            elif(Out_1==0):
              print(" Ligero y muy usado")
            else: print("Pesado y poco usado \n")

            print("{}, {}, = {}, {}".format(x1,x2,Out_1,Out_2),"\n")

            Train = input("¿Introducir datos de nuevo? (SÍ = 1 / NO = 2)\n")

    
    def read():

        print("\n<<<------------IN READ----------->>>\n")
        file = open("wights_Biblioteca.txt","r")
        wightFile = file.read()
        file.close()
        wightGet = []

        Train = "1"
        while Train == "1":

          for p in wightFile.split("\n"):
              wightGet.append(float(p))


          x1 = float(input("Intoduce el peso: "))
          x2 = float(input("Intoduce la frec. de uso: "))

          SumNet  = x1 * wightGet[0] + x2 * wightGet[1] + x1 * wightGet[2] + x2 * wightGet[3] + wightGet[4]
          Out_1 = Biblioteca.StepFunc(SumNet)

          SumNet2 = x1 * wightGet[5] + x2 * wightGet[6] + x1 * wightGet[7] + x2 * wightGet[8] + wightGet[9]
          Out_2 = Biblioteca.StepFunc(SumNet2)

          print("\nResultado: ")
          if(Out_1==Out_2):
            if(Out_1==0):
              print(" Ligero y poco usado")
            else: print("Pesado y muy usado \n")
          elif(Out_1==0):
            print(" Ligero y muy usado")

          else: print("Pesado y poco usado \n")
          print("{}, {}, = {}, {}".format(x1,x2,Out_1,Out_2),"\n")
          Train = input("\n¿Introducir datos de nuevo? (SÍ = 1 / NO = 2)\n")
          