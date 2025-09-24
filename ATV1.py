#Crie um programa que simule uma votação. Os códigos de voto válidos são:
#● 10 - Candidato A
#● 20 - Candidato B
#● 30 - Candidato C
#● 98 - Voto Nulo
#● 99 - Voto em Branco
#O programa deve solicitar um voto e continuar pedindo até que o usuário digite um dos códigos válidos. 
# Ao final, deve exibir o voto registrado.

candidatos = {
    10: "candidato A",
    20: "candidato B",
    30: "candidato C",
    98: "voto Nulo",
    99: "voto em branco"
}   

while True:

    votos = int(input("Escolha um candidato: "))

    if votos in candidatos:
        print(f"Voto registrado: {candidatos[votos]}")
        break
    else:
        print("Código do candidato inválido. Tente novamente.")

print(f"Voto registrado com sucesso!")