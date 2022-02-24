def vendedores():
    
    lista = []
    salarios = []
    
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
   
    
    vendas = float(input("*Exercicio16* Digite o valor de suas vendas: "))
    
    lista.append(vendas)
    
    while(vendas != -1):
        
        vendas = float(input("*Exercicio16* Digite o valor de suas vendas: "))
    
        lista.append(vendas)
        
    lista.remove(-1)
    
    for i in range (len(lista)):
        
        salario = 200 + (0.09 * lista[i])
        salarios.append(salario)
        
  
    for i in range (len(salarios)):
        
        if(salarios[i] >= 1000):
            
            count9 = count9 + 1
        
        elif(salarios[i] >= 900):
            
            count8 = count8 + 1
            
        elif(salarios[i] >= 800):
            
            count7 = count7 + 1
        
        elif(salarios[i] >= 700):
            
            count6 = count6 + 1
        
        elif(salarios[i] >= 600):
            
            count5 = count5 + 1
        
        elif(salarios[i] >= 500):
            
            count4 = count4 + 1
        
        elif(salarios[i] >= 400):
            
            count3 = count3 + 1
        
        elif(salarios[i] >= 300):
            
            count2 = count2 + 1
        
        else:
        
            count1 = count1 + 1
    
    print("\n$200 - $299:",count1,"vendedores\n$300 - $399:",count1,"vendedores\n$400 - $499:",count3,"vendedores\n$500 - $599:",count4,"vendedores\n$600 - $699:",count5,"vendedores\n$700 - $799:",count6,"vendedores\n$800 - $899:",count7,"vendedores\n$900 - $999:",count8,"vendedores\n$1000 em diante:",count9,"vendedores\n")


        
        
        