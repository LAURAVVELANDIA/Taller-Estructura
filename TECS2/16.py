a=str(input("Indique su sexo: "))
b=int(input("Indique su edad en meses: "))
c=float(input("Indique el nivel de hemoglobina: "))
if(b==0 and b<=1) and (c>=13 and c<=26):
  print("NEGATIVO")
elif(b==0 and b<=1) and (c<13 and c<26):
  print("POSITIVO")

elif(b>1 and b<=6) and (c>=10 and c<=18):
  print("NEGATIVO")
elif(b>1 and b<=6) and (c<10 and c<18):
  print("POSITIVO")

elif(b>6 and b<=12) and (c>=11 and c<=15):
  print("NEGATIVO")
elif(b>6 and b<=12) and (c<11 and c<15):
  print("POSITIVO")

elif(b>12 and b<=60) and (c>=11.5 and c<=15):
  print("NEGATIVO")
elif(b>12 and b<=60) and (c<11.5 and c<15):
  print("POSITIVO")

elif(b>60 and b<=120) and (c>=12.6 and c<=15.5):
  print("NEGATIVO")
elif(b>60 and b<=120) and (c<12.6 and c<15.5):
  print("POSITIVO")

elif(b>120 and b<=180) and (c>=13 and c<=15.5):
  print("NEGATIVO")
elif(b>1120 and b<=180) and (c<13 and c<15.5):
  print("POSITIVO")

elif(a==mujer) and (b>180) and (c>=12 and c<=16):
  print("NEGATIVO")
elif(a==mujer) and (b>180) and (c<12 and c<16):
  print("POSITIVO")

elif(a==hombre) and (b>180) and (c>=14 and c<=18):
  print("NEGATIVO")
elif(a==hombre) and (b>180) and (c<14 and c<18):
  print("POSITIVO")