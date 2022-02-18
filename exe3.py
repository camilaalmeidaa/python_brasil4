def notas():
    
    notas = []
    soma = 0
    
    for i in range(4):
        
        nota = float(input("*Exercicio3* Digite a nota: "))
        notas.append(nota)
        
        soma = soma + notas[i]
        
    media = soma / len(notas)
        
    print("\nNotas:",notas,"\nMedia:",media)
    
        