import random
import numpy as np
import os

datos = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
datosTrain = np.array([[0, 0], [0,1], [1, 0], [1, 1]])


pesos1=np.array([random.random()*10,random.random()*10,random.random()*10,random.random()*10])
bias=np.array([random.random()*10,random.random()*10])
aprendiendo=True
salida1=0
salida2=0
epoca=0
tasaAprendizaje=0.3
archivo = open("pesosNOTMono.txt", "w")

#fase de entrenamiento
while aprendiendo:

    aprendiendo = False


    for i in range(len(datos)):

        sumaNeta1=datos[i][0]*pesos1[0]+datos[i][1]*pesos1[1]+bias[0]

        sumaNeta2=datos[i][0]*pesos1[2]+datos[i][1]*pesos1[3]+bias[1]


        if sumaNeta1>0:
            salida1=1
        else: salida1=0
        if sumaNeta2>0:
            salida2=1
        else: salida2=0
        error1=datosTrain[i][0]-salida1
        error2=datosTrain[i][1]-salida2
        

        if error1!=0:    
            pesos1[0]+=tasaAprendizaje*error1*datos[i][0]
            pesos1[1]+=tasaAprendizaje*error1*datos[i][1]
            bias[0]+=tasaAprendizaje*error1 
            aprendiendo=True
        if error2!=0:    
            pesos1[2]+=tasaAprendizaje*error2*datos[i][0]
            pesos1[3]+=tasaAprendizaje*error2*datos[i][1]
            bias[1]+=tasaAprendizaje*error2 
            aprendiendo=True    
    print("entrenando")
    epoca+=1
    
#validando que haya quedado entrenada la red
for i in range(len(datos)):
    sumaNeta1=datos[i][0]*pesos1[0]+datos[i][1]*pesos1[1]+bias[0]
    sumaNeta2=datos[i][0]*pesos1[2]+datos[i][1]*pesos1[3]+bias[1]
    if sumaNeta1>0:
        salida1=1
    else: salida1=0
    if sumaNeta2>0:
        salida2=1
    else: salida2=0
    print(datos[i][0],",",datos[i][1],"=",datosTrain[i][0]," ",datosTrain[i][1]," perceptron=",salida1, " ", salida2)

print("epocas: ",epoca)    
for i in range(len(pesos1)):
    print("peso ",(i+1)," =",pesos1[i])
#for i in range(len(pesos2)):
#    print("peso ",(i+1)," =",pesos1[i])
    
#escritura de los pesos en el archivo    
archivo.write(str(pesos1[0])+","+str(pesos1[1])+","+str(bias[0])+","+str(pesos1[2])+","+str(pesos1[3])+","+str(bias[1]))
archivo.close()




#obtener los datos del archivo
archivo=open("pesosNOTMono.txt","r")
pesosArch=archivo.read()
archivo.close()

#obtener los pesos de la cadena pesosArch
pesos1=[]
pesos2=[]
cont=1
for p in pesosArch.split(","):
    if cont<=3:
        pesos1.append(float(p))
    else:
        pesos2.append(float(p))
    cont+=1
#pedir los datos
x1=int(input("Introduce la entrada 1: "))
x2=int(input("Introduce la entrada 2: "))

#resultado del perceptron
sumaNeta1=x1*pesos1[0]+x2*pesos1[1]+pesos1[2]
if sumaNeta1>0:
    salida1=1
else: salida1=0
sumaNeta2=x1*pesos2[0]+x2*pesos2[1]+pesos2[2]
if sumaNeta2>0:
    salida2=1
else: salida2=0
print ("{}, {} = {} {}".format(x1,x2,salida1, salida2))