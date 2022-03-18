def mouses():
    
    numeros = []
    opcoes = []
    count1 = 0 
    count2 = 0
    count3 = 0
    count4 = 0
    
    print("Escolha uma das opções abaixo:\n1- necessita da esfera\n2- necessita de limpeza\n3- necessita troca do cabo ou conector\n4- quebrado ou inutilizado")
    
    numero = int(input("\n*Exercicio22* Digite o número de identificação do mouse: "))
    
    numeros.append(numero)
    
    opcao = int(input("*Exercicio22* Digite a alternativa correspondente ao problema: "))
    
    opcoes.append(opcao)
    
    while(numero != 0):
        
        numero = int(input("*Exercicio22* Digite o número de identificação do mouse: "))
    
        numeros.append(numero)
    
        opcao = int(input("*Exercicio22* Digite a alternativa correspondente ao problema: "))
    
        opcoes.append(opcao)
    
    for i in range(len(opcoes)):
        
        if(opcoes[i] == 1):
            
            count1 = count1 + 1
        
        elif(opcoes[i] == 2):
            
            count2 = count2 + 1
        
        elif(opcoes[i] == 3):
            
            count3 = count3 + 1
        
        elif(opcoes[i] == 4):
            
            count4 = count4 + 1
        
    
    qtde = len(numeros)
    
    
    print("Quantidade de mouses: ",qtde)
    
    print("\nSituação\t\t\tQuantidade\tPercentual")
    
    print("1- necessita da esfera\t\t",count1,"\t",(count1/qtde)*100,"%\n2- necessita de limpeza\t\t",count2,"\t",(count2/qtde)*100,"%\n3- necessita troca do cabo ou conector\t\t",count3,"\t",(count3/qtde)*100,"%\n4- quebrado ou inutilizado\t\t",count4,"\t",(count4/qtde)*100,"%")
        