#Input das variaveis
altura = int(input("Digite a sua altura em centimetros: "))
peso = float(input("Digite o seu peso: "))

#realização do calculo
imc =  peso / (altura**2)*10000

#print formatado com o imc do usuario
print("{:.2f}".format(imc)) 

#imc baixo
if imc < 18.5:
  print("MAGREZA")

#imc normal
elif imc >= 18.5 and imc <= 24.9:
  print("NORMAL")

#imc alto
elif imc >= 25 and imc <= 29.9:
  print("SOBREPESO")
  print("Obesidade I")

#imc alto
elif imc >= 30 and imc <= 39.9:
  print("OBESIDADE")
  print("Obesidade II")

#imc alto
else:
  print("OBESIDADE GRAVE")
  print("Obesidade III")
