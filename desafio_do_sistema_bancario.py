menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
limite_saque = 3
extrato = ""
numero_saque = 0


while True :

    opcao = input(menu)
    
    if opcao == "d":
        print("Depósito")
        valor_deposito = float(input("Digite uma valor para o depósito: R$"))
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        if valor_deposito <= 0:
          print("Valor invalido! Digite novamente.")
        saldo += valor_deposito
        

    elif opcao == "s":
        print("Saque")
        valor_saque = float(input("Digite uma valor para saque: R$"))
        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numero_saque >= limite_saque

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Depósito: R$ {valor_saque:.2f}\n"
            numero_saque += 1
        
        else:
            print("Operação falhou!O valor informado é inválido")





    
    elif opcao == "e":
        print("\n===================Extrato===================")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================================")

    elif opcao == "q":
       break

    else:
        print("comando inválido, selecione novamente!")

