import pandas as pd;         import time;         import matplotlib.pyplot as plt;      import psutil
inicio_memoria = psutil.virtual_memory().used;    tiempo_inicio=time.time();   import numpy as np
data=pd.read_csv("UNI_CORR_500_01.txt", skiprows=3,sep="\t") #names= cuando la tabla no tiene un encabezado



"----------------------------------------------------------------------------------------------------------------------"


#Velocidad primer txt
def Obtener_velocidad(datax):
    return (((datax["X"].diff(periods=1))**2+(datax["Y"].diff(periods=1))**2)**(1/2))/(1/25)

Dataframe_velocidades = data.groupby("# PersID").apply(Obtener_velocidad) #dataframe_velocidad se convirtio en una serie

data["Velocidad"]=Dataframe_velocidades.values #agrego la serie que tiene propiedad index y value al dataframe original
#en este caso values contiene un total de las filas de datos
print(data)
data=data.dropna(subset=['Velocidad']) #elimino valores none
Dataframe_velocidades = data.groupby("# PersID").apply(Obtener_velocidad)# se crea una serie donde se agrupa por persona y se le agregan los valores de la funcion 
#cada id persona contienen una cantidad de velocidades equivales a los frames donde estuvo

#obtencion de grafico cajas y bigotes primeras 10 personas del primer experimento
fig, ax = plt.subplots()
ax.boxplot([data[(data["# PersID"]==i)]["Velocidad"]  for i in range(1,11)])
ax.set_xlabel('Personas')
ax.set_ylabel('Velocidad')
ax.set_title('Boxplot por persona experimento 01', loc='center')

tabla_experimento1=Dataframe_velocidades.groupby("# PersID").agg(np.mean) #con esto se agrupa el dataset y se comprime todas las
#velocidades obtenidas, calculando solo el promeido
print("Promedio experimento 1: ",tabla_experimento1.mean())
print("Varianza experimento 1: ",tabla_experimento1.var())
print("\n")




"----------------------------------------------------------------------------------------------------------------------"



#velocidad segundo txt
data=pd.read_csv("UNI_CORR_500_06.txt", skiprows=3,sep="\t") #names= cuando la tabla no tiene un encabezado

def obtener_velocidad(datax):
    return (((datax["X"].diff(periods=1))**2+(datax["Y"].diff(periods=1))**2)**(1/2))/(1/25)

Dataframe_velocidades= data.groupby("# PersID").apply(obtener_velocidad) #se agrupa y se asigna el valor de la velocidad por cada frame
#individual
data["Velocidad"]=Dataframe_velocidades.values #se asigna la velocidad de cada linea de coordenada al dataset original
data=data.dropna(subset=['Velocidad']) #paso importante de otra forma el boxplot no arroja imagen
tabla_experimento2=Dataframe_velocidades.groupby("# PersID").agg(np.mean)#se obtiene una seria que almacena la velocidad de cada
#persona en promedio

#obtencion de promedio y varianza
print("Promedio experimento 6: ",tabla_experimento2.mean())
print("Varianza experimento 6: ",tabla_experimento2.var())


#grafico cajas y bigotes experimento 6 primeras 10 personas

fig, ax = plt.subplots()
ax.boxplot([data[(data["# PersID"]==i)]["Velocidad"]  for i in range(1,11)])
ax.set_xlabel('Personas')
ax.set_ylabel('Velocidad')
ax.set_title('Boxplot por persona experimento 06', loc='center')

#grafico cajas y bigotes de personas que ya estan en la cola, 250 al 269
fig, ax = plt.subplots()
ax.boxplot([data[(data["# PersID"]==i)]["Velocidad"]  for i in range(250,270)])
ax.set_xlabel('Personas')
ax.set_ylabel('Velocidad')
ax.set_title('Boxplot por persona experimento 06', loc='center')



"----------------------------------------------------------------------------------------------------------------------"




fig, ax = plt.subplots()
ax.hist(tabla_experimento1,bins=15, color='green', edgecolor='black')
ax.set_xlabel('Velocidad')
ax.set_ylabel('Frecuencia')
ax.set_title('Histograma de Velocidad experimento 1', loc='center')

fig, ax = plt.subplots()
ax.hist(tabla_experimento2,bins=15, color='blue', edgecolor='black')
ax.set_xlabel('Velocidad')
ax.set_ylabel('Frecuencia')
ax.set_title('Histograma de Velocidad experimento 6', loc='center')

fin_memoria = psutil.virtual_memory().used;           fin_tiempo = time.time()
plt.show()
tiempo_transcurrido = fin_tiempo - tiempo_inicio
print("Tiempo de ejecución: ",tiempo_transcurrido*1000," milisegundos")
memoria_utilizada = fin_memoria - inicio_memoria
print("Memoria utilizada: ", memoria_utilizada/ (1048576)," MB")
#distancia euclidiana en un plano bidimensional