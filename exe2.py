def lista_inversa():
    
    numeros = []
    
    for i in range(10):
        
        num = float(input("*Exercicio2* Digite um numero real: "))
        numeros.append(num)
    
    numeros.reverse()
    
    print("Os numeros digitados na ordem inversa são:",numeros)
        
    