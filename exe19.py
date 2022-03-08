def sistemas():
    
    lista = []
    
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    
    print("1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro")
    
    opcao = int(input("*Exercicio19* Qual o melhor Sistema Operacional para uso em servidores? (0= fim): "))
    lista.append(opcao)
    
    while(opcao != 0):
        
        opcao = int(input("*Exercicio19* Qual o melhor Sistema Operacional para uso em servidores? (0= fim): "))
        lista.append(opcao)
    
    lista.remove(0) 
    
    for i in range(len(lista)):
        
        if(lista[i] == 1):
            
            count1 = count1 + 1
        
        elif(lista[i] == 2):
            
            count2 = count2 + 1
            
        elif(lista[i] == 3):
            
            count3 = count3 + 1
        
        elif(lista[i] == 4):
            
            count4 = count4 + 1
            
        elif(lista[i] == 5):
            
            count5 = count5 + 1
            
        elif(lista[i] == 6):
            
            count6 = count6 + 1
            
    total = count1 + count2 + count3 + count4 + count5 + count6

        
    print("\nSistema Operacional \t Votos \t  %")
    print("-------------------     ------   ---")
    
    print("Windows Server\t\t",count1,"\t", round((count1/total)*100),"%\nUnix\t\t\t",count2,"\t",round((count2/total)*100),"%\nLinux\t\t\t",count3,"\t",round((count3/total)*100),"%\nNetware\t\t\t",count4,"\t",round((count4/total)*100),"%\nMacOS\t\t\t",count5,"\t",round((count5/total)*100),"%\nOutro\t\t\t",count6,"\t",round((count6/total)*100),"%")
    
    
    print("-------------------     ------   ---")
    print("\nTotal\t\t\t",total)
    
    

    