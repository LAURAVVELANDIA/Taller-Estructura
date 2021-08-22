a=int(input("Ingrese el valor de A: "))
b=int(input("Ingrese el valor de B: "))
c=int(input("Ingrese el valor de C: "))
d=((b**2)-4*a*c)

if(d==0):
  print("Se debe utilizar: X1=X2=-B/(2*a)")
elif(d>0):
  print("Se debe hacer uso de: 1).X1=(-B+SQRT(B**2-4*a*c))/(2**a)      2). X2=(-B-SQRT(B**2-4*a*c))/(2*a)")
elif(d<0):
  print("No tiene solución en los Reales")