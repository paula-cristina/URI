''' 
    1035 - Teste de Seleção 1
    https://www.urionlinejudge.com.br/judge/pt/problems/view/1035
    Autora: Paula Cristina Martins
    E-mail: paulacristina@unifeg.edu.br 
'''

x = input().split()
if (int(x[1]) > int(x[2])) and (int(x[3]) > int(x[0])) and ((int(x[2]) + int(x[3])) > (int(x[0]) + int(x[1]))) and (int(x[2]) >= 0) and (int(x[3])>=0) and (int(x[0])%2==0):
  print("Valores aceitos")
else:
  print("Valores nao aceitos")