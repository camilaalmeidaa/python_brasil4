def notas3():
    
    lista = []
    contador = 0
    soma = 0
    media = 0
    
    nota = float(input("*Exercicio15* Digite a nota: "))
    
    lista.append(nota)
    
    while(nota != -1):
        
        nota = float(input("*Exercicio15* Digite a nota: "))
    
        lista.append(nota)
        
        contador = contador + 1
    
    lista.remove(-1)
    
    
    
    print(lista)
    print("\nQuantidade de notas:",contador,"\nNotas:",lista,"\n")
    
    lista.reverse()
    
    for i in range (len(lista)):
        
        soma = soma + lista[i]
        
        print(lista[i])
    
    media = soma / len(lista)
    
    count = 0
    count_menor_sete = 0
    
    for i in range (len(lista)):
        
        if(lista[i] > media):
            
            count = count + 1
        
        if(lista[i] < 7):
            
            count_menor_sete = count_menor_sete + 1
    
    print("\nSoma das notas:",soma,"\nMédia das notas:",media,"\nQuantidade de notas acima da media:",count,"\nQuantidade de notas abaixo de 7:",count_menor_sete,"\nFim do programa")
    
    
 
    
        
        