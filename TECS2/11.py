"""
ENTRADAS
salario bruto-->float-->sb
salida
sueldo neto-->float-->sn
"""
sb=float(input("Digite el salario bruto"))
sn=0.0
if(sb>=5000000):
  sn=(sb*0.01)+sb
if(sb>=4300000):
  sn=(sb*0.15)+sb
if(sb>=3600000):
  sn=(sb*0.20)+sb
if(sb>=2000000):
  sn=(sb*0.40)+sb
if(sb>=900000):
  sn=(sb*0.60)+sb
print(sn)