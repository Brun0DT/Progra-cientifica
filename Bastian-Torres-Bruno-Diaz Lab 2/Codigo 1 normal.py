#Bastian-Torres-Bruno-Diaz
"""# el orden del codigo sera:
1. importacion de librerias
2. Definicion de las variables a utilizar
3. Lectura del archivo 
4. cargado de coordenadas mas frecuentes
5. calculo de promedio y varianza
6. Cargado de matriz de frecuencia
7. creacion de mapa de calor
"""
import numpy as np
import time
import matplotlib.pyplot as plt
import psutil
inicio_memoria = psutil.virtual_memory().used
tiempo_inicio=time.time()

#lectura del archivo
archivo=open("UNI_CORR_500_01.txt","r")

def codigo_principal(arch):
    x=[];    y=[];    conta=0
    for line in arch.readlines():
        separacion=line.split();   conta+=1
        if conta>=5:
            y.append(round((-96)*float(separacion[3]))+480)
            x.append(round(float(separacion[2])*35.6)+320)
    arch.close()
    return x,y  
eje_xy=codigo_principal(archivo)
x=eje_xy[0]
y=eje_xy[1]
fig, ax=plt.subplots()
ax.hist2d(x,y,cmap="hot",bins=150)
ax.set_title('Mapa de calor experimento 1', loc = "center")
ax.set_ylabel("Ancho pasillo")
ax.set_xlabel("Largo pasillo")

archivo=open("UNI_CORR_500_06.txt","r")


eje_xy=codigo_principal(archivo)
x=eje_xy[0]
y=eje_xy[1]
fig, ax=plt.subplots()
ax.hist2d(x,y,cmap="hot",bins=150)
ax.set_title('Mapa de calor experimento 6', loc = "center")
ax.set_ylabel("Ancho pasillo")
ax.set_xlabel("Largo pasillo")

#termino de calculo del tiempo
fin_memoria = psutil.virtual_memory().used
fin_tiempo = time.time()

plt.show()
plt.show()

# Calculo del tiempo utilizado
tiempo_transcurrido = fin_tiempo - tiempo_inicio
print("Tiempo de ejecución: ",tiempo_transcurrido*1000," milisegundos")

# Cálculo de la memoria utilizada
memoria_utilizada = fin_memoria - inicio_memoria
print("Memoria utilizada: ", memoria_utilizada/ float(1048576)," MB")