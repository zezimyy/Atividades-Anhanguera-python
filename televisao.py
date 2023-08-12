class Televisao:
    def __init__(self, ligado, canal=10) -> None:
        self.ligado = ligado
        self.canal = canal

tv = Televisao(False)

while True:

    #liga / desliga a televisão
    if tv.ligado == False:
        ligar = input("\nSua televisão está desligada! \ndeseja ligar? [S/N] ")

        if ligar == "S" or ligar == "s":
            tv.ligado = True
            print("\nTelevisao: {}".format(tv.ligado))
            
            print("\nA televisão está no canal {}".format(tv.canal))

            mudar_canal = input("\nDeseja mudar de canal? [S/N]")

            if mudar_canal == "S" or mudar_canal == "s":
                cima_baixo = input("\nmudar o canal para cima ou baixo? [C/B]")

                if cima_baixo == "C" or cima_baixo == "c":
                    tv.canal = tv.canal + 1
                    print(tv.canal)
    
                elif cima_baixo == "B" or cima_baixo == "b":
                    tv.canal-=1
                    print(tv.canal)
    
                elif cima_baixo == "desligar":
                    tv.ligado = False

            else:
                print()

        else:
            continue


    else:
        desligar = input("\nSua televisão ta ligada!\ndeseja desligar? [S/N] ")
        if desligar == "S" or desligar == "s":
            tv.ligado = False
            print("\nTelevisao: {}".format(tv.ligado))
            break
        
        else:
            tv.ligado = True
            print("\nA televisão está no canal {}".format(tv.canal))

            mudar_canal = input("\nDeseja mudar de canal? [S/N]")

            if mudar_canal == "S" or mudar_canal == "s":
                cima_baixo = input("\nmudar o canal para cima ou baixo? [C/B]")

                if cima_baixo == "C" or cima_baixo == "c":
                    tv.canal = tv.canal + 1
                    print(tv.canal)
    
                elif cima_baixo == "B" or cima_baixo == "b":
                    tv.canal-=1
                    print(tv.canal)
    
                elif cima_baixo == "desligar":
                    tv.ligado = False

            else:
                print()
