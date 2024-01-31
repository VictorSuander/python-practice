#  Temos um grupo de pessoas. Escreva um programa em Python que leia o sexo e a altura de cada pessoa,
# calcule e mostre a altura média das mulheres e dos homens separadamente. Utilize o comando de repetição que desejar

grupo_de_pessoas = [('Gustavo','Masculino','1.72'),('Julia','Feminina','1.59'),('Caio','Masculino','1.82'),('Gerberson','Masculino','1.56'),('Stefanny','Feminino','1.39')]
lista_mulher = []#Lista Vazia das Mulheres
lista_homem = []#Lista Vazia dos Homens

for i in grupo_de_pessoas:
    print(i)
    if i[1] == 'Masculino':
        lista_homem.append(float(i[2]))
    else:
        lista_mulher.append(float(i[2]))


z = len(lista_mulher)# Ler o tamanho da lista
a = sum(lista_mulher) #Faz a soma de todos itens da lista 
x = len(lista_homem)#Ler o tamanho da lista
y = sum(lista_homem)#Faz a soma de todos itens da lista 

print("A média da mulher é: ",a/z,"\nA média do homem é: ", y/x)#Determina a media e já printa.5
