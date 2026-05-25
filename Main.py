menu = """

{d} Depositar
{s} Sacar
{e} Extrato
{q} Sair

=> """

saldo = 0
limite= 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 2

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"

        else:
            print("A operação falhou! O valor informado é invalido.")

    elif opcao =="s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("A operação falhou! Você não tem saldo o suficiente.")

        elif excedeu_limite:
            print("A operação falhou! O valor do saque excede o limite disponivel.")

        elif excedeu_saques:
            print("A operação falhou! Numero máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numero_saques += 1

        else:
            print("A operação falhou! O valor indformado é invalido.")     
        
    elif opcao == "e":
        print("\n$$$$$$$$$$$$$$$$$$ EXTRATO $$$$$$$$$$$$$$$$$$")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("--------------------------------------------------")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        
