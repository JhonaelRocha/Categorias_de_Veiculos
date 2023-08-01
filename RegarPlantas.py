
# Jhonael Rocha
# P. Vinícius Oliveira
# Luiz Valença Filho

numPlantas = 0
planta = ""
qntPlantas = 0
try:
    qntPlantas = int(input("Quantas plantas você tem? : "))
except Exception as erro:
    print("Valor inválido : " + str(erro))
while numPlantas < qntPlantas:
    if numPlantas % 2 == 0:
        planta = "Batata"
    else:
        planta = "Tomate"
    print(f'Regou a planta : {planta} na posição {numPlantas}')
    numPlantas = numPlantas + 2

