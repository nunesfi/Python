class HtmlStringMixin:
    def __str__(self):
        #Conversão para HTML
        html = super().__str__() \
            .replace('(', '<strong>(') \
            .replace(')', ')</strong>')
        return f'<spam>{html}</spam>'

class Pessoa:
    def __init__(self, nome) -> None:
        self.nome = nome

    #convertendo p/ string
    def __str__(self):
        return self.nome

class Animal:
    def __init__(self, nome, pet=True):
        self.nome = nome
        self.pet = pet

    #Retorna o nome + o PET se sel.pet = True
    def __str__(self): 
        return self.nome + ' pet' if self.pet else ''  

# Cuidados com a ordem de inclusão p/ mixins de classe
# A primeira a ser chamada junta-se com a segunda classe chamada
class PessoHtml(HtmlStringMixin, Pessoa):
    pass

class AnimalHtml(HtmlStringMixin, Animal):
    pass

if __name__ == '__main__':
    p1 = Pessoa('Filipi')
    print(p1)

    p2 = PessoHtml('Nunes')
    print(p2)

    p3 = AnimalHtml('Paçoca')
    print(p3)