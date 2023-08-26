def mapear(funcao, lista):
    for i in lista:
        yield funcao(i)

if __name__ == '__main__':
    print(list(mapear(lambda x: x ** 2, [2, 3, 4])))