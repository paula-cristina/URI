'''
    1064 - Positivos e Média
    https://www.urionlinejudge.com.br/judge/pt/problems/view/1064
    Autora: Paula Cristina Martins
    E-mail: paulacristina@unifeg.edu.br 
'''

x = qtd = valor = 0
for x in range(0,6):
  a = float(input())
  if a > 0:
    qtd += 1
    valor+=a
print("%d valores positivos" % qtd)
print("{:.1F}". format(valor/qtd))