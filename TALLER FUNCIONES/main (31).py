frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in frutas:
    lista_frutas.append(i)
print(lista_frutas)
#Realizar una funcion que cuente el numero de veces que se repite un elemento  

def contar_veces(self, elemento, lista):
    veces = 0
    for i in lista:
         if elemento==i:
             veces += 1
    return veces

"""
if __name__ == "__main__":
    nueva=eliminar_un_caracter(lista_numeros,"\n")
    nueva_dos=numeros_pares(nueva)
    print(elimina_elemento_lista(nueva_dos,"10"))
"""

