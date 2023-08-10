import numpy as np
a=np.array([3,4]); b=np.array([[2,2,5],[5,6,7],[3,4,7]])
print("el producto de vectores es", b.trace())

#resolver sistema ecuaciones
#x+2y=1
#3x+5y=2

a=np.array([[1,2],[3,5]])
b=np.array([1,2])

print("las soluciones del sistema ecuaciones son: ")
print(np.linalg.solve(a,b))

import random
a=[random.randint(1,10) for _ in range(10)] # el _ se usa para descartar ya que no buscamos agregar valores a una lista
print(a)

#diccionario={zz:a.count(zz) for zz in range(1,11)}   # asi se hace todo sin utilizar un ciclo for gigante 
diccionario={}
print("           ")
a=[random.randint(1,10) for _ in range(100)]; lista=[]; numero=[a for a in range(1,11)]
for i in range (1,11):
    contar=0
    for k in a:
        if k==i:
            contar+=1
    print("numero ",i,": ",contar," veces")
    diccionario[i]=contar
    lista.append(contar)
#formato de lista
print("El numero que mas veces se repite corresponde a: ",[numero[i] for i in range(len(lista)) if lista[i]==max(lista)]," con un recuento de",max(lista)," veces")
print("El numero que menos veces se repite corresponde a: ", [numero[i] for i in range(len(lista)) if lista[i]==min(lista)]," con un recuento de",min(lista)," veces")
#diccionario
print("El numero que mas veces se repite corresponde a: ",[i for i in range(1,11) if diccionario[i]== max(diccionario.values())]," con un recuento de",max(diccionario.values())," veces")
print("El numero que mas veces se repite corresponde a: ",[i for i in range(1,11) if diccionario[i]== min(diccionario.values())]," con un recuento de",min(diccionario.values())," veces")

import matplotlib.pyplot as plt

#fig, ax=plt.subplots()
#ax.bar([i for i in numero ],[val for i, val in diccionario.items()])
#plt.show()

"""fig, ax=plt.subplots()
ax.boxplot([i for i, val in diccionario.items()])
plt.show()"""

#fig, ax=plt.subplots()
#ax.boxplot([i for i in a])
#plt.show()

#fig, ax=plt.subplots()
#ax.violinplot([i for i in a])
#plt.show()

fig, ax = plt.subplots(2, 2, sharey=False)
ax[0, 0].bar([i for i in numero ],[val for i, val in diccionario.items()], color = 'fireBrick')
ax[0, 1].boxplot([i for i in a])
ax[1, 1].violinplot([i for i in a])
ax[1, 0].plot([i for i in range(10)],diccionario.values())
ax[0,1].set_yticks(sorted(list(diccionario.values())))

plt.show()