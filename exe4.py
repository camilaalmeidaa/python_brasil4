def consoantes():
    
    letras = []
    lista = []
    count_consoantes = 0
    count_vogais = 0
    
        
    vogais = ['a','e','i','o','u']
    
    
    for i in range(10):
        
        letra = input("*Exercicio4* Digite um caractere: ").lower()
        letras.append(letra)
        
        if letra in vogais:
            
            count_vogais = 1
        
        else:
            
            lista.append(letra)
            count_consoantes = count_consoantes + 1
        
    print("\nConsoantes:",lista,"Quantidade de consoantes:",count_consoantes)
            
    

    