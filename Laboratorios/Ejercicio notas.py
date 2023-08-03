import numpy as np

print("---------------------------------------------------------------------------")
materia=str(input("Ingrese una materia: "))
Materia_solicitada=[]
while materia.upper() !="FIN":
    Materia_solicitada.append(materia)
    materia=str(input("Ingrese una materia: "))
print("---------------------------------------------------------------------------")
Porcentajes=[]
for i in Materia_solicitada:
    Porcentaje=int(input("Ingrese un porcentaje para la evaluacion de "+str(i)+" "))
    Porcentajes.append(Porcentaje)
print("---------------------------------------------------------------------------")
nombre=str(input("Ingrese un nombre de alumno: "))
nombres=[]
while nombre.upper() !="FIN":
    nombres.append(nombre)
    nombre=str(input("Ingrese un nombre de alumno: "))
matriz=np.zeros((len(Materia_solicitada),len(nombres)))
print("---------------------------------------------------------------------------")
for i in Materia_solicitada:
    print("Ingrese notas para ",i)
    for j in nombres:
        nota=float(input("Ingrese un nota para "+j+": "))
        matriz[Materia_solicitada.index(i),nombres.index(j)]=nota  
print("---------------------------------------------------------------------------")
for i in range(len(Materia_solicitada)):
    maximo=0
    alumno=""
    print("La mejor nota en la evaluacion de "+Materia_solicitada[i]+"fue :")
    for k in range(len(nombre)):
        if matriz[i,k]>maximo:
            maximo=matriz[i,k]
            alumno=nombres[k]
    print("Alumno: ",alumno)
    print("nota: ",maximo)
print("---------------------------------------------------------------------------")

#mejores notas generales
notamax=0
for i in range(len(Materia_solicitada)):
    for z in range(len(nombres)):
        if matriz[i,z]>notamax:
            notamax=matriz[i,z]

for i in range(len(Materia_solicitada)):
    for k in range(len(nombres)):
        if matriz[i,k]==notamax:
            print("La mejora nota corresponde a la materia de ",str(Materia_solicitada[i])," de ",str(nombres[k]),"con un "+str(notamax))
bestprom=0
for i in range(len(nombres)):
    for j in range(len(Materia_solicitada)):
        
        
print("El mejor promedio corresponde a :",bestprom," que es de ",al)