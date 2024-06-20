contador = 1
dadosProduto = []


def cadastrarPeca():
    sair = True
    while sair:
        global contador
        # foi criado um dicionario dados para ser manipulado somente dentro da função.
        #(FOI ADICIONADO O MEU RU NO NOME DO DICIONARIO POIS NÃO INTERFERE NO PROGRAMA)
        dados_RU3887957 = {}
        # a varialvel contador é utilizada como o código do produto, pois a cada uso da função ele recebe + 1.
        print('Codigo da peça {:02}'.format(contador))
        dados_RU3887957['codigo'] = contador
        dados_RU3887957['nome'] = input('Por favor entre com o NOME da peça: ')
        dados_RU3887957['fabricante'] = input('Por favor entre com o FABRICANTE da peça: ')
        #foi utilizado o try para tratamento de erros no input do valor.
        try:
            dados_RU3887957['valor'] = float(input('Por favor entre com o Valor(R$) da peça: '))
            print('Peça cadastrada com sucesso!')
            # a array dadosProduto recebe uma copia do dicionario dados.
            dadosProduto.append(dados_RU3887957.copy())
            contador += 1
            # a varialvel de controle recebe false para sair do loop e encerra a função.
            sair = False
        except ValueError:
            print('Você digitou um valor não numérico no valor do produto')
            print('Entre com um valor numérico')


def consultarPeca():
    print('Você Selecionou a Opção de Consultar Peças')
    # a variavel de controle retornar é utilizada para encerrar o loop e voltar para o programa principal
    retornar = True
    while retornar:
        # foi utilizado o try para tratamento de erros caso o usuário escreva um valor não numérico
        try:
            opcoes = int(input('-----------------------------------\n'
                               'Escolha a Opção Desejada:\n'
                               '1 - Consultar Todas as Peças\n'
                               '2 - Consultar Peça por Código\n'
                               '3 - Consultar Peças por fabricante\n'
                               '4 - Retornar\n'
                               'R: '))
            if opcoes == 1:
                # a primeira condição serve para verificar se dadosProdutos está vazio, assim evitando entrar no codigo abaixo.
                if dadosProduto == []:
                    print('Não existe produtos para consultar.')
                    break
                # for é utilizado para passar sobre a lista e o outro for e para passar no dicionário imprimindo chave/valor.
                for x in dadosProduto:
                    print('-' * 20)
                    for i, j in x.items():
                        print('{} : {}'.format(i, j))

            elif opcoes == 2:
                sair = True
                while sair:
                    # a primeira condição serve para verificar se dadosProdutos está vazio, assim evitando entrar no codigo abaixo.
                    if dadosProduto == []:
                        print('Não existe peças para consultar')
                        break
                    # foi utilizado o try para tratamento de erros no input do codigo.
                    try:
                        # foi acrescentado um modo de sair para o usuário, pois se o mesmo não souber nenhum código ficará em um loop infinito.
                        codigo = int(input('Digite o Código desejado ou digite 0 para SAIR: '))
                        if codigo != 0:
                            for peca in dadosProduto:
                                if peca['codigo'] == codigo:
                                    print('-' * 20)
                                    for i, j in peca.items():
                                        print('{} : {}'.format(i, j))
                                    # apos o término do loop 'for', a variavel sair recebe False para interromper o loop while dentro da condição.
                                    sair = False
                                    break
                            else:
                                print('Este código não existe!')
                        # se o input do usuário for igual a 0, sair recebe false e encerra o loop while dentro da condição
                        else:
                            sair = False
                    except ValueError:
                        print('Digite um código com valor numérico')

            elif opcoes == 3:
                sair = True
                while sair:
                    # a primeira condição serve para verificar se dadosProdutos está vazio, assim evitando entrar no codigo abaixo.
                    if dadosProduto == []:
                        print('Não existe peças para consultar')
                        break
                    # foi acrescentado um modo de sair para o usuário, pois se o mesmo não souber nenhum nome de fabricante ficará em um loop infinito.
                    fabricante = input('Insira o nome do Fabricante ou digite 0 para SAIR: ').lower()
                    # foi adicionado uma variável de controle 'encontrado' para caso o input não entre no loop
                    # a variavel permanece False e caia no 'if not' assim repetindo
                    encontrado = False
                    if fabricante != '0':
                        for peca in dadosProduto:
                            if peca['fabricante'].lower() == fabricante:
                                print('-' * 20)
                                for i, j in peca.items():
                                    print('{} : {}'.format(i, j))
                                # apos o término do loop 'for', a variavel sair recebe False para interromper o loop dentro da condição.
                                # e a variavel encontrar recebe True para não imprimir o if not no final do loop.
                                encontrado = True
                                sair = False
                        if not encontrado:
                            print('Fabricante não cadastrado')
                    # se o usuário digitar 0, sair recebe false e encerra o loop da condição
                    else:
                        sair = False
            elif opcoes == 4:
                #se o input foi igual a 4 encerra o loop da função e retorna para o programa principal.
                retornar = False

            else:
                #caso o usuário digitar um numero diferente dos relacionados.
                print('Digite somente os valores representados')
                continue

        except ValueError:
            print('Você digitou um valor não Numérico')
            print('Entre com um valor Numérico')


def removerPeca():
    print('Você Selecionou a Opção de Remover Peças')
    sair = True
    while sair:
        # a primeira condição serve para verificar se dadosProdutos está vazio, assim evitando entrar no codigo abaixo.
        if dadosProduto == []:
            print('Não existe peças para remover')
            break
        # foi acrescentado um modo de sair para o usuário, pois se o mesmo desisir de remover alguma peça poderar retornar.
        # foi utilizado o try para tratamento de erro.
        try:
            codigo = int(input('Insira o codigo da peça que deseja remover ou digite 0 para SAIR: '))
            if codigo != 0:
                for peca in dadosProduto:
                    if peca['codigo'] == codigo:
                        # se a condição der verdadeira a peça que foi encontrada será removida usando o remove().
                        dadosProduto.remove(peca)
                        print('Peça removida com sucesso')
                        # apos o término do loop 'for', a variavel sair recebe False para interromper o loop dentro da condição.
                        sair = False
                        break
                else:
                    print('Este código não existe!')
            # se o usuário digitar 0, sair recebe false e encerra o loop da condição
            else:
                sair = False
        except ValueError:
            print('Digite um código com valor numérico')

##Programa Principal##

print('Bem vindo a Loja de Bicicleta do DANIEL MARCUS VIEIRA SANTOS RU 3887957')
sair = True

while sair:
    # o loop while é utilizado para navegar entre as funções
    # o usuário chama a função pelo input e dentro da função sera tratado a solicitação
    # caso o usuário queira encerrar o programa é so digitar 4 que variavel sair revebe false e ecerra o programa.
    try:
        opcoesEntrada = int(input('------------------------------\n'
                                  '1 - Cadastrar Peças\n'
                                  '2 - Consultar Peças\n'
                                  '3 - Remover Peça\n'
                                  '4 - Sair\n'
                                  'R: '))
        if opcoesEntrada == 1:
            cadastrarPeca()
        elif opcoesEntrada == 2:
            consultarPeca()
        elif opcoesEntrada == 3:
            removerPeca()
        elif opcoesEntrada == 4:
            sair = False
        else:
            print('Digite somente os valores representados')
            continue
    except ValueError:
        print('Você digitou um valor não Numérico')
        print('Entre com um valor Numérico')
