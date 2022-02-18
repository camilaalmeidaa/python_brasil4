def vetores():
    
    vetor1 = []
    vetor2 = []
    vetor3 = []

    for i in range(10):
        
        vetor1.append(int(input("*Exercicio10* Digite um elemento: ")))
    
    for i in range(10):
        
        vetor2.append(int(input("*Exercicio10* Digite um elemento: ")))
    
    for i in range(10):
        
        vetor3.append(vetor1[i])
        vetor3.append(vetor2[i])

    print("\nVetor itercalado:",vetor3)
    
 