media1 = float(input("Digite a media n 1°: "))
media2 = float(input("Digite a media n 2°: "))
media = (media1+media2)/2

if media <= 3.9:
  print("E")
  print("Reprovado!")
  
elif media >= 4 and media <= 5.9:
  print("D")
  print("Reprovado!")
  
elif media >= 6 and media <= 7.4:
  print("C")
  print("Aprovado!")
  
elif media >= 7.5 and media <= 8.9:
  print("B")
  print("Aprovado!")

else: 
  print("A")
  print("Aprovado!")
