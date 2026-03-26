#declaração de variaveis
venda_mensal: int = 0
preco_atual: float = 0.0
#inicio
def main():
    preco_atual =  float(input('Digite o preço atual do produto: '))
    venda_mensal = float(input('Digite a media mensal do produto: '))
    novopreco(venda_mensal, preco_atual)

def novopreco(venda_mensal, preco_atual):
    if venda_mensal < 500 and preco_atual < 30.00:
        preco_novo = preco_atual * 1.10
    elif venda_mensal >= 500 and venda_mensal < 1000 and preco_atual >= 30.00 and preco_atual < 80.00:
        preco_novo = preco_atual * 1.15
    elif venda_mensal >= 1000 and preco_atual >= 80.00:
        preco_novo =  preco_atual * 0.95
    else:
        preco_novo = preco_atual
    print('Novo preço do produto:', preco_novo,)

if  __name__ == "__main__":
    main()
#fim