eleitores = 0
nao_eleitores = 0
total_idades = []

for i in range (500): 
     idade = int (input("Digite a idade do aluno: "))
     total_idades.append(idade)
    
for idade in total_idades:
     if idade >= 16:
         eleitores += 1
    
     else:
         nao_eleitores += 1
        
print ("O total de alunos eleitores é de ", eleitores)
print ("Já o total de alunos que não estão sujeitos ao voto é de ", nao_eleitores)
