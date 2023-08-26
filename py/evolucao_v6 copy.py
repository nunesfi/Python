from abc import ABCMeta, abstractproperty

class Humano(metaclass=ABCMeta):
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    #classe abstrata
    @abstractproperty
    def inteligente(self):
        pass

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

    @property
    def inteligente(self):
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligente(self):
        return True


if __name__ == '__main__':
    

    try:
        anonimo = Humano('Filipi')
        print(anonimo.inteligente)
    except TypeError:
        print('classe abstrata')

    jose = HomoSapiens('José')
    print('{} da classe {}, inteligente: {}'.format(jose.nome,
        jose.__class__.__name__, jose.inteligente))