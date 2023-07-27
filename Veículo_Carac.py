
categoria = ""

Peso = float(input("Qual o peso do seu veículo? : "))
print(str(Peso) + " Kg")

qntRodas = int(input("Quantas rodas ele tem? : "))
if qntRodas > 1 : print(str(qntRodas) + " Rodas")
elif qntRodas == 1 : print(str(qntRodas) + " Roda")

qntPessoas = int(input("Nele cabem quantas pessoas? : "))
if qntPessoas > 1 : print(str(qntPessoas) + " Pessoas")
elif qntPessoas == 1 : print(str(qntPessoas) + " Pessoa")

if qntRodas == 2 or qntRodas == 3 : 
     categoria = "A"
elif qntRodas == 4 and qntPessoas <= 8 and Peso <= 3500 :
     categoria = "B"
elif qntRodas >= 4 and Peso > 3500 and Peso <= 6000 :
     categoria = "C"
elif qntRodas >= 4 and qntPessoas > 8 :
     categoria = "D"
elif qntRodas >= 4 and Peso > 6000 :
     categoria = "E"
else :
     categoria = "Nenhuma"

print("A Categoria é : " + categoria)