menu = """
========BancoPY========
*Selecione o serviço

[d]Depósito
[s]Saque
[e]Extrato
[q]Sair

=======================

==>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":

        deposito = int(input("Digite o valor desejado:"))
    
        if deposito > 0:
            saldo += deposito
            print(f"Depósito: R${saldo:.2f}")
            extrato += f"Depósito: R${saldo:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "s":

        saque = float(input("Digite seu valor:"))

        if saldo > 0:
            if saque <= limite:
                numero_saques += 1

                if numero_saques <= LIMITE_SAQUES:
                    saldo -= saque
                    extrato += f"Saque: R${saque:.2f}\n"
                
                    print(f"numero de saques {numero_saques}")
                    print(f"Valor sacado {saque}")
                    
                else:
                    print("Você atingiu seu limite diário para saques!")
            else:
                print(f"Seu limite por saque é de R${limite}!")
        else:
            print("Você não possui saldo em conta!")
    
    elif opcao == "e":
       print("\n===============EXTRATO================")
       print("Não foram realizadas movimentações." if not extrato else extrato)
       print(f"\nSaldo: R${saldo:.2f}")
       print("========================================")     

    elif opcao == "q":
        print("Obrigado por utilizar nossos serviços!")
        break

    else:
        print("Operação inválida, por favor selcione novamente a operação desejada.")