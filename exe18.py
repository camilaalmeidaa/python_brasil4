def jogadores():
    
    votos = []
    count = 0
    j1 = 0
    j2 = 0
    j3 = 0
    j4 = 0
    j5 = 0
    j6 = 0
    j7 = 0 
    j8 = 0 
    j9 = 0 
    j10 = 0 
    j11 = 0 
    j12 = 0 
    j13 = 0
    j14 = 0 
    j15 = 0 
    j16 = 0 
    j17 = 0 
    j18 = 0 
    j19 = 0 
    j20 = 0 
    j21 = 0 
    j22 = 0
    j23 = 0
    
    
    
    print("Enquete: Quem foi o melhor jogador?\n")
    
    voto = int(input("*Exercicio18* Número do jogador (0 = fim): "))
    votos.append(voto)
    
    
    
    while(voto != 0):
        
        voto = int(input("*Exercicio18* Número do jogador (0 = fim): "))
        votos.append(voto)
        
        if(voto < 0 or voto > 23):
        
            print("Informe um valor entre 1 e 23 ou 0 para sair!")
        
            voto = int(input("*Exercicio18* Número do jogador (0 = fim): "))
            votos.append(voto)
    
    
    
    for i in range(len(votos)):
        
        if ((votos[i] < 1) or (votos[i] > 23)):
            
            votos[i] = 0

    
    for i in range(len(votos)):
        
        if(votos[i] != 0):
            
            count = count + 1
        
        if(votos[i] == 1):
            
            j1 = j1 + 1
        
        elif(votos[i] == 2):
            
            j2 = j2 + 1
        
        elif(votos[i] == 3):
            
            j3 = j3 + 1
        
        elif(votos[i] == 4):
            
            j4 = j4 + 1
        
        elif(votos[i] == 5):
            
            j5 = j5 + 1
        
        elif(votos[i] == 6):
            
            j6 = j6 + 1
        
        elif(votos[i] == 7):
            
            j7 = j7 + 1
        
        elif(votos[i] == 8):
            
            j8 = j8 + 1
        
        elif(votos[i] == 9):
            
            j9 = j9 + 1
        
        elif(votos[i] == 10):
            
            j10 = j10 + 1
        
        elif(votos[i] == 11):
            
            j11 = j11 + 1
        
        elif(votos[i] == 12):
            
            j12 = j12 + 1
        
        elif(votos[i] == 13):
            
            j13 = j13 + 1
        
        elif(votos[i] == 14):
            
            j14 = j14 + 1
            
        elif(votos[i] == 15):
            
            j15 = j15 + 1
        
        elif(votos[i] == 16):
            
            j16 = j16 + 1
        
        elif(votos[i] == 17):
            
            j17 = j17 + 1
        
        elif(votos[i] == 18):
            
            j18 = j18 + 1
        
        elif(votos[i] == 19):
            
            j19 = j19 + 1
        
        elif(votos[i] == 20):
            
            j20 = j20 + 1
        
        elif(votos[i] == 21):
            
            j21 = j21 + 1
        
        elif(votos[i] == 22):
            
            j22 = j22 + 1
        
        elif(votos[i] == 23):
            
            j23 = j23 + 1


    lista = [j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20,j21,j22,j23]
    
    
    for i in range(len(lista)):
        
        
        if(lista[i] == max(lista)):
            
            print("\nO melhor jogador foi o número",i+1,"com",lista[i],"votos, correspondendo a",(lista[i]/len(votos)*100),"% dos votos.")
        
        
        
        
    
    
    print("\nResultado da votação:\n\nForam computados",count,"votos")
    
    
            
        
 
        
        
    
    