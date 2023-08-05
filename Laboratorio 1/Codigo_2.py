import time
import matplotlib.pyplot as plt
import psutil
inicio_memoria = psutil.virtual_memory().used
tiempo_inicio=time.time()

PixelX = []
PixelY = []

def traspasoX (metro):
    pixel = ((metro+9.0)*(640/18))
    PixelX.append(int(pixel))
    
def traspasoY (metro):
    pixel = 480-(metro*(480/5))
    PixelY.append(int(pixel))

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

DicX = {i:0 for i in X} ; DicY = {i:0 for i in Y} ; DicXY = {i:0 for i in XY}


for i in range(len(X)):
    DicX[X[i]]+=1 ; DicY[Y[i]]+=1 ; DicXY[XY[i]]+=1

#Optimización
MaxX = max(DicX.values()) ; MaxY = max(DicY.values()) ; MaxXY = max(DicXY.values())

    
#print("La(s) coordenadas X que más se repite(n):", [i for i in DicX.keys() if DicX[i] == MaxX],"con un recuento de",MaxX,"oportunidades")
#print("La(s) coordenadas Y que más se repite(n):", [i for i in DicY.keys() if DicY[i] == MaxY],"con un recuento de",MaxY,"oportunidades")
#print("La(s) coordenadas X,Y que más se repite(n):", [i for i in DicXY.keys() if DicXY[i] == MaxXY],"con un recuento de",MaxXY,"oportunidades")


PixelesXY =[]

for i in range(len(X)):
    traspasoX(X[i])
    traspasoY(Y[i])
    
    XYp = []
    XYp.append(PixelX[i])
    XYp.append(PixelY[i])
    string = str(XYp[0])+"-"+str(XYp[1])
    PixelesXY.append(string)
    
DicPixXY = {i:0 for i in PixelesXY}
for i in range(len(PixelesXY)):
    DicPixXY[PixelesXY[i]]+=1 

Matrix=np.zeros((481,641))
for i in DicPixXY.keys():
    xp, yp = i.split("-")
    col = int(xp)  #estos se podrian cambiar
    fil = int(yp)  ##
    Matrix[fil][col] = DicPixXY[i]
    
import matplotlib.pyplot as plt
plt.imshow(Matrix, cmap='hot', interpolation='nearest')
plt.colorbar()
fin_memoria = psutil.virtual_memory().used
fin_tiempo = time.time()
plt.plot()
print("La varianza para la coordenadas del eje x son: ",np.var(X),"\nLa varianza para la coordenadas del eje y son: ",np.var(Y)); print("|","-"*147,"|")

# Calculo del tiempo utilizado
tiempo_transcurrido = fin_tiempo - tiempo_inicio
print("Tiempo de ejecución: ",tiempo_transcurrido*1000," milisegundos")

# Cálculo de la memoria utilizada
memoria_utilizada = fin_memoria - inicio_memoria
print("Memoria utilizada: ", memoria_utilizada/ float(1048576)," MB")