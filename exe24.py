import random

def dados():
    
    
    
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    
    for i in range(100):
        
        lancamento = random.randint(1,6)

        if(lancamento == 1):
            
            count1 = count1 + 1
            
        elif(lancamento == 2):
            
            count2 = count2 + 1
            
        elif(lancamento == 3):
            
            count3 = count3 + 1
            
        elif(lancamento == 4):
            
            count4 = count4 + 1
            
        elif(lancamento == 5):
            
            count5 = count5 + 1
            
        else:
            
            count6 = count6 + 1
            

    print("Numero 1: ", count1)
    print("Numero 2: ", count2)
    print("Numero 3: ", count3)
    print("Numero 4: ", count4)
    print("Numero 5: ", count5)
    print("Numero 6: ", count6)
    