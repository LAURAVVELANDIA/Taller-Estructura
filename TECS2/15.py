a=int(input("Digite el valor de la lectura actual: "))
b=int(input("Digite el valor de la lectura pasada: "))
c=a-b
d=c*4600
e=c*80000
f=c*100000
g=c*120000

if(0<=c<=100):
  print(d)
elif(101<=c<=300):
  print(e)
elif(301<=c<=500):
  print(f)
elif(c>=501):
  print(g)