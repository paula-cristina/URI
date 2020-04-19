''' 
    1038 - Lanche
    https://www.urionlinejudge.com.br/judge/pt/problems/view/1037
    Autora: Paula Cristina Martins
    E-mail: paulacristina@unifeg.edu.br 
'''

x = input().split()
cod = int(x[0])
qtd = int(x[1])
if cod == 1:
  print("Total: R$ {:.2F}". format(qtd * 4.00))
elif cod == 2:
  print("Total: R$ {:.2F}". format(qtd * 4.50))
elif cod == 3:
  print("Total: R$ {:.2F}". format(qtd * 5.00))
elif cod == 4:
  print("Total: R$ {:.2F}". format(qtd * 2.00))
elif cod == 5:
  print("Total: R$ {:.2F}". format(qtd * 1.50))