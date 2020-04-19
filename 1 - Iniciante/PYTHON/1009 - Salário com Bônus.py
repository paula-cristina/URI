''' 
    1009 - Salário com Bônus
    https://www.urionlinejudge.com.br/judge/pt/problems/view/1009
    Autora: Paula Cristina Martins
    E-mail: paulacristina@unifeg.edu.br 
'''

funcionario = input("")
sal_fixo = float(input(""))
vendas = float(input(""))
comissao = 15
print("TOTAL = R$ {:.2F}". format(sal_fixo + ((vendas * comissao) / 100)))