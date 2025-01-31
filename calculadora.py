def calculadora(operacao):
    def somar(a, b):
        return a + b

    def subtrair(a, b):
        return a - b

    def multiplicar(a, b):
        return a * b

    def dividir(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Erro: Divisão por zero não é permitida."

    match operacao:
        case "+":
            return somar
        case "-":
            return subtrair
        case "*":
            return multiplicar
        case "/":
            return dividir
        case _:
            return None  # Adicionar um caso padrão para operações inválidas


def conversao(numeros):
    numero = input(numeros)
    if isinstance(numero, float):
        numero = round(numero, 2)  
    # Substituir vírgula por ponto antes da conversão
    numero = numero.replace(",", ".")
    try:
        numero = int(numero)
    except ValueError:
        numero = float(numero)
      # Arredondar para 2 casas decimais se for float
    return numero



operacao = input("Digite a operação: +, -, *, /: ")
numero1 = conversao("Digite o primeiro número: ")
numero2 = conversao("Digite o segundo número: ")

funcao = calculadora(operacao)

if funcao:
    numeros = funcao(numero1, numero2)
    print(f"O resultado da operação é: {numeros}")
else:
    print(f"Operação {operacao} inválida. Tente novamente.")