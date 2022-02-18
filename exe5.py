def par_impar():
    
    numeros = []
    pares = []
    impares = []
    
    for i in range(20):
        
        num = int(input("*Exercicio5* Digite um numero inteiro: "))
        numeros.append(num)
        
        if(num % 2 == 0):
            
            pares.append(num)
        
        else:
            
            impares.append(num)
            
    print("\nNumeros:",numeros,"\nPares:",pares,"\nImpares:",impares,"\n")
    
    