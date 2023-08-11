lista = input("Digite 5 numeros separados por espaço: ").split()
soma = 0
multiplicacao = 1

for i in lista:
  i = int(i)
  soma = soma + i
for i in lista:
  i = int(i)
  multiplicacao = multiplicacao * i

print(soma)
print(multiplicacao)
print(lista)
