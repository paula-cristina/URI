''' 
    1012 - Área
    https://www.urionlinejudge.com.br/judge/pt/problems/view/1012
    Autora: Paula Cristina Martins
    E-mail: paulacristina@unifeg.edu.br 
'''

x = (input("")).split()
pi = 3.14159
print("TRIANGULO: %.3F" % (float(x[0])*float(x[2]) / 2))
print("CIRCULO: %.3F" % (pi * (float(x[2])**2)))
print("TRAPEZIO: %.3F" % ((float(x[0]) + float(x[1]))*(float(x[2])) / 2))
print("QUADRADO: %.3F" % (float(x[1])*float(x[1])))
print("RETANGULO: %.3F" % (float(x[0])*float(x[1])))