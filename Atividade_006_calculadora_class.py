class Calculadora:

    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2

    def somar(self):
        return self.n1+self.n2
    
    def subtrair(self):
        return self.n1-self.n2
    
    def multiplicar(self):
        return self.n1*self.n2
    
    def dividir(self):
        return self.n1/self.n2

n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))

c = Calculadora(n1, n2)

fazer = input("Oque a calculadora irá fazer? [somar, subtrair, multiplicar, dividir] ")

if fazer == "somar":
    print("{:.2f}".format(c.somar()))

elif fazer == "subtrair":
    print("{:.2f}".format(c.subtrair()))

if fazer == "multiplicar":
    print("{:.2f}".format(c.multiplicar()))

elif fazer == "dividir":
    print("{:.2f}".format(c.dividir()))
