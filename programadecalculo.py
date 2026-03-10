#programadecalculo
#geraldo
#2026

print(" ################################################################# ")
print("                      CALCULADORA 2000                             ")
print(" ################################################################# ")

op = input ("Digite 1-SOMA , 2-SUBTRAÇÃO , 3-MULTIPLICAÇÃO , 4-DIVISÃO , 5-POTENCIAÇÃO , 6-RADICIAÇÃO")
op = int(op)


a = input ("Entre com o 1º número")
a = int(a)

if op == 6:
	pass
else:
	b = input ("entre com o 2º número")
	b = int(b)
	

if (op == 1):
	print(a + b)

elif (op == 2):
	print(a - b)

elif (op == 3):
	print(a * b)

elif (op == 4):
	print(a / b)

elif (op == 5):
	print(a ** b)

elif (op == 6):
	print(a ** (1/2))


else: 
	print ("Digite um número válido e tente novamente.")
print ("Obrigado por usar a calculadora 2000.")

input()

