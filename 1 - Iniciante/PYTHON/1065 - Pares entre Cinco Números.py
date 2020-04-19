'''
    1065 - Pares entre Cinco Números
    https://www.urionlinejudge.com.br/judge/pt/problems/view/1065
    Autora: Paula Cristina Martins
    E-mail: paulacristina@unifeg.edu.br 
'''

x = qtd = 0
for x in range(0,5):
  a = float(input())
  if a % 2 == 0:
    qtd += 1
print("%d valores pares" % qtd)