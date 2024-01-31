# Criar um algoritmo que leia a idade de uma pessoa e informe sua classe 
# eleitoral:
#  •  não-eleitor (abaixo de 16 anos)
#  •  eleitor obrigatório (entre 18 e 65 anos)
#  •  eleitor facultativo (entre 16 e 18 anos e maior de 65 anos)
while True:
    Idade = int(input("DIGITE SUA IDADE: "))

    if 16 > Idade:
        print("Não Eleitor")
    elif 18 <= Idade < 65:
        print ("Eleitor Obrigatório")
    elif 16 < Idade < 18 or Idade > 65:
        print ("Eleitor Facultativo")
    elif 15 < Idade < 17 or Idade > 70:
        print("acertou misaravi")