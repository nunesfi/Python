class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade dever ser um número positivo')
        self._idade = idade

    def das_cavernas(self):
        self.especie = 'Homo Sapiens_2'
        return self

    # metodo estático não recebe parametros
    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    # metodo de classe recebe a Classe como primeiro parametro - Param: cls padrão
    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]

    # metodo de instancia recebe o self


class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('José')
    jose.idade = 40
    print(f'Nome: {jose.nome} Idade {jose.idade}')