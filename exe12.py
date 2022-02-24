def idade_altura2():
    
    idades = [12,13,13,15,16,12,14,16,14,13,14,15,16,12,11,15,14,13,12,12,12,13,14,14,14,14,15,13,12,13]
    alturas = [1.70,2.0,1.40,1.55,1.70,1.3,1.4,1.5,1.43,1.52,1.12,1.53,1.38,1.42,1.5,1.70,2.0,1.40,1.55,1.70,1.3,1.4,1.5,1.43,1.52,1.12,1.53,1.38,1.42,1.5]
    
    soma = 0
    media = 0

    for i in range(len(alturas)):
        
        soma =  soma + alturas[i]
        media = soma / len(alturas)

    contador = 0

    for j in range(len(idades)):
        
        if idades[j] >= 13 and alturas[j] < media:
            
            contador = contador + 1
            
    print("O numero de alunos com mais de 13 anos e altura abaixo da média é:",contador,"alunos.\n")