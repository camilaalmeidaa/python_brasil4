def vetores2():
    
    vetor1 = []
    vetor2 = []
    vetor3 = []
    vetor4 = []
    
    print("Vetor 1:")
    
    for i in range(10):
        
        vetor1.append(int(input("*Exercicio10* Digite um elemento: ")))
        
    print("Vetor 2:")
    
    for i in range(10):
        
        vetor2.append(int(input("*Exercicio10* Digite um elemento: ")))
    
    print("Vetor 3:")
    
    for i in range(10):
        
        vetor3.append(int(input("*Exercicio10* Digite um elemento: ")))
    
    
    for i in range(10):
        
        vetor4.append(vetor1[i])
        vetor4.append(vetor2[i])
        vetor4.append(vetor3[i])

    print("\nVetor itercalado:",vetor4)
    