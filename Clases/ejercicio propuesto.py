"""1. Comprobar si una cadena contiene exactamente cinco caracteres
(arbitrarios)
2. Comprobar si una cadena contiene al menos un espacio
3. Compruebe si la cadena "12345" comienza con 1
4. Compruebe si una cadena contiene x al menos tres veces al mismo
tiempo.
5. principio y/o al final. Por ejemplo, las siguientes cadenas
6. satisfacer el desiderátum: "x....xx", "xx....x", "xxxx..."."""
cadena1="12345xxx.....xxxxx2x3x3xsdx4"
print(cadena1.startswith("1"))
print(len(cadena1)==5)
print(cadena1.find(" "))
if cadena1.startswith("xxx")==True or cadena1.endswith("xxx")==True:
    print("Al inicio o final")
elif  cadena1.find("xxx")!=-1:
    print("Entremedio del texto")

print(cadena1.strip("x")) #buscara todas las x independientemenet de si son 3 juntas o separadas
#ademas el punto hace que se detenga toda la busqueda desde el lado izquierdo, o el 4 impide uqe se elimine un lado izquierda ya que
#elimina los elementos de corrido
print(cadena1.lstrip("x"))



print(" ");print("Ejercicio propuesto 2")

#la triple comilla permite que se pueda hacer espaciosentre el texto que se este escribienod y la comilla simplem no lo permite
chain_a = """SSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKM
FCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVV
RRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFR
HSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILT
IITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKG
EPHHELPPGSTKRALPNNT"""

"""1. ¿Cuál es el largo secuencia? (¡Sin caracteres especiales!)
2. Cree una nueva secuencia de variables con todas las líneas nuevas eliminadas.
3. ¿Cuántas cisteínas "C" e histidinas "H" hay en la secuencia?
4. ¿La cadena contiene la subsecuencia "NLRVEYLDDRN"? ¿Dónde?
5. ¿Cómo puedo usar find() y los operadores de extracción de subcadenas [i:j] para extraer la primera línea de chain_a?"""

contar=0; cadena_limpia=""
for i in chain_a:  
    if i!="\n":
        cadena_limpia+=str(i)
print("El largo es de : ",str(len(cadena_limpia)))
print("Existen ",cadena_limpia.count("C")," C")
print("Existen ",cadena_limpia.count("H")," H")
print("La secuencia NLRVEYLDDRN se encuentra en la posicion" ,cadena_limpia.find("NLRVEYLDDRN"))
print("la primera linea es: ",chain_a[0:chain_a.find("\n")])
print(cadena_limpia[0:106])#lo dejo hasta 1 valor antes de encontrar la secuencia solicitada, por lo cual para 
#grandes cadenas de texto solo guarda la ultima posicion



#Ejercicio 2
translation_of = {"a": "ade", "c": "cyt","g": "gua", "t": "tym"}
L = ["A", "T", "T", "A", "G", "T", "C"]

Cadena="\"";valores=list(translation_of.values());llave=list(translation_of.keys())

for i in range(len(L)):
    if L[i].lower() in  llave:
        if i<len(L)-1:
            Cadena+= str(valores[llave.index(L[i].lower())])+" "
        else:
             Cadena+= str(valores[llave.index(L[i].lower())])
print(Cadena+"\"")

"""en la cadena:
"ade tym tym ade gua tym cyt"""

lista="bim"
for z in lista:
    print(z,end=".")
print("  ")



#Ejercicio propuesto ciclo FOR
"""Dada una lista L de enteros, imprima los índices de un par de valores
cuya suma es igual a 17. Ejemplo: Si L=[3,7,12,10,8,32,7,5], escr}iba 2,7 o 1,3
porque L[2]+L[7]=17 y L[1]+L[3]=17.  """
L=[3,7,12,10,14,32,7,5];L2=[]
dic={}
#FORMA 1
for i in L:
    for k in L:
        if i+k==17 and k not in L2:
            print("los valores sumados que dan 17 son: ",i," ",k) ; L2.append(k); L2.append(i)

