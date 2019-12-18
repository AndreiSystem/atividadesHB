from model.produtos_classe import ProdutosClasse
from dao.produtos_dao import ProdutosDao

lista = [
    ['frutas', 'verduras', 'legumes', 'preço'],
    ['mamão', 'abacaxi', 'laranja', 'uva', 'pera', 'maçã', 'vergamota'],
    ['alface crespa', 'alface lisa', 'rúcula',
     'almeirão', 'repolho', 'salsinha', 'couve'],
    ['feijão', 'ervinha', 'lentilha', 'vagem',
     'feijão branco', 'grão de bico', 'soja'],
    [[10.00, 2.56, 5.25, 9.5, 10.05, 15, 5.75], [2.99, 2.95, 3.5, 3.25, 5.89, 2.9, 2.5],
     [9.0, 5.0, 7.5, 1.75, 10.9, 5.99, 3.55]
     ]
]


p = ProdutosDao()
mercado = ProdutosClasse()

# cadastrando legumes:
l = 0

for i in lista[4][0]:
    legumes = mercado.set_legumes(lista[3][l])
    preco = mercado.set_preco(i)

    if p.existe_produto(mercado.legumes):
        print('legumes já cadastrado!')
        break
    p.inserir_legumes(mercado.legumes, mercado.preco)
    l += 1


# cadastrando frutas:
f = 0
for i in lista[4][1]:
    frutas = mercado.set_frutas(lista[1][f])
    preco = mercado.set_preco(i)

    if p.existe_produto(mercado.frutas):
        print('frutas já cadastrada!')
        break
    p.inserir_frutas(mercado.frutas, mercado.preco)
    f += 1

# cadastrando verduras:
v = 0
for i in lista[4][2]:
    verduras = mercado.set_verduras(lista[2][v])
    preco = mercado.set_preco(i)

    if p.existe_produto(mercado.verduras):
        print('verduras já cadastrada!')
        break
    p.inserir_verduras(mercado.verduras, mercado.preco)
    v += 1
