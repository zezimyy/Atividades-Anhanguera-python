salario = float(input("Digite seu salario: "))

if salario <= 280:
    incremento = 0.20
elif salario >= 280.01 and salario <= 700:
    incremento = 0.15
elif salario >= 700.01 and salario <= 1500:
    incremento = 0.10
else:
    incremento = 0.05
    
print("Salario antes do reajuste: {}".format(salario))
print("Aumento de {}%".format(incremento*100))
print("Ouve um aumento de {} reais".format(salario*incremento))
print("O seu novo salario é de {} reais".format((salario*incremento)+salario))
