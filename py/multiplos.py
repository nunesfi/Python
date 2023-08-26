# Herança Multipla

class Animal:
    @property
    def capacidades(self):
        return ('dormir', 'comer', 'beber')

class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('amar', 'falar', 'estudar')

class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('criar teias', 'andar pelas paredes')

#A classe homem aranha rece gerança multipla
# quando chamar a função capacidades, será chamada todos os atributos de todas "capacidades"
#Tomar cuidado com a herança multipla
class HomemAranha(Homem, Aranha):
    @property
    def capacidades(self):
        return super().capacidades + \
            ('bater em bandidos', 'atirar teias em prédios')

if __name__ == "__main__":
    filipi = Homem()
    print(f'Homem {filipi.capacidades}')

    aranha = Aranha()
    print(f'Aranha {aranha.capacidades}')

    peter = HomemAranha()
    print(f'Peter Homem Aranha: {peter.capacidades}')