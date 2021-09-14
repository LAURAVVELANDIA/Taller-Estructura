frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in frutas:
    lista_frutas.append(i)
print(lista_frutas)
for i in numeros:
    lista_numeros.append(float(i))
print(lista_numeros)

#Realizar una funcion que elimine un caracter de todos los elementos de la lista
"""
Entradas:
lista-->list-->lista
Salidas:
lista-->lista
"""

def eliminar_un_caracter_de_toda_la_lista(lista,elemento):
    auxiliar=[]
    for i in lista:
     a=i.replace(elemento,"")
     auxiliar.append(a)
    return auxiliar