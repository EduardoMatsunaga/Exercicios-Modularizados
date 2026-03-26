#declaração de variaveis
x: int = 0
y: int = 0
result: int = 0
#inicio
def main():
    global x, y, result
    x = int(input('Digite um numero:'))
    y = int(input('Digite um  numero:'))
    multiplo()

def multiplo():
    if x > y:
        if x % y == 0:
            print(f'{x} é maior e multiplo de {y}')
        else:
            print(f'{x} é maior que {y}')
    elif y > x:
        if y % x == 0:
            print(f'{y} é maior e multiplo de {x}')
        else:
            print(f'{y} é maior que {x}')
    else:
        print('Numeros iguais')

if __name__ == '__main__':
    main()
#fim