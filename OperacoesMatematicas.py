# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a  operação a ser executada. Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão

# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.
numero1 = float(input("Digite o primeiro número : "))
numero2 = float(input("Digite o segundo número : "))
print("1.soma")
print("2.subtração")
print("3.multiplicação")
print("4.divição")
operacao = int(input("Digite a operação : "))

def calcular(num1,num2,operador):
   if operador == 1:
      print(num1 + num2)
   elif operador == 2:
      print(num1 - num2)
   elif operador == 3:
      print(num1 * num2)
   elif operador == 4:
      print(num1 / num2)
   else:
      print("0, a opeção é inválida")
calcular(numero1,numero2,operacao)
