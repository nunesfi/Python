class RGB:
    def __init__(self):
        # retornando as cores basicas / interação do ultimo p o primeiro [::-1]
        # função pop - pega o valor e remove o ultimo
        self.cores = ['red', 'green', 'blue'][::-1]

    
    #interator
    def __next__(self):
        try:
            #retorna o pŕoximo elemento
            return self.cores.pop()
        except IndexError:
            raise StopIteration()

if __name__ == "__main__":
    cores = RGB()
    print(next(cores))
    print(next(cores))
    print(next(cores))

# criado este tratamento de erro, pois a função next retorna o elemento e remove da lista
# com isso chegou um momento em que não iria retornar nada e iria retornar o INdex Error
    try:
        print(next(cores))
    except StopIteration:
        print('Acabou!')