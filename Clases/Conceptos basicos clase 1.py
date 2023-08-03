print("separacion letras 1");Palabra="whitechocolateespaceeegg";print(Palabra[0:6]);print(Palabra[4:14]);print(Palabra[15:]);print(" ")

print("separacion letras 2");Palabra="abcdefghijklmnopqrst";print(Palabra[::2]);print(Palabra[1::2]);print(Palabra[-1:8:-1]);print(" ")
#palabra[inicio;fin que no incluye esa posicion cuando va al revez cuando va en el orden si la cuenta;cada cuanto avanza]
#empiezan en 0
print("isalpha");a="javaortran";print(a.isalpha());print(" ") #si pongo espacio dara false

print("join");lista=["one","two","three"]; print("-".join (lista));print("\n".join (reversed(lista)));print(" ".join("sos"));print(" ") 
#\n es salto espacio se puede usar como lista o tupla
print("split");lista=("one, and two, and three"); print(lista.split(" "));print(lista.split("and"));print(lista.split(",")) #\n es salto espacio

print("\n");print("tabla simple");nombre="|         Primera tabla       |";lineas="+"+"-"*29+"+"
print(lineas,nombre,lineas,
      "|    Nov 23 1636|          100|",
      "|    Nov 23 1636|          100|",
      "|    Nov 23 1636|          100|",lineas,sep="\n")

print("Representar string");numero=1250000; print("{:5,d}".format(numero));print(" ")
#.pop es para indicar la posicion, si pongo nada elimina el ultimo
print("listas"); lista2=[1,2,3,4];print(lista2); lista2.append(5) ;print(lista2.pop(0));lista3=[5,8,9,7,10];lista2.extend(lista3);print(lista2)
print(sorted(lista2,reverse=True)); lista_auxiliar=lista2[:]

#crear archivo
print("crear archivo")
arch=open("textoprueba.txt","w")
for i in range(1,1001):
    print(i,i**2,i**3,i**4,sep=", ",file=arch)
arch.close

arch=open("textoprueba.txt","r")
cuadrado=[]
cubo=[] 
cuarta=[]

for line in arch.readlines():
    separacion=line.split(",")
    cuadrado.append(separacion[1])
    cubo.append(separacion[2])
    cuarta.append(separacion[3])
arch.close()
n=500
print(" ")
print(n,"al cubo son", cubo[n-1])

palabra="abscdef"
print(palabra[-1:1])

import numpy as np