nombre=str(input("Digite su nombre: "))
m=float(input("Digite el valor de su compra: "))
a=(m-(m*0.05))
b=(m-(m*0.11))
c=(m-(m*0.18))
d=(m-(m*0.25))
if(m<=50000):
  print("No aplica descuento")
elif(m>50000 and m<=100000):
  print(("Descuento de 5%, ")+str(a))
elif (m>=101000 and m<=700000):
  print(("Descuento de 11%, ")+("Valor a pagar: ")+str(b))
elif(m>700000 and m<=1500000):
  print(("Descuento de 18%, ")+str(c))
elif(m>1500000):
  print(("Descuento de 25%, ")+str(d))
print(("Cliente:")+str(nombre))
print(("Monto de la compra: ")+str(m))