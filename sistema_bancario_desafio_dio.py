menu = '''
Bem-Vindo ao Banco Pacífico
---------------------------
           *-*-*
-------[d]Depositar--------
-------[s]Sacar------------
-------[e]Extrato----------
-------[q]Sair-------------
           *-*-*
         Versão 1
'''

saldo = 0
limite = 500
extrato = ""
num_saque = 0
LIM_SAQUE = 3


while True:

    opcao = input(menu)


    if opcao == "d":
        valor = float(input("Informe ovalor a depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: AOA {valor:.2f}\n"

        else:
            print("Operação falhada! O valor informado é inválido.")


    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = num_saque >= LIM_SAQUE

        if excedeu_saldo:
            print("Operação falhada! O seu saldo não é suficiente.")

        elif excedeu_limite:
            print("Operação falhou! Excedeu o seu limite de levantamento.")

        elif excedeu_saque:
            print("Operação falhada! Excedeu o seu limite de saque")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: AOA {valor:.2f}\n"
            num_saque += 1

        else:
            print("operação falhou! O valor inserido é invalido")


    elif opcao == "e":
        print("\n *************** Extrato **************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: AOA {saldo:.2f}")
        print("*****************************************")


    elif opcao == "q":
        break

    else:
        print("Operação inválida! Por favor selecione a operação desejada-")