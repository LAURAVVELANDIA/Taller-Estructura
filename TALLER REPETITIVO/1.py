k=int(input(""))
n=int(input(""))
final=(n+1)
while (n>k):
  a=[]
  for i in range (k,final):
    a.append(i)
  a.sort(reverse=True)
  print(a)
  break
else:
  print("k debe ser menos que n")