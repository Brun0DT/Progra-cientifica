import pandas as pd;         import time;         import matplotlib.pyplot as plt;      import psutil
inicio_memoria = psutil.virtual_memory().used;    tiempo_inicio=time.time()


data=pd.read_csv("UNI_CORR_500_01.txt", skiprows=3,sep="\t") #names= cuando la tabla no tiene un encabezado 
data["xpixel"]=round((data["X"])*35.6)+320
data["ypixel"]=round(data["Y"]*(-96))+480
fig, ax=plt.subplots()
ax.hist2d(data["xpixel"],data["ypixel"],bins=(60,50),cmap="inferno")
ax.set_title('Mapa de calor experimento 1', loc = "center")
ax.set_xlabel("Largo pasillo")
ax.set_ylabel("Ancho pasillo")

#EGUNDO text
data=pd.read_csv("UNI_CORR_500_06.txt", skiprows=3,sep="\t") #names= cuando la tabla no tiene un encabezado 
fig, ax=plt.subplots()
data["xpixel"]=round((data["X"])*35.6)+320
data["ypixel"]=round(data["Y"]*(-96))+480
ax.hist2d(data["xpixel"],data["ypixel"],bins=(60,50),cmap="inferno",)
ax.set_title('Mapa de calor experimento 6', loc = "center")
ax.set_xlabel("Largo pasillo")
ax.set_ylabel("Ancho pasillo")

fin_memoria = psutil.virtual_memory().used;           fin_tiempo = time.time()
plt.show()
plt.show()

tiempo_transcurrido = fin_tiempo - tiempo_inicio
print("Tiempo de ejecución: ",tiempo_transcurrido*1000," milisegundos")
memoria_utilizada = fin_memoria - inicio_memoria
print("Memoria utilizada: ", memoria_utilizada/ (1048576)," MB")

