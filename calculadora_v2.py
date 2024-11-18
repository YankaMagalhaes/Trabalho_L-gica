#variavel declarada
saida = ''
# Funções das operações 
def adicao (a, b):
    return a + b
def subtracao (a, b):
    return a - b
def multiplicacao (a, b):
    return a * b
def divisao (a, b):
    if divisao == 0:
        return ('Não foi possivel realizar a divisão por 0')
    else:
        a / b
#Função da calculadora, onde irá ocorrer o processo de verificação e operação matamatica após armazenagem do dado 
def calculadora (num1, num2, operacao ):
    
    if operacao == '+' or operacao == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao == 'subtracao':
        resultado = subtracao(num1, num2)
    elif operacao == '*' or operacao == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao == 'divisao':
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    return resultado

# Laço while para continuar ou parar, lower utilizado para converter o caracter 
while saida.lower() != 'n':
    # Solicita os números e a operação ao usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, / ou o nome da operação): ")

    # Chama a função calculadora e armazena o resultado
    resultado = calculadora(num1, num2, operacao)

    # Exibe o resultado
    print(f"Resultado da operação: {resultado}")

    # saida informa ao usuário se deseja continuar
    saida = input("Deseja continuar? (S/N): ")