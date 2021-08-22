a=float(input("Digite el valor de su sueldo: "))
d1=float(input("Valor de ventas departamento #1: "))
d2=float(input("Valor de ventas departamento #2: "))
d3=float(input("Valor de ventas departamento #3: "))
t=(d1+d2+d3)
td1=((d1*100)/t)
td2=((d2*100)/t)
td3=((d3*100)/t)

b=((a*0.20)+a)
if(td1>33.3):
  print(("Departamento #1 ")+str(b))
elif(td2>33.3):
  print(("Departamento #2 ")+str(b))
elif(td3>33.3):
  print(("Departamento #3 ")+str(b))