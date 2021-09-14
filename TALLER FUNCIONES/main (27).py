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


#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas:
lista-->list-->lista
Salidas
lista-->lista
tipodatos
"""  

def informacion_lista(lista):
  contador=0
  while True:
        try:
            lista[contador]
            contador +=1
        except IndexError:
            break
  return