#FORMA 2
print(" ")
#[ i for i in L for k in L if i+k==17 ]
#listas de comprehension se pueden usar como filtros o 


"""#Dada la lista de cadenas que representan (parte de) la estructura 3D de una
cadena proteica, calcule una lista de listas que contengan, para cada residuo
(es decir, para cada fila de átomos), sus coordenadas."""

"el texto se encuentra en foto pasar despues"


"""1.Dado un número n, imprima todas las posibles formas de obtenerlo como
productos de dos enteros. Presta atención a las repeticiones
conmutativas. (por ejemplo, 4x9 y 9x4). No incluya repeticiones
conmutativas.
2.Dada una lista de valores, generar la sublista de valores que solo
aparecen una vez en la lista. Por ejemplo, L = [1,3,2,3,5,4,5,3,3] debería
generar [1, 2, 4].
3. Dada una lista de valores, potencialmente con valores repetidos, generar
una sublista ordenada de valores donde se eliminan los valores
repetidos. Por ejemplo, L = [1,3,2,3,5,4,5,3,3] debería generar L= [1,2,3,4,5]
4. Dadas dos li9stas de valores (sin repeticiones), generar la sublista de
valores que aparecen en ambos."""

L = [1,3,2,3,5,4,5,3,3]
diccionario={i:0 for i in L}
for i in L:
    diccionario[i]+=1
print([i for i,k in diccionario.items() if k==1 ])
#3
L1=([i for i in diccionario.keys()]); l2=[7,8,9,0,10,1,2,3,4,5]
print([i for i in L1 if i in l2]) ; print([i for i in L1 for k in l2 if i ==k])

print("""\nSudoku""")
#Diccionario
import numpy as np

sudoku=([[1,2,3,4,5,6,7,8,9],
         [4,5,6,7,8,9,1,2,3],
         [7,8,9,1,2,3,4,5,6],
        [2,3,4,5,6,7,8,9,1],
        [5,6,7,8,9,1,2,3,4],
        [8,9,1,2,3,4,5,6,7],
        [3,4,5,6,7,8,9,1,2],
        [6,7,8,9,1,2,3,4,5],
        [9,1,2,3,4,5,6,7,8]])
suma=sum([1,2,3,4,5,6,7,8,9])

for i in range(9):
    suma2=0;suma3=0
    for k in range(9):
        suma2+=sudoku[i][k]
        suma3+=sudoku[k][i]
    if suma2==suma and suma==suma3 :
        continue
    else:
        print("El sudoku esta incorrecto")
        break


import matplotlib.pyplot as plt
import numpy as np
fig, ax=plt.subplots()
ax.fill_between([1,2,3,4],[1,2,0,0.5])
plt.show()

x=np.random.normal(5,1.5,size=1000)
fig, ax=plt.subplots()
ax.hist(x,np.arange(0,11))
plt.show()

fig, ax=plt.subplots()
ax.pie([13,4,5,5,6])
plt.show()

fig, ax=plt.subplots()
ax.boxplot([1,2,1,2,3,4,5,44,4,3,2])
plt.show()

fig, ax=plt.subplots()
ax.violinplot([1,2,1,2,3,4,5,44,4,3,2])
plt.show()


fig, ax=plt.subplots()
x=np.linspace(-3.0,3.0,100)
y=np.linspace(-3.0,3.0,100)
x,y = np.meshgrid(x,y)
z=np.sqrt(x**2+2*y**2)
ax.contourf(x,y,z)
plt.show()

#mapas de calor
#imshow es una cuadricula en basea a cantidad de datos
fig, ax=plt.subplots()
x=np.random.random((16,16))
ax.imshow(x)
plt.show()

fig, ax=plt.subplots()
x,y= np.random.multivariate_normal(mean=[0.0,0.0], cov=[[1.0,0.4],[0.4,0.5]], size=1000).T
ax.hist2d(x,y)
plt.show()
