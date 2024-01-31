# Faça um programa em Python que leia um valor n, inteiro e positivo, calcule e mostre a seguinte soma:
#  S = 1 + 1/2 + 1/3 + 1/4 +...+ 1/n

s = [1]
n = int(input("Digite um Numero Inteiro: "))

for item in range(2, n+1, 1):
    s.append(1/item)

soma = sum(s)
print(soma)