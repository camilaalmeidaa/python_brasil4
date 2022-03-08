def abonos():
    
    salarios = []
    abonos = []
    
    count_min = 0
    abono = 0
    
    sal = float(input("*Exercicio20* Digite seu salário de dezembro (0 = fim): "))
    salarios.append(sal)
    
    
    
    while(sal != 0):
        
        sal = float(input("*Exercicio20* Digite seu salário de dezembro (0 = fim): "))
        salarios.append(sal)
    
    salarios.remove(0)
    
    for i in range(len(salarios)):
        
        if(salarios[i] < 1000):
            
            abono = 100
            abonos.append(abono)
            
            count_min = count_min + 1
        
        else:
            
            abono = 0.2 * salarios[i]
            abonos.append(abono)
    

    
    print("Projeção de Gastos com Abono")
    print("============================")
    
    
    for j in range(len(salarios)):
        
        print("Salário:",salarios[j])
    
    print("Salário\t\t- Abono")    
    
    for m in range(len(salarios)):
        
        print("R$",salarios[m],"\t- R$",abonos[m])
    
    qtde = len(salarios)
    
    print("\nForam processados",qtde,"colaboradores\nTotal gasto com abonos: R$",sum(abonos),"\nValor mínimo pago a",count_min,"colaboradores\nMaior valor de abono pago: R$",max(abonos))    
        
    
    