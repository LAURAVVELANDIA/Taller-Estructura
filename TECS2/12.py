"""
entradas
temperatura-->float-->t
salidas
deporte-->str-->d
"""
t=float(input("Digite temperatura: "))
d=""#str
if(t>85):
  d="Natación"
elif(t>=71 and t<=85):
  d="Tennis"
elif(t>=33 and t<=70):
  d="Golf"
elif(t>=11 and t<=32):
  d="Esquí"
elif(t<=10):
  d="Marcha"
print(d)