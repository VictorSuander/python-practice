# Faça um programa em Python que 
# imprima os números pares entre 0 e 100

lista = []

grupo_de_valores = [-4,-3,-2,-1,0,1,2,3,4]

for item in grupo_de_valores:
    if item >= 0:
        print("Positivo")
    else:
        print(item," é Negativo")
print("Valor Minimo: ", min(grupo_de_valores))
print("Valor Maximo: ", max(grupo_de_valores))
