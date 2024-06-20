print('BEM VINDO A LOJA DO DANIEL MARCUS VIEIRA SANTOS RU: 3887957')
valorProd = float(input('Digite o valor do Produto: '))
quantProd = int(input('Digite a quantidade do Produto: '))
valorSemDesc = valorProd * quantProd

if(quantProd < 10):
     # A Variavel info armazena o valor das unidades que faltam para chegar a 10, para que no print mostre a informação.
     info_RU3887957 = 10 - quantProd
     print('Caso queira ganhar 5% de desconto no valor total é so acrescentar {} unidade a mais'. format(info_RU3887957))
     print('O valor do produto sem desconto foi de: R$ {}'.format(valorSemDesc))
    # o calculo da porcentagem e do valor sem com desconto foi implementado diretamente no .format()
elif(quantProd >= 10 and quantProd < 100):
     print('O valor do produto sem desconto foi de: R$ {}'.format(valorSemDesc))
     print('O valor do produto com desconto foi de: R$ {}  (Desconto 5%)'.format(valorSemDesc - (valorSemDesc * 0.05)))

elif (quantProd >=100 and quantProd < 1000):
     print('O valor do produto sem desconto foi de: R$ {}'.format(valorSemDesc))
     print('O valor do produto com desconto foi de: R$ {}  (Desconto 10%)'.format(valorSemDesc - (valorSemDesc * 0.10)))
else:
     print('O valor do produto sem desconto foi de: R$ {}'.format(valorSemDesc))
     print('O valor do produto com desconto foi de: R$ {}  (Desconto 15%)'.format(valorSemDesc - (valorSemDesc * 0.15)))