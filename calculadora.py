def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é permitida"

def calculadora():
    while True:
        print("\nEscolha a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("0. Sair")

        escolha = input("Digite sua escolha (0/1/2/3/4): ")

        if escolha == '0':
            print("Saindo da calculadora. Até logo!")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"Resultado: {soma(num1, num2)}")
        elif escolha == '2':
            print(f"Resultado: {subtracao(num1, num2)}")
        elif escolha == '3':
            print(f"Resultado: {multiplicacao(num1, num2)}")
        elif escolha == '4':
            print(f"Resultado: {divisao(num1, num2)}")
        else:
            print("Escolha inválida, tente novamente.")

calculadora(
