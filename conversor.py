import os
os.system('cls' or 'clear')
def decimal_to_base(decimal, base):
    digits = []
    while decimal > 0:
        digits.append(decimal % base)
        decimal //= base
    return ''.join([str(digit) for digit in digits[::-1]])

def base_to_decimal(number, base):
    number = number[::-1]
    decimal = 0
    for i in range(len(number)):
        digit = int(number[i], base)
        decimal += digit * (base ** i)
    return decimal

def dados_projeto():
    print("Curso: Ciência da Computação")
    print("Componentes do grupo: Fulano, Beltrano e Ciclano")
    print("Disciplinas envolvidas: Algoritmos e Programação, Matemática Discreta")
    print("Versão do aplicativo: 1.0")

def converter():
    while True:
        print("Selecione a operação que deseja realizar:")
        print("1. Conversão de decimal para binário, octal e hexadecimal")
        print("2. Conversão de binário, octal e hexadecimal para decimal")
        print("3. Exibir dados do projeto")
        print("4. Encerrar aplicação")
        opcao = input("Digite a opção desejada (1, 2, 3 ou 4): ")
        if opcao == '1':
            decimal = int(input("Digite o número decimal que deseja converter: "))
            print(f"O número {decimal} em binário é: {decimal_to_base(decimal, 2)}")
            print(f"O número {decimal} em octal é: {decimal_to_base(decimal, 8)}")
            print(f"O número {decimal} em hexadecimal é: {decimal_to_base(decimal, 16)}")
        elif opcao == '2':
            base = int(input("Digite a base do número que deseja converter (2, 8 ou 16): "))
            number = input("Digite o número que deseja converter: ")
            print(f"O número {number} em decimal é: {base_to_decimal(number, base)}")
        elif opcao == '3':
            dados_projeto()
        elif opcao == '4':
            print("Encerrando aplicação...")
            break
        else:
            print("Opção inválida. Tente novamente.")

converter()