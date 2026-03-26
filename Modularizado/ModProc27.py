#declaração de variaveis
voltas: float = 0.0
extensao: float = 0.0
tempo: float = 0.0
def main():
    voltas = float(input('Digite a quantidade de voltas:'))
    extensao = float(input('Digite a extensão do circuito (metros):'))
    tempo = float(input('Digite o tempo de duração (minutos):'))
    velocidade(voltas, extensao, tempo)

def velocidade(voltas,extensao,tempo):
    distancia = (voltas * extensao) / 1000
    tempo = tempo / 60
    velocidade = distancia  / tempo
    print('A velocidade media foi:', velocidade, 'km/h')

if __name__ == '__main__':
    main()
#fim