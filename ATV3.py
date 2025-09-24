#Peça ao usuário um número inteiro positivo N. O programa deve calcular e exibir o fatorial de N (N!). 
# Exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120. O programa não deve aceitar números negativos edeve tratar o fatorial de 0 como 1.


numero = int(input("Digite um numero inteiro: "))

if numero < 0:
    print("Número negativo não é permitido. Tente novamente.")
else:
    fatorial = 1
    for N in range(1, numero + 1):
     fatorial = fatorial * N

print(f" O fatorial do {numero} é: {fatorial}")