'''
    1060 - Números Positivos
    https://www.urionlinejudge.com.br/judge/pt/problems/view/1060
    Autora: Paula Cristina Martins
    E-mail: paulacristina@unifeg.edu.br 
'''

x = 0
b = 0
for x in range(0,6):
  a = float(input())
  if a > 0:
    b += 1
print("%d valores positivos" % b)