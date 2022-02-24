def saltos():
    
    lista = []
 
    nome = input("*Exercicio17* Digite o nome do atleta: ")
    
    for i in range(5):
        
        salto = float(input("*Exercicio17* Digite a distancia do salto: "))
        
        lista.append(salto)
    
    
        
    print("\nAtleta:",nome)
            
    for i in range(len(lista)):
        
        print("Salto",i+1,":",lista[i],"m")
    
   
    
    print("\nMelhor Salto:",max(lista),"m\nPior Salto:",min(lista))
    
    lista.remove(max(lista))
    lista.remove(min(lista))
    
    media = sum(lista) / len(lista)
    
    print("Media dos demais saltos:",media)
    
    print("\nResultado final:\n")
    print(nome,":",media,"m")
        