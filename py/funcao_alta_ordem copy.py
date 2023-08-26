# Passando uma função como parametro para outra função
# Dentro de uma função passar outra função

from funca_primeira_classe import dobro, quadrado

def processar(titulo, lista, funcao):
    print(f"Processando: {titulo}")
    for i in lista:
        print(i, "=>", funcao(i))

if __name__ == "__main__":
    processar("Dobros de 1 a 10", range(1, 11), dobro)
    print(processar)

    processar("Quadrados de 1 a 10", range(1, 11), quadrado)
    print(processar)