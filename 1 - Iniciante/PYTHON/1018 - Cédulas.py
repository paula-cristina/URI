''' 
    1018 - Cédulas
    https://www.urionlinejudge.com.br/judge/pt/problems/view/1018
    Autora: Paula Cristina Martins
    E-mail: paulacristina@unifeg.edu.br 
'''

valor = int(input(""))
x = valor
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
n1 = x
print("{}\n{} nota(s) de R$ 100,00\n{} nota(s) de R$ 50,00\n{} nota(s) de R$ 20,00\n{} nota(s) de R$ 10,00\n{} nota(s) de R$ 5,00\n{} nota(s) de R$ 2,00\n{} nota(s) de R$ 1,00". format(valor,n100, n50, n20, n10, n5, n2, n1))