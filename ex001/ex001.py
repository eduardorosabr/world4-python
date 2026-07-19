#Declaração  de Classe
class Gafanhoto:
    def __init__(self): #Método construtor
        #Atributos de Instância
        self.nome = ""
        self.idade = 0

    #Métodos de Instância
    def aniversario(self):
        self.idade += 1
    def mensagem(self):
        return f"{self.nome} é gafanhoto e tem {self.idade} anos de idade"
    
# Declaração de objetos
g1 = Gafanhoto()
g1.nome = "maria"
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Mauro"
g2.idade = 52
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())