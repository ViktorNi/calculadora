print("||||| SISTEMA DE CALCULADORA SIMPLES ||||")

print("ESCOLHA UMA DAS OPÇÕES ABAIXO:")
print("1 - SOMA")
print("2 - SUBTRAÇÃO")
print("3 - MULTIPLICAÇÃO")
print("4 - DIVISÃO")

opcao = int(input("Digite aqui o número correspondente a escolha da sua operação 1/2/3/4: "))
num1 = int(input("Digite aqui o primeiro da sua operação: "))
num2 = int(input("Digite aqui o segundo número da sua operação: "))

if opcao == 1:
    soma = num1 + num2 
    print('O resultado da soma é:', soma)

elif opcao == 2:
    subtracao = num1 - num2
    print("O resultado da subtração é", subtracao)
    
elif opcao == 3:
    multiplicacao = num1 * num2
    print("O resultado da multiplicação é:", multiplicacao)
    
elif opcao == 4:
    if num2 == 0:
        print("Erro: não é possível dividir por zero")
    
    else:
        divisao = num1 / num2
        print("O resultado da divisão é", divisao)

else:
    print("Operação inválida")