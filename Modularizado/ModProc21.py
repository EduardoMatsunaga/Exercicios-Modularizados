#definição de  variaveis
media: float  = 0.0
n1: float = 0.0
n2: float = 0.0
n3: float = 0.0
n4: float = 0.0
#inicio
def main():
    global n1, n2, n3, n4
    n1 = float(input('Digite a sua nota:'))
    n2 = float(input('Digite a sua nota:'))
    n3 = float(input('Digite a sua nota:'))
    n4 = float(input('Digite a sua nota:'))
    med()

def med():
    global n1, n2, n3, n4, media
    media = (n1 + n2 + n3 + n4) / 4
    if media >= 6.0:
        print('Aprovado')
    elif media >= 3.0 and media < 6.0:
        print('Exame')
    else:
        print('Retido')
if __name__ =='__main__':
    main()
#fim