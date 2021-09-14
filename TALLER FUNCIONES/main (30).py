frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in frutas:
    lista_frutas.append(i)
print(lista_frutas)

#realizar una funcion que agregue al final de archivo frutas una fruta
"""
def frutas(elemento):
    lista.insert(45,"elemento")
    print(lista_frutas)
"""


