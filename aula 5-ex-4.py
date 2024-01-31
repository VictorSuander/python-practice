#  Elabore um programa em Python que implemente uma calculadora com as funções de somar, subtrair, multiplicar e dividir. 
# O programa deverá solicitar ao usuário os dois valores, e perguntar qual a operação pretendida (‘+’, ‘-‘ , ‘*’ ou ‘/’ ) 
# e a seguir calcular e mostrar o resultado.

while True:
    num1 = float(input("Digite um Valor 1: "))
    num2 = float(input("Digite um Valor 2: "))
    operador = input("Qual é o operador ( + ) ( - ) ( / ) ( * ) :  ")

    if operador == "+":
        print(num1 + num2)
    elif operador == "-":
        print(num1 - num2)
    elif operador == "/":
        print(num1 / num2)
    elif operador == "*":
        print(num1 * num2)
    else:
        print("Operador Invalido")

    

    

