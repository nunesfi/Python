class Humano:
    #atributo de classe
    especie= 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Sapiens_2'
        return self

    #metodo estático não recebe parametros
    @staticmethod
    def especies():
        adjetivos = ('Habilis' , 'Erectus', 'Neanderthalensis', 'Sapiens')
        return('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    # metodo de classe recebe a Classe como primeiro parametro - Param: cls padrão
    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]

    #metodo de instancia recebe o self

class Neanderthal(Humano):
    especie = Humano.especies()[-2]

class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

if __name__ == '__main__':
    jose = HomoSapiens('José')
    Grokn = Neanderthal('Grokn')
    print(f'Evolução (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(f'Evolução (a partir da instancia): {", ".join(jose.especies())}')
    print(f'Homo Sapiens evoluido? {HomoSapiens.is_evoluido()}')
    print(f'Neanderthal evoluido? {Neanderthal.is_evoluido()}')
    print(f'José evoluido? {jose.is_evoluido()}')
    print(f'Grokn evoluido? {Grokn.is_evoluido()}')

