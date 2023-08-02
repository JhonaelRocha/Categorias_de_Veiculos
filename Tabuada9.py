
numero_ad = input("Qual o numero você quer a tabuada? : ")

def FazerTabuada(numero):
    fator = 1
    while fator <= 10:
        calculo = numero * fator
        print(f'{numero} x {fator} = {calculo}')
        fator += 1
    
try:
    FazerTabuada(int(numero_ad))
except:
    print("Valor inválido")
    


