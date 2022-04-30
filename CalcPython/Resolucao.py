print('ESCOLHA SUA OPERAÇÃO: ')
print()
print('1-soma \n2-divisao \n3-multiplicação \n4-subtração')
print()
operacao = int(input('Digite um número: '))
if operacao == 1:
    print('A operação escolhida foi Soma!')
elif operacao == 2:
    print('A operação escolhida foi Divisão!')
elif operacao == 3:
    print('A operação escolhida foi Multiplicação!')
elif operacao == 4:
    print('A operação escolhida foi Subtração!')
print()
num1 = int(input('Digite o Primeiro número para a calculadora: '))    
num2 = int(input('Digite o Segundo número para a calculadora: '))
if operacao == 1: 
    print(num1 + num2)
elif operacao == 2:
    print(num1 / num2)
elif operacao == 3:
    print(num1 * num2)
elif operacao == 4:
    print(num1 - num2)

