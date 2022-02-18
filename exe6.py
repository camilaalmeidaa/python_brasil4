def notas2():
    
    medias = []
    count_alunos = 0

    
    for i in range(10):
        
        soma = 0
        
        print("*Exercicio6* Aluno",i+1,":")
        
        for j in range(4):
            
            nota = float(input("*Exercicio6* Digite a nota: "))
            
            soma = soma + nota
            
        medias.append(soma / 4)
        
        if(medias[i] >= 7):
            
            count_alunos = count_alunos + 1
    
    print("\nNumero de alunos com média maior ou igual a 7:",count_alunos)
