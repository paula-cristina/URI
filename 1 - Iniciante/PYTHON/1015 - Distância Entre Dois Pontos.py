''' 
    1015 - Distância Entre Dois Pontos
    https://www.urionlinejudge.com.br/judge/pt/problems/view/1015
    Autora: Paula Cristina Martins
    E-mail: paulacristina@unifeg.edu.br 
'''

import math
x = (input("")).split()
y = (input("")).split()
print("%.4F" % math.sqrt(math.pow(float(y[0]) - float(x[0]), 2) + math.pow(float(y[1]) - float(x[1]), 2)))