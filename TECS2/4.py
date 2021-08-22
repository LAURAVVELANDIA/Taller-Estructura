a=float(input("Ingrese el valor de la compra total: "))
b=(a*0.55)
c=(a*0.30)
d=(a*0.15)
x=(d*0.20)

e=(a*0.70)
f=(a*0.30)
w=(f*0.20)
if(a>5000000):
  print(("La empresa pagará: ")+str(b))
  print(("Pedira al banco: ")+str(c))
  print(("El credito con el fabricante sera de: ")+str(d))
  print(("La cantidad por intereses con el fabricante es de: ")+str(x))
else:
  print(("La empresa pagará: ")+str(e))
  print(("El credito con el fabricante sera de: ")+str(f))
  print(("La cantidad por intereses con el fabricante es de: ")+str(w))