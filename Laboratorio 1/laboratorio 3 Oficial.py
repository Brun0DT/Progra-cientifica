#Bastian-Torres-Bruno-Diaz
import numpy as np
import time
import matplotlib.pyplot as plt
import psutil
inicio_memoria = psutil.virtual_memory().used
tiempo_inicio=time.time()
#Funciones 
def frecuencia(diccionario,COORDENADAS):  
   for i in range(len(COORDENADAS)):
      diccionario[COORDENADAS[i]]+=1
   return diccionario

def impresion(diccionario):
   maximo=max(diccionario.values())
   print("|","-"*150,"|");print("La coordenada x que mas veces se repite corresponde a: ",[i for i in diccionario.keys() if diccionario[i]== maximo]," con una cantidad de ",maximo)

def rellenar_Matriz_frec  (diccionario_uniones): # creacion de matriz de frecuencia para datos en pixeles
    Matrix=np.zeros((481,641)) #x,y
    for llave,valor in diccionario_uniones.items():
        keys=llave.split("-");    col_X=(int(keys[1]));      fila_y=(int(keys[0]))
        Matrix[fila_y][col_X]=valor
    return Matrix

def transformacion (x,y): #tranformacion a pixeles
    uniones=[] # se agregara la concatenacion de strings para la coordenadas x e y
    for i in range(len(x)):
        #pixey e pixelx tendran 
        pixely=round(((-96)*float(y[i]))+480);    pixelx=round(float((float(x[i])*35.6)+320))
        uniones.append(str(pixely)+"-"+str(pixelx))
    diccionario_uniones={i:0 for i in uniones} 
    diccionario_uniones=frecuencia(diccionario_uniones,uniones)
    #print(diccionario_uniones)
    return rellenar_Matriz_frec(diccionario_uniones)
"-----------------------------------------------------------------------------------------------------"
#lectura del archivo
arch=open("UNI_CORR_500_01.txt","r");    id=[];    frame=[];    x=[];    y=[];   z=[];   conta=0;    coordenadas=[]

for line in arch.readlines():
    separacion=line.split();   conta+=1
    if conta>=5:
      var2=separacion[4].split("\n");   id.append(separacion[0]);   frame.append(separacion[1]);   z.append(float(var2[0]))
      x.append(float(separacion[2]));   y.append(float(separacion[3]))
      coordenadas.append((str(separacion[2])+","+str(separacion[3])))

arch.close()

#Creacion de diccionarios rellenos de ceros
diccionario_x={i:0 for i in x};     diccionario_y={i:0 for i in y};      diccionario_x_e_Y={i:0 for i in coordenadas}
#obtencion de las frecuencias
diccionario_x=frecuencia(diccionario_x,x)
diccionario_y=frecuencia(diccionario_y,y)
diccionario_x_e_Y=frecuencia(diccionario_x_e_Y,coordenadas)
#Impresion de coordenas mas repetidas con mayor frecuencia obtenida
impresion(diccionario_x);  impresion(diccionario_y);  impresion(diccionario_x_e_Y) ; print("|","-"*150,"|")
print("La varianza para la coordenadas del eje x son: ",np.var(x),"\n La varianza para la coordenadas del eje y son: ",np.var(y)); print("|","-"*150,"|")
print("El Promedio para la coordenadas del eje x son: ",np.mean(x),"\n La varianza para la coordenadas del eje y son: ",np.mean(y)); print("|","-"*150,"|")

#llamada de funciones para transformacion y relleno de matriz frecuencia
pixeles=transformacion(x,y)
matriz_frecuencias=pixeles

#obtenicion de matriz de calor, el eje x corresponde al largo del pasillo, el y al ancho
fig, ax=plt.subplots()
ax.imshow(matriz_frecuencias,cmap="hot")
fin_memoria = psutil.virtual_memory().used
fin_tiempo = time.time()
plt.show()

# Calculo del tiempo utilizado
tiempo_transcurrido = fin_tiempo - tiempo_inicio
print("Tiempo de ejecución: ",tiempo_transcurrido*1000," milisegundos")

# Cálculo de la memoria utilizada
memoria_utilizada = fin_memoria - inicio_memoria
print("Memoria utilizada: ", memoria_utilizada/ float(1048576)," MB")