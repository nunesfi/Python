def cores_arco_iris():
    yield "vermelho"
    yield "laranja"
    yield "amarelo"
    yield "verde"
    yield "azul"
    yield "índigo"
    yield "violeta"

if __name__ == '__main__':
    generation = cores_arco_iris()
    print(type(generation))

    while True:
        print(next(generation))


