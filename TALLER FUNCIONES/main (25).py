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

#Retorna una lista con las palabras iniciales con la letra que pasa por parametro  
"""
Entradas:
lista-list-->lista
Salidas
lista-list-->lista
"""  

def letra(lista):
    aux=[]
    for i in lista:
        aux.append(i)
    return aux

