eleitor = []
nao_eleitor = []

while (500) :
    idade = int(input("DIGITE SUA IDADE: "))


    if 16 > idade:
        nao_eleitor.append(idade)
        print("Não Eleitor")        
    elif 16 <= idade <= 65:
        eleitor.append(idade)
        print("Eleitor")
    
    a = sum(eleitor)
    
    print("A Quantidade de Eleitores: ", a)
   