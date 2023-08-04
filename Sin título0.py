# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 13:50:35 2023

@author: Bruno
"""

def frecuencia(diccionario,COORDENADAS):  
   for i in range(len(COORDENADAS)):
      diccionario[COORDENADAS[i]]+=1
   return diccionario

def impresion(diccionario):
   maximo=max(diccionario.values())
   print("-"*150);print("La coordenada x que mas veces se repite corresponde a: ",[i for i in diccionario.keys() if diccionario[i]== maximo]," con una cantidad de ",maximo)

import numpy as np
arch=open("UNI_CORR_500_01.txt","r")

id=[];  frame=[];  x=[];  y=[];  z=[];  conta=0;  coordenadas=[]

for line in arch.readlines():
    separacion=line.split(); conta+=1
    if conta>=5:
      var2=separacion[4].split("\n");  id.append(separacion[0]);  frame.append(separacion[1]);  x.append(separacion[2]);  y.append(separacion[3]); z.append(var2[0])
      coordenada=str(separacion[2])+","+str(separacion[3]);coordenadas.append(coordenada)
arch.close()

diccionario_x={i:0 for i in x};  diccionario_y={i:0 for i in y};   diccionario_x_e_Y={i:0 for i in coordenadas}

diccionario_x=frecuencia(diccionario_x,x);  diccionario_y=frecuencia(diccionario_y,y);  diccionario_x_e_Y=frecuencia(diccionario_x_e_Y,coordenadas)

impresion(diccionario_x);  impresion(diccionario_y);  impresion(diccionario_x_e_Y)

#tranformacion a pixeles

def Crear_matrices (diccionario,diccionario2):
   matriz=np.zeros([len(x),2])
   lista=[i for i in diccionario.values()]
   lista2=[i for i in diccionario2.values()]
   for i in range(len(lista2)):
      matriz[i,0]=lista[i]
      matriz[i,0]=lista[i]
   return matriz

def transformacion (x,y):
    uniones=[]
    diccionario_uniones={}
    ly=[]
    lx=[]
    
    for i in range(len(x)):
        
        pixely=round(((-96)*float(y[i]))+480);   pixelx=round(float((float(x[i])*35.6)+320))
        
        string=str(pixelx)+"-"+str(pixely)
        lx.append(pixelx)
        ly.append(pixely)
        uniones.append(string)
        
    for  i in uniones:
        
        diccionario_uniones[i]+=1
        
    return recorrer(diccionario_uniones),lx,ly

pixeles=transformacion(x,y)
pixelesy=pixeles[2]
pixelesx=pixeles[1]
matriz_frecuencias=pixeles[0]


def recorrer  (diccionario_uniones):
    Matrix=np.zeros((641,481)) #x,y
    for llave,valor in diccionario_uniones.items():
        keys=llave.split("-")
        fila_X=(int(keys[0]))
        Col_y=(int(keys[1]))
        if fila_X>480:
            Col_y=480
        if Col_y>640:
            fila_X=640
        Matrix[fila_X][Col_y]=valor
    return Matrix

import matplotlib.pyplot as plt

plt.imshow(matriz_frecuencias, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.show()