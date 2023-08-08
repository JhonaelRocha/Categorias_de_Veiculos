# Ricardo Simines - Tiago Lima Reis - Jhonael Rocha

nomes = ["Júlio","Vitor","Gabriela","Suelem","Ricardo","Tiago"]

def achar_nome(arr):
  nome = (input("Digite o seu nome : ")).title()
  print(nome)
  achou = False

  for i in range(len(arr)):

    if arr[i] == nome:
      achou = True
      
  if(achou == False):
    print("Nâo achamos o nome " + nome)
  else:
    print("Achamos o nome: " + nome)

achar_nome(nomes)