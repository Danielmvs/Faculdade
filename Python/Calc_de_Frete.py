def dimensoesObjeto():
    while True:
        try:
            largura = float(input('Digite a largura do Objeto em cm: '))
            altura = float(input('Digite a altura do Objeto em cm: '))
            comprimento = float(input('Digite o comprimento do Objeto em cm: '))
            dimensao = altura * largura * comprimento
            # Foi utilizado uma lista dentro de lista para representar os intervalos
            calcDimensoes = [
                [0, 1000],
                [1000, 10000],
                [10000, 30000],
                [30000, 100000]
            ]
            # o indice do intervalo e igual ao indice dos valores, portanto se a dimensão estiver entre o intervalo valerá o valor referenciado
            valor = [10, 20, 30, 50]
            # O loop for é utilizado para navegar entre as listas de dentro e verificar se a dimensão está entre o intervalo
            # caso seja verdadeiro a variavel valorPago recebe o valor no indice que o intervalo foi localizado
            for indice, intervalo in enumerate(calcDimensoes):
                if intervalo[0] <= dimensao < intervalo[-1]:
                    valorPago = valor[indice]
                    return valorPago, dimensao
                elif dimensao >= 100000:
                    print(f'O volume do objeto é (em cm³): {dimensao}'
                          '\nObjeto com o volume igual ou acima de 100000 cm³ não são transportado'
                          '\nAdicione um objeto com as dimensões que sejam válida')
                    break
        except ValueError:
            print('Você digitou alguma dimensão do objeto com o valor não numérico')
            print('Por favor entre com as dimensões desejadas novamente')


# a variavel valorDimensão armazena o retorno da função que é (valorPago e dimensao)
print('Bem vindo a transportadora do DANIEL MARCUS VIEIRA SANTOS RU: 3887957')
valorDimensao = dimensoesObjeto()
print('O volume do objeto é (em cm³): {}'.format(valorDimensao[1]))


def pesoObjeto():
    while True:
        try:
            # Foi utilizado uma lista dentro de lista para representar os intervalos
            peso = float(input('Digite o peso do Objeto (em kg): '))
            calcPeso = [
                [0, 0.1],
                [0.1, 1],
                [1, 10],
                [10, 30],
            ]
            # o indice do intervalo e igual ao indice do multiplicador, portanto se o peso estiver entre o intervalo valerá o valor referenciado
            mutiplicador = [1, 1.5, 2, 3]
            # loop for é utilizado para navegar entre as listas de dentro e verificar se o peso está entre o intervalo
            # caso seja verdadeiro a variavel valorMultiplicado recebe o multiplicador no indice que o intervalo foi localizado, multiplicando com o valorDimensao que ja foi encontrado anteriomente
            for indice, intervalo in enumerate(calcPeso):
                if intervalo[0] <= peso < intervalo[-1]:
                    valorMultiplicado = mutiplicador[indice] * valorDimensao[0]
                    return valorMultiplicado, peso
                elif peso >= 30:
                    print('não aceitamos objetos tão pesado')
                    break
        except ValueError:
            print('Você digitou o peso do objeto com o valor não numérico')
            print('Por favor entre com o peso desejado novamente')


# a variavel valorPeso armazena o retorno da função que é valorMultiplicado e peso
valorPeso = pesoObjeto()


def rotaObejto():
    while True:
        print(
            'Selecione a rota:\n'
            'RS - De Rio de Janeiro até São Paulo\n'
            'SR - De São Paulo até Rio de Janeiro\n'
            'BS - De Brasília até São Paulo\n'
            'SB - De São Paulo até Brasília\n'
            'BR - De Brasília até Rio de Janeiro\n'
            'RB - Rio de Janeiro até Brasília'
        )
        rotaEscolhida = input('Digite a sigla da rota desejada: ').upper()
        # foi utilizado uma lista para armazenar as rotas
        rotas = [
            'RS - De Rio de Janeiro até São Paulo',
            'SR - De São Paulo até Rio de Janeiro',
            'BS - De Brasília até São Paulo',
            'SB - De São Paulo até Brasília',
            'BR - De Brasília até Rio de Janeiro',
            'RB - Rio de Janeiro até Brasília']
        # o indice da rota e igual ao indice do multiplicadorRota
        mutiplicadorRota = [1, 1, 1.2, 1.2, 1.5, 1.5]
        # foi utilizado uma variavel de controle que recebe o valor False
        # Quando a rota escolhida entrar no loop para fazer a verificação a variavel validação recebe true e retornar os valores representados
        # caso o loop não entre na condição o valor da variavel continuará false então cairá em outra condição que faz o loop while continuar.
        validacao = False
        for indice, rota in enumerate(rotas):
            if rotaEscolhida == rota[0:2]:
                valorTotal = mutiplicadorRota[indice] * valorPeso[0]
                validacao = True
                return valorTotal, mutiplicadorRota[indice]
        if not validacao:
            print('Você digitou uma rota que não existe')
            print('Por favor entre com a rota desejado novamente')


# a variavel precoDaEntrega armazena o retorno da função que é valorTotal e multiplicadorRota[indice]
precoDaEntrega = rotaObejto()
# o print de finzalização do pedido, utilizada todos os retornos das funções que foram armazenadas em variaveis em formato de tuplas, no qual o valores são acessados por meio de incices.
print('Total a pagar(R$): {:.2f} (Dimensões: {} * Peso: {} * Rota: {})'.format(precoDaEntrega[0], valorDimensao[1],
                                                                               valorPeso[1], precoDaEntrega[1]))
print('Obrigado por confiar no trabalho da empresa do DANIEL MARCUS VIEIRA SANTOS RU: 3887957')