import pandas as pd
import time
import matplotlib.pyplot as plt
import psutil
inicio_memoria = psutil.virtual_memory().used
tiempo_inicio=time.time()

data=pd.read_csv("UNI_CORR_500_01.txt", skiprows=3,sep="\t") #names= cuando la tabla no tiene un encabezado 
fig, ax=plt.subplots()

#en pixeles
ax.hist2d(round((data["X"])*35.6)+320,round(data["Y"]*(-96))+480,bins=150,cmap="inferno")
fin_memoria = psutil.virtual_memory().used
fin_tiempo = time.time()
plt.show()

# Calculo del tiempo utilizado
tiempo_transcurrido = fin_tiempo - tiempo_inicio
print("Tiempo de ejecución: ",tiempo_transcurrido*1000," milisegundos")

# Cálculo de la memoria utilizada
memoria_utilizada = fin_memoria - inicio_memoria
print("Memoria utilizada: ", memoria_utilizada/ float(1048576)," MB")