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


def buscar_tipo(produtos):
    print("""
    Bem Vindo ao seu Mercado Online!
    Opções do Mercado:
    0 - Sair
    1 - Verduras
    2 - Frutas
    3 - Legumes
    """)

    while True:
        escolha = int(
            input('Selecione a categoria que você quer dar uma olhada: '))

        if escolha == 1:
            print(produtos.listar_por_tipo(escolha))
            print()
        elif escolha == 2:
            print(produtos.listar_por_tipo(escolha))
            print()
        elif escolha == 3:
            print(produtos.listar_por_tipo(escolha))
            print()
        elif escolha == 0:
            print('Pesquisa finalizada!')
            break
        else:
            print()
            print('Essa Opção não está disponível no momento.')
            print()


buscar_tipo(p)
