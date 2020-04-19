''' 
    1020 - Idade em Dias
    https://www.urionlinejudge.com.br/judge/pt/problems/view/1020
    Autora: Paula Cristina Martins
    E-mail: paulacristina@unifeg.edu.br 
'''

x = int(input())
y = x 
ano = y // 365
y = y % 365
mes = y // 30
y = y % 30
dia = y
print("{} ano(s)\n{} mes(es)\n{} dia(s)". format(ano, mes, dia))