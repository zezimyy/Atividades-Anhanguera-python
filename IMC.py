altura = int(input("Digite a sua altura em centimetros: "))
peso = float(input("Digite o seu peso: "))
imc =  peso / (altura**2)
imc = imc*10000
print("{:.2f}".format(imc)) 

if imc < 18.5:
  print("MAGREZA")
elif imc >= 18.5 and imc <= 24.9:
  print("NORMAL")
elif imc >= 25 and imc <= 29.9:
  print("SOBREPESO")
  print("Obesidade I")
elif imc >= 30 and imc <= 39.9:
  print("OBESIDADE")
  print("Obesidade II")
else:
  print("OBESIDADE GRAVE")
  print("Obesidade III")
