def idade_altura():
    
    idades = []
    alturas = []
    
    for i in range(5):
        
        print("*Exercicio8* Pessoa",i+1,":")
        
        idade = int(input("*Exercicio8* Digite a idade: "))
        idades.append(idade)
        
        altura = float(input("*Exercicio8* Digite a altura: "))
        alturas.append(altura)
        
    idades.reverse()
    alturas.reverse()
    
    print("Idades na ordem inversa:",idades,"\nAlturas na ordem inversa:",alturas)