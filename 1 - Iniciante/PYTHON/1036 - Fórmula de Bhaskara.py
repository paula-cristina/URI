''' 
    1036 - Fórmula de Bhaskara
    https://www.urionlinejudge.com.br/judge/pt/problems/view/1036
    Autora: Paula Cristina Martins
    E-mail: paulacristina@unifeg.edu.br 
'''

import math
v = input().split()
a = float(v[0])
b = float(v[1])
c = float(v[2])
d = b**2 - 4 * a * c
if d < 0 or a == 0:
  print("Impossivel calcular")
else:
  x1 = (-b + (math.sqrt(d))) / (2 * a)
  x2 = (-b - (math.sqrt(d))) / (2 * a)
  print("R1 = {:.5F}\nR2 = {:.5F}". format(x1, x2))
