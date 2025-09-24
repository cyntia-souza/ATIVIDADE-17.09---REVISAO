# Faça um programa "Controle de Despesas". O programa deve pedir o valor de uma despesa(use float).
# O usuário pode digitar despesas indefinidamente. Quando ele digitar 0, o programa para. No final, ele deve mostrar:
#1. O total gasto.
#2. O número de despesas registradas.
#3. O valor médio por despesa (Total / Número).

total = 0
n_despesas = 0
valor_medio = 0

while True:
   
    valor = float(input("Digite um valor: "))

    if valor == 0:
        print("sistema encerrado!")
        break
    else:
        if valor != 0:
            n_despesas = n_despesas + 1

    total = valor * n_despesas

print(f"o tota gasto foi: {total}")
print(f"o numero de despesas foi: {n_despesas}")
print(f"o valor medio por despesas foi: {total / n_despesas}")


