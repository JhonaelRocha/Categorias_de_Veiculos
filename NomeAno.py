rodando = True
while rodando:
    try:
        print("Insira seu nome : ")
        nome = input()
        anoNascimento = int(input("Insira seu ano de nascimento : "))
        if anoNascimento < 1922 or anoNascimento > 2021:
            print("Digite um ano entre 1922 e 2021")
            continue
        print(f'{nome.title()} você nasceu em {anoNascimento}.')
        rodando = False
    except:
        print("Dados incorretos")
