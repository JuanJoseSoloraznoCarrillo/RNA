import numpy as np
import random
import os

#Datos

#Segmentos del LED (7 segmentos y tres salidas)
data=np.array  ([[1,1,1,1,1,1,0,1,0,0], #0
                 [0,1,1,0,0,0,0,0,1,0], #1
                 [1,1,0,1,1,0,1,1,0,0], #2
                 [1,1,1,1,0,0,1,0,1,0], #3
                 [0,1,1,0,0,1,1,1,0,0], #4
                 [1,0,1,1,0,1,1,0,1,0], #5
                 [1,0,1,1,1,1,1,1,0,0], #6
                 [1,1,1,0,0,0,0,0,1,1], #7
                 [1,1,1,1,1,1,1,1,0,1], #0
                 [1,1,1,1,0,1,1,0,1,1]])#9   #entradas

#Interpretación de la salida
'''
           [[1,0,0], #0 Es par   y menor a 7
            [0,1,0], #1 Es impar y menor a 7
            [1,0,0], #2 Es par   y menor a 7
            [0,1,0], #3 Es impar y menor a 7
            [1,0,0], #4 Es par   y menor a 7
            [0,1,0], #5 Es impar y menor a 7
            [1,0,0], #6 Es par   y menor a 7
            [0,1,1], #7 Es impar y mayor o igual a 7
            [1,0,1], #8 Es par   y mayor o igual a 7
            [0,1,1]])#9 Es impar y mayor o igual a 7  #Salidas
'''

