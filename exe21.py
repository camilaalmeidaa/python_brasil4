def combustivel(lista1,lista2):
    
    for i in range(len(lista1)):
        
        print("Veículo",i+1,"\nNome:",lista1[i],"\nKm por litro:",lista2[i],"\n")
    
    print("Relatório Final\n")
    
    
    for j in range(len(lista1)):
        
        print(f"{j+1} - {lista1[j]} \t - {lista2[j]} \t - {1000/lista2[j]:.2f} litros \t - R${(1000/lista2[j])*2.25:.2f}")