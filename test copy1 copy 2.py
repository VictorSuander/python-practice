genero = input("Olá! Antes de iniciarmos, preciso que você me responda: você é homem ou mulher? ")
altura = float(input("Preciso saber também qual a sua altura em metros (Obs: Digite o seu peso sendo separado por ponto). Agora, digite pra mim: "))

if genero == "Homem" or genero == "homem":
    peso_ideal = (72.7*altura)-58
 
elif genero == "mulher" or genero == "Mulher":
    peso_ideal = (62.1*altura)-44.7
    
else:
  peso_ideal = None

if peso_ideal is not None:
  print(f"Seu peso ideal é {peso_ideal:.2f} kg.")
else:
  print("Você deve ter colocado algum dado incorreto.")