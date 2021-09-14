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


#Realizar una funcion que retorne el tamaño de una lista   
"""
Entradas:
Lista->list-->lista
Salidas
tamaño lista
"""   

def tamano_lista(lista):
    contador=0
    while True:
        try:
            lista[contador]
            contador +=1
        except IndexError:
            break
    return

