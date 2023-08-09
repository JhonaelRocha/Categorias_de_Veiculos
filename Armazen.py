# “Boa tarde, 

# Estamos modernizando nossa loja e precisamos de um novo sistema de controle de estoque. Geralmente anotamos todos os produtos que temos disponíveis, e quando um dos produtos acaba, substituímos ele por algum outro produto. 

# Ouvi dizer que vocês podem fazer um sistema para a gente que mostra a lista com todos nossos produtos, e nos deixa alterar um produto por outro. 

# Além disso, estamos pensando em ampliar nosso armazém, para ter mais espaço para mais produtos. Então, se puderem fazer com que o sistema nos permita adicionar mais produtos à lista, e qualquer outra coisa que acharem necessário, seria muito bom. 

 

# Desde já agradeço!” 

print("Digite os produtos de sua loja (6) e suas respectivas quantidades")


produtos = ["","","","","",""]
quantidade = [0,0,0,0,0,0]
acabou = False

for i in range(0,len(produtos)):
    produtos[i] = input(f'Qual o {i + 1}° produto? : ')
    quantidade[i] = int(input(f'Quantos {produtos[i]} tem? : ')) 
    print(f'No seu estoque tem {quantidade[i]} {produtos[i]}')
    if quantidade[i] == 0:
        acabou = True
        produtos[i] = input(f'{produtos[i]} acabou, o que você deseja colocar no lugar? : ')
        try:
            quantidade[i] = int(input(f'Quantos {produtos[i]} você tem? : '))
            print(f'No seu estoque tem {quantidade[i]} {produtos[i]}')
        except:
            print("Valor inválido, nada foi adicionado")