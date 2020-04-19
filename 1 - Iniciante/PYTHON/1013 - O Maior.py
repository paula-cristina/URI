''' 
    1013 - O Maior
    https://www.urionlinejudge.com.br/judge/pt/problems/view/1013
    Autora: Paula Cristina Martins
    E-mail: paulacristina@unifeg.edu.br 
'''

x = (input("")).split()
if int(x[0]) >= int(x[1]) >= int(x[2]) or int(x[0]) >= int(x[2]) >= int(x[1]):
  print("%d eh o maior" % int(x[0]))
elif int(x[1]) >= int(x[2]) >= int(x[0]) or int(x[1]) >= int(x[0]) >= int(x[2]):
  print("%d eh o maior" % int(x[1]))
else:
  print("%d eh o maior" % int(x[2]))