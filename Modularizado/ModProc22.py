#declaração de variaveis
a: int = 0.0
b: int = 0.0
#inicio
def main():
    global a, b
    a = int(input('Digite um número: '))
    b = int(input('Digite um número: '))
    cres()

def cres():
    if a > b:
        print(f'Valores em ordem crescente: {b} , {a}')
    else:
        print(f'Valores em ordem crescente: {a} , {b}')
if __name__ == '__main__':
    main()
#fim