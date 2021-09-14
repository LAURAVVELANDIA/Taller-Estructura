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
#Retornar una lista con los numero negativos  
"""
Entradas:
Salidas
"""  

def numeros_negativos(lista):
  for i in lista:
   c = 0 
   for numeros in lista:
       if numeros <= 0:
           c += 1 
   return c

