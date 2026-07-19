#Declaração  de Classe
class Gafanhoto:
    """
    Essa classe cria um gafanhoto que e uma pessoa que tem nome e idade

    Para criar uma nova pessoa, use
    variavel =  Gafanhoto(nome,idade)

    """
    def __init__(self,n = "vazio",i = 0): #Método construtor
        #Atributos de Instância
        self.nome = n
        self.idade = i

    #Métodos de Instância
    def aniversario(self):
        self.idade += 1
    def __getstate__(self):
        return f"Estado: nome = {self.nome}; idade = {self.idade}"
    def __str__(self): ##Dunder Method
        return f"{self.nome} e gafanhoto e tem {self.idade} anos de idade"
    
# Declaração de objetos
g1 = Gafanhoto("maria", 17)
g1.aniversario()
#print(g1.__doc__) #Dunder Attribute
#print(g1)
#print(g1.__dict__)
#print(g1.__getstate__())
print(g1.__class__)
#g2 = Gafanhoto("Mauro", 54)
#print(g2)
#print(g2.__getstate__())