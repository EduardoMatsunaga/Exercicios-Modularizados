#definição de variaveis
delta: float = 0.0
a: float = 0.0
b: float =  0.0
c: float = 0.0
x1: float = 0.0
x2: float = 0.0
#inicio
def main():
    global a, b, c, delta
    a = float(input('Digite o valor de A: '))
    b = float(input('Digite o valor de B: '))
    c = float(input('Digite o valor de C: '))
    delta =  ((b*b) - 4  *  a *  c)
    raiz()

def raiz():
    if delta >= 0:
        x1 = ((-b - delta**0.5) / 2  *  a)
        x2 = ((-b + delta**0.5)  /  2 * a)
        print(f'As raizes são: {x1} , {x2}')
    else:
        x1 = ((-b - delta**0.5) / 2  *  a)
        x2 = ((-b + delta**0.5)  /  2 * a)
        print('Não possui raizes reais')
        
if __name__ =='__main__':
    main()
#fim