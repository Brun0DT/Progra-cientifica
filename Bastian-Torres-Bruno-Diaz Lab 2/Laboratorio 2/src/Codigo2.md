#Codigo para medir el tiempo de ejecición
import time
import matplotlib.pyplot as plt
import psutil
inicio_memoria = psutil.virtual_memory().used
tiempo_inicio=time.time()

#Listas para almacenar metros pasados a pixeles
PixelX = []
PixelY = []
PixelesXY =[]
#####################################################################################################
#Definiciones para transformar metro a pixel 
def traspasoX (metro):
    pixel = ((metro+9.0)*(640/18))
    PixelX.append(int(pixel))
    
def traspasoY (metro):
    pixel = 480-(metro*(480/5))
    PixelY.append(int(pixel))

################################################################################################################

#Lectura y almacenamiento de coordenadas
import numpy as np
Crd =[]
X = []
Y = []
XY = []

UNI = open('UNI_CORR_500_01.txt', 'r')
for line in UNI.readlines():
    extrae = line[0:29]
    aux = extrae.split()
    Crd.append(aux)
UNI.close()

for n in range (5,len(Crd)):
    ListaAux = Crd[n]
    a=[]
    AuxX = ListaAux [2]
    AuxY = ListaAux [3]
    AuxZ = ListaAux [4]
    X.append(float(AuxX))
    Y.append(float(AuxY))
    a.append(float(AuxX))
    a.append(float(AuxY))
    XY.append(str(a))
    
#Creación de diccionarios    
DicX = {i:0 for i in X} ; DicY = {i:0 for i in Y} ; DicXY = {i:0 for i in XY}

#Almacenamiento de repeticiones por variable en diccionarios
for i in range(len(X)):
    DicX[X[i]]+=1 ; DicY[Y[i]]+=1 ; DicXY[XY[i]]+=1

#Definicion de repeticiones maximas para cada grupo
MaxX = max(DicX.values()) ; MaxY = max(DicY.values()) ; MaxXY = max(DicXY.values())

#Impresión de datos solicitados
print("La(s) coordenadas X que más se repite(n):", [i for i in DicX.keys() if DicX[i] == MaxX],"con un recuento de",MaxX,"oportunidades")
print("La(s) coordenadas Y que más se repite(n):", [i for i in DicY.keys() if DicY[i] == MaxY],"con un recuento de",MaxY,"oportunidades")
print("La(s) coordenadas X,Y que más se repite(n):", [i for i in DicXY.keys() if DicXY[i] == MaxXY],"con un recuento de",MaxXY,"oportunidades")


#Traspaso de pixeles X e Y a lista en formato "X-Y"
for i in range(len(X)):
    traspasoX(X[i])
    traspasoY(Y[i])
    
    XYp = []
    XYp.append(PixelX[i])
    XYp.append(PixelY[i])
    string = str(XYp[0])+"-"+str(XYp[1])
    PixelesXY.append(string)
    
#Traspaso de lista de pixeles "X-Y" a diccionario con conteo de repeticiones
DicPixXY = {i:0 for i in PixelesXY}
for i in range(len(PixelesXY)):
    DicPixXY[PixelesXY[i]]+=1 

#Traspaso de diccionario "X-Y" a matriz en base a las repeticiones
Matrix=np.zeros((481,641))
for i in DicPixXY.keys():
    xp, yp = i.split("-")
    col = int(xp)  
    fil = int(yp)  
    Matrix[fil][col] = DicPixXY[i]
    
#Generacion de mapa de calor en base a la matriz
import matplotlib.pyplot as plt
plt.imshow(Matrix, cmap='hot', interpolation='nearest')
plt.colorbar()
#Calculo e impresion de las varianzas para datos X e Y
print("La varianza para la coordenadas del eje x son: ",np.var(X),"\nLa varianza para la coordenadas del eje y son: ",np.var(Y)); print("|","-"*147,"|")

#Calculo de tiempo utilizado
fin_tiempo = time.time()
tiempo_transcurrido = fin_tiempo - tiempo_inicio
fin_memoria = psutil.virtual_memory().used
memoria_utilizada = fin_memoria - inicio_memoria
print(f"Tiempo de ejecución: {tiempo_transcurrido*1000} segundos")

# Cálculo de la memoria utilizada
fin_memoria = psutil.virtual_memory().used
memoria_utilizada = fin_memoria - inicio_memoria
print(f"Memoria utilizada: {memoria_utilizada/ float(1048576)} bytes")

#Impresion de mapa de calor
plt.show()