''' 
    1021 - Notas e Moedas
    https://www.urionlinejudge.com.br/judge/pt/problems/view/1021
    Autora: Paula Cristina Martins
    E-mail: paulacristina@unifeg.edu.br 
'''

valor = float(input(""))

x = valor
''' notas '''
n100 = x // 100
x = x % 100
n50 = x // 50
x = x % 50
n20 = x // 20
x = x % 20
n10 = x // 10
x = x % 10
n5 = x // 5
x = x % 5
n2 = x // 2
x = x % 2

x*=100
''' moedas '''
m1 = x // 100
x = x % 100
m50 = x // 50
x = x % 50
m25 = x // 25
x = x % 25
m10 = x // 10
x = x % 10
m5 = x // 5
x = x % 5
m01 = x

print("NOTAS:\n{} nota(s) de R$ 100.00\n{} nota(s) de R$ 50.00\n{} nota(s) de R$ 20.00\n{} nota(s) de R$ 10.00\n{} nota(s) de R$ 5.00\n{} nota(s) de R$ 2.00\nMOEDAS:\n{} moeda(s) de R$ 1.00\n{} moeda(s) de R$ 0.50\n{} moeda(s) de R$ 0.25\n{} moeda(s) de R$ 0.10\n{} moeda(s) de R$ 0.05\n{} moeda(s) de R$ 0.01". format(int(n100), int(n50), int(n20), int(n10), int(n5), int(n2), int(m1), int(m50), int(m25), int(m10), int(m5), int(m01)))