class RedMonocapaLeds:
    ''' Red monocapa para clasificar la salida de un led de siete segmentos ''' 
    #StepFunction
    def StepFunc(Sum):
        if Sum > 0:
           out = 1
        else: out =0
        return out

    def Train(dataIN):
        ''' Recalcula los valores de los pesos '''
        LRate = 0.3
        file  = open("wights_Biblioteca.txt", "w")
        learn   = True
        epoch   = 0

        #wight for neuron one and two
        """ Cuatro pesos de entrada para cada neurona, más el peso del "bias" """
        wight1 = np.array([random.random()*10, 
                           random.random()*10, 
                           random.random()*10, 
                           random.random()*10,
                           random.random()*10, 
                           random.random()*10, 
                           random.random()*10, 
                           random.random()*10])

        wight2 = np.array([random.random()*10,
                           random.random()*10, 
                           random.random()*10,
                           random.random()*10,
                           random.random()*10, 
                           random.random()*10, 
                           random.random()*10, 
                           random.random()*10])

        wight3 = np.array([random.random()*10,
                           random.random()*10, 
                           random.random()*10,
                           random.random()*10, 
                           random.random()*10, 
                           random.random()*10, 
                           random.random()*10, 
                           random.random()*10])

        while (learn):
    
            learn = False
            epoch += 1
            print(" \nTraining: ", epoch,\
                  "\n\n <----------wight1----------> \n",wight1,\
                    "\n <----------wight2----------> \n",wight2,\
                    "\n <----------wight3----------> \n",wight3)

            for i in range(len(data)):

                #Neuron_1
                """  """
                Sum = dataIN[i][0] * wight1[0] \
                    + dataIN[i][1] * wight1[1] \
                    + dataIN[i][2] * wight1[2] \
                    + dataIN[i][3] * wight1[3] \
                    + dataIN[i][4] * wight1[4] \
                    + dataIN[i][5] * wight1[5] \
                    + dataIN[i][6] * wight1[6] + wight1[7]

                out = RedMonocapaLeds.StepFunc(Sum) 
                E1=data[i][7]-out

                #Neuron_2
                Sum2 = dataIN[i][0] * wight2[0] \
                     + dataIN[i][1] * wight2[1] \
                     + dataIN[i][2] * wight2[2] \
                     + dataIN[i][3] * wight2[3] \
                     + dataIN[i][4] * wight2[4] \
                     + dataIN[i][5] * wight2[5] \
                     + dataIN[i][6] * wight2[6] + wight3[7]

                out2 = RedMonocapaLeds.StepFunc(Sum2)
                E2=data[i][8]-out2

                #Neuron_3
                Sum3 = dataIN[i][0] * wight3[0] \
                     + dataIN[i][1] * wight3[1] \
                     + dataIN[i][2] * wight3[2] \
                     + dataIN[i][3] * wight3[3] \
                     + dataIN[i][4] * wight3[4] \
                     + dataIN[i][5] * wight3[5] \
                     + dataIN[i][6] * wight3[6] + wight3[7]

                out3 = RedMonocapaLeds.StepFunc(Sum3)
                E3=data[i][9]-out3

                print("Error_1------> ", E1, "Error_2------> ",E2, "Error_3-------> ",E3)
         
                if E1 != 0:
                    wight1[0]+=LRate*E1*dataIN[i][0]
                    wight1[1]+=LRate*E1*dataIN[i][1]
                    wight1[2]+=LRate*E1*dataIN[i][2]
                    wight1[3]+=LRate*E1*dataIN[i][3]
                    wight1[4]+=LRate*E1*dataIN[i][4]
                    wight1[5]+=LRate*E1*dataIN[i][5]
                    wight1[6]+=LRate*E1*dataIN[i][6]
                    wight1[7]+=LRate*E1
                    learn  = True

                if E2 != 0:
                    wight2[0]+=LRate*E2*dataIN[i][0]
                    wight2[1]+=LRate*E2*dataIN[i][1]
                    wight2[2]+=LRate*E2*dataIN[i][2]
                    wight2[3]+=LRate*E2*dataIN[i][3]
                    wight2[4]+=LRate*E2*dataIN[i][4]
                    wight2[5]+=LRate*E2*dataIN[i][5]
                    wight2[6]+=LRate*E2*dataIN[i][6]
                    wight2[7]+=LRate*E2
                    learn  = True

                if E3 != 0:
                    wight3[0]+=LRate*E3*dataIN[i][0]
                    wight3[1]+=LRate*E3*dataIN[i][1]
                    wight3[2]+=LRate*E3*dataIN[i][2]
                    wight3[3]+=LRate*E3*dataIN[i][3]
                    wight3[4]+=LRate*E3*dataIN[i][4]
                    wight3[5]+=LRate*E3*dataIN[i][5]
                    wight3[6]+=LRate*E3*dataIN[i][6]
                    wight3[7]+=LRate*E3
                    learn  = True

        print("\n------------End Train---------------\n")
        
        return wight1,wight2,wight3

        
    def Test(wight1, wight2, wight3,dataIN):
        ''' Valida el entrenamiento de las neuronas '''
        print("\n<<<------------IN TEST----------->>>\n")
        Train = "1"
        OutGral = []
       
        for i in range(len(data)):
            SumNet =  dataIN[i][0] * wight1[0] \
                    + dataIN[i][1] * wight1[1] \
                    + dataIN[i][2] * wight1[2] \
                    + dataIN[i][3] * wight1[3] \
                    + dataIN[i][4] * wight1[4] \
                    + dataIN[i][5] * wight1[5] \
                    + dataIN[i][6] * wight1[6] + wight1[7]

            Out_1 = RedMonocapaLeds.StepFunc(SumNet)
            

            SumNet2 =  dataIN[i][0] * wight2[0] \
                        + dataIN[i][1] * wight2[1] \
                        + dataIN[i][2] * wight2[2] \
                        + dataIN[i][3] * wight2[3] \
                        + dataIN[i][4] * wight2[4] \
                        + dataIN[i][5] * wight2[5] \
                        + dataIN[i][6] * wight2[6] + wight3[7]
            Out_2 = RedMonocapaLeds.StepFunc(SumNet2)

            SumNet3 =  dataIN[i][0] * wight3[0] \
                        + dataIN[i][1] * wight3[1] \
                        + dataIN[i][2] * wight3[2] \
                        + dataIN[i][3] * wight3[3] \
                        + dataIN[i][4] * wight3[4] \
                        + dataIN[i][5] * wight3[5] \
                        + dataIN[i][6] * wight3[6] + wight3[7]
            Out_3 = RedMonocapaLeds.StepFunc(SumNet3)
            aux = [Out_1,Out_2,Out_3]
            
            OutGral.append(aux)
        
        return OutGral    

    def salida(OutGral):
        '''Interpreta la salida de la red neuronal'''
        print("\nInterpretación de la salida: \n")
        for v in range(len(OutGral)):
            if(OutGral[v][0]==1 and OutGral[v][2]==0):
                print("El número: ",v," Es par   y menor a 7")
            if(OutGral[v][1]==1 and OutGral[v][2]==0):
                print("El número: ",v," Es impar y menor a 7")
            if(OutGral[v][2]==1 and OutGral[v][0]==1):
                print("El número: ",v," Es par   y mayor o igual a 7")
            if(OutGral[v][2]==1 and OutGral[v][1]==1):
                print("El número: ",v," Es impar y mayor o igual a 7")


#Salida

OUT = RedMonocapaLeds.Train(data)

fin = RedMonocapaLeds.Test(OUT[0],OUT[1],OUT[2],data)

for n in fin:
    print(n)

RedMonocapaLeds.salida(fin)