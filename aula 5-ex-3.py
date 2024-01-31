produto = input("Digite o nome do Produto: ")
venda = float (input("Digite o Valor Pago: "))

if venda < 10:
    print ("O Valor de Venda é: ",venda * 1.7, "\nO Produto é: ", produto)
elif 10 <= venda < 30:
    print ("O Valor de Venda é: ",venda * 1.5, "\nO Produto é: ", produto)
elif 30 <= venda < 50 :
    print ("O Valor de Venda é: ",venda * 1.4, "\nO Produto é: ", produto)
elif venda >= 50:
    print ("O Valor de Venda é: ",venda * 1.3, "\nO Produto é: ", produto)
    