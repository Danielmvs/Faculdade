print("""
LOJA DO DANIEL MARCUS VIEIRA SANTOS RU:3887957
*****************Cardapio*****************
| Código |        Descrição      | Valor |
|  100   |    Cachorro Quente    | 9,00  |
|  101   | Cachorro Quente Duplo | 11,00 |
|  102   |        X-Egg          | 12,00 |
|  103   |      X- Salada        | 13,00 |
|  104   |       X-Bacon         | 14,00 |
|  105   |        X-Tudo         | 17,00 |
|  200   |    Refrigerante Lata  | 5,00  |
|  201   |     Chá Gelado        | 4,00  |
""")
#matriz de produtos em que cada codigo referencia ao indice do item/valor
produtosValores = [
    [100, 101, 102, 103, 104, 105, 200, 201],
    ['Cachorro Quente',
     'Cachorro Quente Duplo',
     'X-Egg',
     'X-Salada',
     'X-Bacon',
     'X-Tudo',
     'Refrigerante Lata',
     'Chá Gelado'],
    [9, 11, 12, 13, 14, 17, 5, 4]
]
# a variavel outroPedido serve para manter a iteração, pois quando recebe o valor de 0 encerra o loop.
outroPedido = 1
valorTotal = 0
# foi acrescentado a variavel quantPedido para armazenar todos os pedidos que forem solicitados e no final listar os mesmo
quantPedido = []
while outroPedido == 1:
    pedido = int(input('Entre com o código desejado:  '))
    if pedido in produtosValores[0]:
        # a variavel codigo recebe o indice do pedido, no qual é usada para localizar os outros indeces relacionado.
        codigo = produtosValores[0].index(pedido)
        lanche = produtosValores[1][codigo]
        valorDoLanche = produtosValores[2][codigo]
        print('Você pediu um {} no valor de R${} reais'.format(lanche, valorDoLanche))
        valorTotal += valorDoLanche
        # a variavel quantPedido é utilizada para armazenar os pedidos solicidados.
        quantPedido.append([lanche, valorDoLanche])
        outroPedido = int(input('Deseja pedir mais alguma coisa?\n 1 - Sim\n 0 - Não\n'))
        if outroPedido == 1:
            continue
        elif outroPedido == 0:
            print('O pedido total foi de R${} Reais!\n ********Lista de Pedidos*********'.format(valorTotal))
            # a varialvel 'tam' recebe o tamanho da lista que é armazenada em 'quantPedidos' a cada novo pedido.
            tam = len(quantPedido)
            # a variavel indice é resposável que o loop percorra toda a lista, assim obetendo os dados do pedido
            indice_RU3887957 = 0
            # a variavel contador enumera os pedidos
            contador = 1
            # O laço de reptição foi criado para listar os pedidos ao finalizar a compra
            while tam >= 1:
                print('+', '-' * 40, '+')
                print('| Pedido {}° {} - R${} '.format(contador, quantPedido[indice_RU3887957][0],
                                                                quantPedido[indice_RU3887957][1]))
                indice_RU3887957 += 1
                tam -= 1
                contador += 1
            print('+', '-' * 40, '+')
            break
            # foi utilizado um loop while, no qual é utilizado para permanecer no loop enquanto não digitar um valor valido.
        while outroPedido not in [0, 1]:
            print('!!!Digite somente o valor 0 ou 1 !!!')
            outroPedido = int(input('Deseja pedir mais alguma coisa?\n 1 - Sim\n 0 - Não\n'))
    else:
        print('!!!Digite um codigo válido!!!')
        continue