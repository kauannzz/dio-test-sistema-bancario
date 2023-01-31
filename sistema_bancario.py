#TODOS DEPOSITOS DEVEM SER ARMAZENADOS EM UMA VARIAVEL E EXIBIDO NUMA OPERAÇÃO DE EXTRATO
#DEVE PERMITIR 3 SAQUES DIARIOS COM LIMITE MAX DE 500$ EM SAQUE

#TODOS OS DADOS DEVEM SER ARMAZENADOS EM UMA VARIAVEL E EXIBIDO NUMA OPERAÇÃO DE EXTRATO

#OPERAÇÃO DE EXTRATO DEVE LISTAR TODOS DEPOSITOS E SAQUES REALIZADOS NA CONTA E NO FIM DEVE EXIBIR O SALDO ATUAL DA CONTA

SAQUES_DIARIOS = 3
LIMITE_SAQUE_DIARIO = 500
SAQUES_REALIZADOS = 0
VALOR_EM_CONTA = 0


while True:
    WELCOME = input('[1] Depositar\n[2] Sacar\n[3] Extrato\n')

    if WELCOME == '1':
        valor_deposito = int(input('Qual o valor do seu depósito: '))
        if valor_deposito < 0:
            print('O valor deve ser positivo!')    
        else:
            VALOR_EM_CONTA = VALOR_EM_CONTA + valor_deposito
            print('Valor depositado com sucesso!')
            
    elif WELCOME == '2':
        valor_saque = int(input('Qual o valor do seu saque: '))
        if SAQUES_DIARIOS <= SAQUES_REALIZADOS:
            print('Você excedeu o limite de saques diarios!')
        elif VALOR_EM_CONTA < VALOR_EM_CONTA:
            print('Você não tem dinheiro para sacar!')
        elif valor_saque > LIMITE_SAQUE_DIARIO:
            print('Você excedeu o limite do valor de saque por dia!')
        else:
            SAQUES_REALIZADOS = SAQUES_REALIZADOS + 1 #Adiciona um saque a conta
            LIMITE_SAQUE_DIARIO = LIMITE_SAQUE_DIARIO - valor_saque #Diminui o valor do saque diario
            VALOR_EM_CONTA = VALOR_EM_CONTA - valor_saque #Diminui o valor da conta de acordo com o valor do saque
            print('Você sacou o valor com sucesso!')
    elif WELCOME == '3':
        print(f"""
        Valor da conta: R${VALOR_EM_CONTA}
        Total de saques realizadas: {SAQUES_REALIZADOS}
        """)
        break
    else:
        print('Operação inválida!')
        break