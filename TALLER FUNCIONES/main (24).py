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
#Realizar una funcion que elimine un elemento de una lista
"""
Entradas:
lista-list-->lista
elemento-->str-->elemento
Salidas
lista-list-->lista
"""  
def elimina_elemento_lista(lista,elemento):
  lista.remove(elemento)
  return lista




