#Crie um menu interativo que simula a frente de um caixa de banco. O programa deve exibir as seguintes opções:
#1. Ver Saldo
#2. Fazer Depósito
#3. Fazer Saque
#4. Sair
#O programa deve pedir a escolha do usuário e, por enquanto, apenas exibir uma mensagem confirmando a opção escolhida
#  (ex: "Você escolheu 'Fazer Depósito'."). Se o usuário digitar "0",o programa deve encerrar. Se digitar uma opção
#  inválida, deve avisar e mostrar o menu novamente.

servicos = {
    1: 'Ver Saldo',
    2: 'Fazer Depósito',
    3: 'Fazer Saque',
    4: 'Sair'
}

print("Bem-vindo ao Banco C! ")

while True:

    opcao = int(input("Escolha uma opção: "))

    if opcao == 0:
        print("Sistema encerrado. Até mais!")
        break
    elif opcao in servicos:
        print(f"Voce escolheu: {servicos[opcao]}") 
        break
    else:
        print("opção inválida! Digite a opção correta")
        