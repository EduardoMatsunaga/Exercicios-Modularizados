h_ini: int = 0
m_ini: int = 0
h_fim: int = 0
m_fim: int = 0
duracaoM: float = 0.0
tempo_min_ini: float = 0.0
tempo_min_fim: float = 0.0
horas: int = 0
minu: int = 0
#inicio
def main():
    global h_ini, h_fim, m_ini, m_fim,  tempo_min_ini, tempo_min_fim
    h_ini = int(input('Digite a hora de inicio do jogo:'))
    m_ini = int(input('Digite os minutos de inicio do jogo:'))
    h_fim = int(input('Digite a hora que acabou o jogo:'))
    m_fim = int(input('Digite os minutos que acabou o jogo:'))
    tempo_min_ini = h_ini * 60 + m_ini
    tempo_min_fim = h_fim * 60 + m_fim
    tempojogo()

def tempojogo():
    if tempo_min_ini < tempo_min_fim: 
        duracaoM = tempo_min_fim - tempo_min_ini
    else:
        duracaoM = (1440 - tempo_min_ini) + tempo_min_fim
    horas = duracaoM //  60
    minu = duracaoM % 60
    print(f'A duração do jogo foi de {horas} horas : {minu} minutos.')

if __name__ == '__main__':
    main()
#fim