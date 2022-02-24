def temperatura():
    
    lista = []
    media = 0
    
    for i in range(12):
        
        temp = float(input("*Exercicio13* Digite a temperatura média do mes: "))
        lista.append(temp)
        
        media = media + lista[i]
    
    media_geral = media / 12
    
    print(media_geral)
    
    for i in range(12):
        
        if lista[i] > media_geral:
            
            print("Acima da media de temperatura:",lista[i],"\nNo mes:",i+1,"\n")