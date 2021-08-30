a=int(input("Dividendo: "))
b=int(input("Divisor: "))
if a>0 and b>0:
  c=0
  r=a
  while(r>=b):
    r=r-b
    c=c+1
  print(c)