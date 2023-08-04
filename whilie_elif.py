
# Klaus Santos - Oswaldo José - Jhonael Rocha

def mostrarNumero():
    rodando = True
    while (rodando == True):
        try:
            numero = int(input("Digite um número entre 0 e 100 : "))
            if numero >= 0 and numero <= 100:
                print("O número que você digitou foi : " + str(numero))
                rodando = False
                if numero % 2 == 0 and numero % 3 != 0: #Verifica se o número é múltiplo de 2 e não é de 3
                    print(str(numero) + " é divisível por 2")
                elif numero % 2 != 0 and numero % 3 == 0: #Verifica se o número é múltiplo de 3 e não é de 2
                    print(str(numero) + " é divisível por 3")
                elif numero % 2 == 0 and numero % 3 == 0: #Verifica se o número é múltiplo de 3 e de 2 ao mesmo tempo
                    print(str(numero) + " é divisível por 2 e por 3") 
                else:
                    print(str(numero) + " não é divisível nem por 2 nem por 3")  
            else:
                print("O número não está entre 0 e 100")
        except:
            print("Você não digitou um número inteiro")
mostrarNumero()