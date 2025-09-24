#Simule um interruptor de luz.
#1. Comece com uma variável luz_acesa = False.
#2. Crie um loop while que pergunta ao usuário "O que fazer? (1: apertar interruptor, 0: sair)".
#3. Se o usuário digitar "1", você deve inverter o estado da variável (se False, vira True; se True, vira False).
#4. Após cada ação, mostre o estado atual: "A luz está ACESA." ou "A luz está APAGADA."
#5. Se o usuário digitar "0", o programa sai.


luz_acesa = False

O_que_fazer = {
    1: "apertar interruptor", 
    0: "sair"
}

while True:

    acao = int(input("ligar ou desligar luz: "))

    if acao == 0:
        print("sair")
        break
       
    elif acao == 1:
        luz_acesa = not luz_acesa
        if luz_acesa:
            print(f"A luz esta acesa")
        else:
            print(f"A luz esta apagada")
    else:
     print("Opção inválida. Digite 1 para apertar o interruptor ou 0 para sair.")