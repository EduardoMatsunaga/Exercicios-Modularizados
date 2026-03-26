#declaração de variaveis
x: int = 0
#inicio
def main():
    global x
    x = int(input('Digite um valor inteiro:'))
    divisivel()

def divisivel():
    if (x % 2 == 0) and (x % 3 == 0):
        print('É divisivel por 2 e 3')
    else:
        print('Não é divisivel por 2 e 3')

if __name__ == '__main__':
    main()
#fim