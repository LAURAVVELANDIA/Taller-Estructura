a=float(input("Digite el kilometraje: "))
b=70000+((a-300)*30000)
c=150000+((a-1000)*9000)

if(a<=300):
  print("50000")
elif(a>300 and a<=1000):
  print(b)
elif(a>1000):
  print(c)
