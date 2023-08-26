# Armazenando funções dentro de ambiente que seriam armazenado por dados (variáveis)

def dobro(x):
    return x * 2

def quadrado(x):
    return x ** 2

if __name__ == '__main__':
    #Forma 1
    d = dobro
    print('O dobro d 5 é: ', d(5))

    q= quadrado
    print('O quadrado d 5 é: ', q(5))
    
    # retornar alteranadamente o dobro ou quadrado nos numero de 1 a 10
    # coloquei as funções em uma lista e multipliquei por 5(repetições)
    # variando entre dobro e quadrado
    # colocamos a função zip para juntar as funções e variar num range de 1 a 11

    funcs = [dobro, quadrado] * 5
    for func, numero in zip(funcs, range(1, 11)):
        print(f'O {func.__name__} de {numero} é {func(numero)}')