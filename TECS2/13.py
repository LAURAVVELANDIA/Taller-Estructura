d=float(input("Digite un valor: "))
cienmil=(d/100000)
cincuentamil=((d%100000)/50000)
veintemil=((d%50000)/20000)
diezmil=((d%20000)/10000)
cincomil=((d%10000)/5000)
dosmil=((d%5000)/2000)
mil=((d%2000)/1000)

qup=((d%1000)/500)
dop=((d%500)/200)
cip=((d%200)/100)
p=((d%100)/50)

print(("De billetes de 100.000 son: ")+str(cienmil))
print(("De billetes de 50.000 son: ")+str(cincuentamil))
print(("De billetes de 20.000 son: ")+str(veintemil))
print(("De billetes de 10.000 son: ")+str(diezmil))
print(("De billetes de 5.000 son: ")+str(cincomil))
print(("De billetes de 2.000 son: ")+str(dosmil))
print(("De billetes de 1.000 son: ")+str(mil))
print(("De monedas de 500 son: ")+str(qup))
print(("De monedas de 200 son: ")+str(dop))
print(("De monedas de 100 son: ")+str(cip))
print(("De monedas de 50 son: ")+str(p))