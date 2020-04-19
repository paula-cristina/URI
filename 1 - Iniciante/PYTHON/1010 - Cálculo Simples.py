''' 
    1010 - Cálculo Simples
    https://www.urionlinejudge.com.br/judge/pt/problems/view/1010
    Autora: Paula Cristina Martins
    E-mail: paulacristina@unifeg.edu.br 
'''

x = (input()).split()
y = (input()).split()
print("VALOR A PAGAR: R$ {:.2F}". format((float(x[1])*float(x[2]))+(float(y[1])*float(y[2]))))