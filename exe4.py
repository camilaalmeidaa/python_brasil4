def consoantes(lista):
    
    
    consoantes = []
    count_consoantes = 0
    count_vogais = 0
    
        
    vogais = ['a','e','i','o','u']
    
    
    for i in range(len(lista)):
        
        lista[i].lower()
        
        if lista[i] in vogais:
            
            count_vogais = 1
        
        else:
            
            consoantes.append(lista[i])
            count_consoantes = count_consoantes + 1
        
    print("\nConsoantes:",consoantes,"\nQuantidade de consoantes:",count_consoantes)
            
    

    