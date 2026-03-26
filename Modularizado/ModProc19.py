#declaração de variaveis
a: float = 0.0
b: float = 0.0
#inicio
def main():
    global a,b
    a = float(input('Digite um número real: '))
    b = float(input('Digite um número real: '))
    maior()

def maior():
     if a > b:
         print(f'Maior valor: {a}')
     else:
         print(f'Maior valor: {b}')

if __name__ =='__main__':
    main()
#fim