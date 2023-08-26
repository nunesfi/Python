compras = (
    {'quantidade': 2, "preço": 10},
    {'quantidade': 3, 'preço': 20},
    {'quantidade': 5, 'preço': 14},
)

#função lambda
totais = tuple(map(lambda compra: compra['quantidade'] * compra['preço'], compras))

print('Preços totais', totais)
print('Total geral', sum(totais))

# ----------------------- Forma procedural (alternativa) --------------------------------
compras = (
    {'quantidade': 2, "preço": 10},
    {'quantidade': 3, 'preço': 20},
    {'quantidade': 5, 'preço': 14},
)

def calc_preco_total(compra):
    return compra['quantidade'] * compra['preço']

totais = tuple(map(calc_preco_total,compras))

print('Preços totais', totais)
print('Total geral', sum(totais))