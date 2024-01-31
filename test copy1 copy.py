salario = float(input("Preciso que digite o valor do seu salário fixo mensal:"))
vendas = float(input("Qual foi total desse mes das suas vendas?"))

comissao = vendas*0.04
total = salario+comissao

print (f"O valor da sua comissão é de R${comissao:.2f}")
print (f"No total, você receberá R${total:.2f}")
