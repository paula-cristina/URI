''' 
    1019 - Conversão de Tempo
    https://www.urionlinejudge.com.br/judge/pt/problems/view/1019
    Autora: Paula Cristina Martins
    E-mail: paulacristina@unifeg.edu.br 
'''

n = int(input())
h = n // 3600
m = (n - h * 3600) // 60
s = n % 60
print("{}:{}:{}". format(h, m, s))