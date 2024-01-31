# Ler três valores inteiros (variáveis a, b e c) e efetuar o cálculo da equação de segundo grau, apresentando: 
# as duas raízes, quando for possível efetuar o cálculo (delta positivo ou zero); a mensagem "Não há raízes reais", 
# se não for possível fazer o cálculo (delta negativo);
# e a mensagem "Não é equação do segundo grau", se o valor de a for igual a zero.
import math

a = float(input("Me fale um Valor A: "))
b = float(input("Me fale um Valor B: "))
c = float(input("Me fale um Valor C: "))

 #delta =  b² - 4 * a * c
 #x = b +- raiz delta /2 * a

delta = ((b**2) - (4 * a * c))
print (delta)

if 0 > delta:
    print ("Não há raízes reais")
elif delta == 0:
    print("Não é equação do segundo grau")
else:
    print("Delta positivo")


