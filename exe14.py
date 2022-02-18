def perguntas():
    
    print("*Exercicio14* Responda as perguntas a seguir com 'Sim' ou 'Nao':\n")
    
    p1 = input("*Exercicio14* Telefonou para a vitima? ")
    p2 = input("*Exercicio14* Esteve no local do crime? ")
    p3 = input("*Exercicio14* Mora perto da vitima? ")
    p4 = input("*Exercicio14* Devia para a vitima? ")
    p5 = input("*Exercicio14* Já trabalhou com a vitima? ")
    
    contador = 0
    
    
    if((p1 == 'Sim') or (p1 == 'sim')):
        
        contador = contador + 1
    
    if((p2 == 'Sim') or (p2 == 'sim')):
        
        contador = contador + 1
    
    if((p3 == 'Sim') or (p3 == 'sim')):
        
        contador = contador + 1
    
    if((p4 == 'Sim') or (p4 == 'sim')):
        
        contador = contador + 1
    
    if((p5 == 'Sim') or (p5 == 'sim')):
        
        contador = contador + 1
    
    else:
        
        contador = contador
        
    
    if(contador == 5):
        
        print("Assassino\n")
        
    elif(contador > 2):
        
        print("Cúmplice\n")
        
    elif(contador == 2):
        
        print("Suspeita\n")
    
    else:
        
        print("Inocente\n")
    
    