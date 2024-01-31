# while True:
    
#     a = int(input("Digite um inteiro: "))
#     b = int(input("Digite um inteiro: "))
#     c = int(input("Digite um inteiro: "))
#     print("%d, %d e %d " %(a, b, c))
 
     
#     if a >= b + c or b >= a + c or c >= a + b:
#         print("Não são comprimentos dos lados de um triângulo")
#     else:
#         print("São comprimentos dos lados de um triângulo")

        
#     if   a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
#         print("retângulo")
#     elif a*a >  b*b + c*c or b*b >  a*a + c*c or c*c >  a*a + b*b:
#         print("obtusângulo")
#     else:
#         print("acutângulo")

        
#     if  a == b == c:
#         print("equilátero")
#     elif a == b or a == c or b == c:
#         print("isósceles")
#     else:
#         print("escaleno")
               		
def main():
    continua = "Sim"
    lista = []
    contador = 1

    while continua == "Sim":
        i = int(input("Digite um numero: "))
        lista.append(i)
        if len(lista) >= 3:
            continua = input("Continua ou Para? Sim ou Não.")
        
    subida = False
    descida = False
    
    for a in lista:
        if contador < len(lista):
            if a < lista[contador]:
                subida = True
                descida = False
            elif a > lista[contador] and subida == True:
                descida = True

        contador += 1
    
    if subida == True and descida == True:
        print("Pico")
    else:
        print("Não é Pico")

main()
