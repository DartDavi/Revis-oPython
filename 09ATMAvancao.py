# 9. Caixa Eletrônico (ATM) Avançado Desenvolva um simulador de caixa eletrônico. O 
# programa deve exibir um menu contínuo com as opções: 1 - Depositar, 2 - Sacar, 3 - Consultar 
# Saldo, 4 - Sair. 
# ●  O saldo inicial é zero. 
# ●  Crie uma função para lidar com o saque, que receba o saldo atual e o valor desejado. 
# A função deve verificar se há saldo suficiente. Se não houver, deve exibir uma 
# mensagem de erro. 
# ●  Desafio extra no saque: Se o saque for aprovado, o programa deve utilizar uma 
# lógica de repetição e decisões (ou restos de divisão) para calcular e exibir a 
# quantidade de notas de R  20 e R$ 10 necessárias para entregar o valor, 50,𝑅
# priorizando sempre as notas maiores. (Considere que o caixa só aceita saques 
# múltiplos de 10). 
def sacar(saldo, valor):
    if valor <= 0:
        print("Valor inválido! O saque deve ser maior que zero.")
        return saldo

    if valor % 10 != 0:
        print("Valor inválido! O caixa só aceita saques múltiplos de 10.")
        return saldo

    if valor > saldo:
        print("Saldo insuficiente!")
        return saldo

    resto = valor

    notas_50 = resto // 50
    resto = resto % 50

    notas_20 = resto // 20
    resto = resto % 20

    notas_10 = resto // 10

    print(f"Saque de R$ {valor:.2f} realizado. Notas entregues:")
    if notas_50 > 0:
        print(f"  {notas_50} nota(s) de R$ 50")
    if notas_20 > 0:
        print(f"  {notas_20} nota(s) de R$ 20")
    if notas_10 > 0:
        print(f"  {notas_10} nota(s) de R$ 10")

    return saldo - valor


saldo = 0
opcao = 0

while opcao != 4:
    print("\n===== CAIXA ELETRÔNICO =====")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar Saldo")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        deposito = float(input("Valor do depósito: R$ "))
        if deposito > 0:
            saldo += deposito
            print(f"Depósito realizado. Saldo atual: R$ {saldo:.2f}")
        else:
            print("Valor inválido! O depósito deve ser maior que zero.")

    elif opcao == 2:
        valor = int(input("Valor do saque: R$ "))
        saldo = sacar(saldo, valor)

    elif opcao == 3:
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == 4:
        print("Obrigado por usar o caixa eletrônico. Até logo!")

    else:
        print("Opção inválida! Escolha de 1 a 4.")