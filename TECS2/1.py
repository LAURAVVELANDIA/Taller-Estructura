a=float(input("Ingrese el valor de su dinero: "))
b=float(input("Que porcentaje de interes (indicar el decimal): "))
c=int(input("Ingrese la cantidad de meses que tiene este dinero en el banco: "))
d=(a*b)
e=(d*c)
if(e>100000):
  print("DEBE REINVERTIR")
else:
  print("NO DEBE REINVERTIR")
