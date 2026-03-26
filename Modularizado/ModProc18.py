#definição de variaveis
result: int = 0
a: int = 0
b: int = 0
#inicio
def main():
    global a, b 
    a = int(input('Digite um número: '))
    b = int(input('Digite um número: '))
    diferenca()

def diferenca():
        if a > b:
            result = a - b
        else: 
            result = b - a
        print(f'A diferença do maior pelo menor é: {result}')
if __name__ =='__main__':
    main()
#fim