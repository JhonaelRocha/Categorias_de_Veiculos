#Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código #deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o #programa mostrará a seguinte lista de operações:

#1: Soma
#2: Subtração
#3: Multiplicação
#4: Divisão
#0: Sair

#Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o #sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

#Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de #cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário #escolher a opção “Sair”, o sistema irá parar.

#É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o #resultado.


def mostrarOpcoes():
    print("1 : Soma")
    print("2 : Subtração")
    print("3 : Multiplicação")
    print("4 : Divisão")
    print("0 : Sair")

mostrarOpcoes()

def calcular(opcao, num1, num2):
    if opcao == 1:
        total = num1 + num2
    elif opcao == 2:
        total = num1 - num2
    elif opcao == 3:
        total = num1 * num2
    elif opcao == 4:
        total = num1 / num2
    else:
        total = None
        
    return total

opcao = -1

while opcao != 0:
    opcao = int(input("O que você deseja fazer? : "))

    if opcao == 0:
        print("Encerrando o programa.")
        break

    if opcao != 1 and opcao !=2 and opcao !=3 and opcao !=4:
        print("Opção inválida, digite outra opção.")
        mostrarOpcoes()
        continue

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resultado = calcular(opcao, num1, num2)
    if resultado != None:
        print("Resultado:", resultado)