import sys

# Definir as variáveis iniciais
saldo = 0
depositos = []
saques = []

# Função para fazer um depósito
def deposito(valor):
    global saldo
    global depositos

    # Validar o valor
    if valor < 0:
        print("O valor do depósito deve ser positivo.")
        sys.exit(1)

    # Adicionar o depósito ao saldo
    saldo += valor

    # Adicionar o depósito à lista de depósitos
    depositos.append(valor)

# Função para fazer um saque
def saque(valor):
    global saldo
    global saques

    # Validar o valor
    if valor < 0:
        print("O valor do saque deve ser positivo.")
        sys.exit(1)

    # Validar o saldo
    if saldo < valor:
        print("O saldo não é suficiente para o saque.")
        sys.exit(1)

    # Subtrair o saque do saldo
    saldo -= valor

    # Adicionar o saque à lista de saques
    saques.append(valor)

# Função para exibir o extrato
def extrato():
    global saldo
    global depositos
    global saques

    # Imprimir o cabeçalho do extrato
    print("Extrato bancário")
    print("Saldo atual: R$", saldo, sep="")

    # Imprimir os depósitos
    print("Depósitos:")
    for deposito in depositos:
        print("R$", deposito, sep="")

    # Imprimir os saques
    print("Saques:")
    for saque in saques:
        print("R$", saque, sep="")

# Menu principal
print("Bem-vindo ao sistema bancário!")

while True:
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        valor = float(input("Digite o valor do depósito: "))
        deposito(valor)
    elif escolha == "2":
        valor = float(input("Digite o valor do saque: "))
        saque(valor)
    elif escolha == "3":
        extrato()
    elif escolha == "4":
        break
    else:
        print("Opção inválida.")
