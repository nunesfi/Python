class Humano:
    #atributo de classe
    especie= 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Sapiens_2'
        return self

if __name__ == '__main__':
    jose = Humano('José')
    Gront = Humano('Gront').das_cavernas()

    print(f'Humano.especie: {Humano.especie}')
    print(f'jose.especie {jose.especie}')
    print(f'Gront.especie {Gront.especie}')
    
