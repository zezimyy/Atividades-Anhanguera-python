num = input("Digite 20 numeros separados por espaço: ").split()

par = []
impar = []

for c in num:
  if int(c) % 2 == 0:
    par.append(c)
  else:
    impar.append(c)

print("Par: {}".format(par))
print("Impar: {}".format(impar))
