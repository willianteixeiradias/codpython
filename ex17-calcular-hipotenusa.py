' calcular a hipotenusa de um triangulo formula  a**  + b** = c**'
from math import hypot
num1 = float (input('digite o numero do lado A'))
num2 = float (input('digite o numero do lado B:'))
hipo = float
# metodo 1
#hipo =  ( (num1**2+num2**2) **(1/2))
hipo = hypot(num1, num2)
print ( hipo)

