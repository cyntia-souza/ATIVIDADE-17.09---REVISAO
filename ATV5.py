#Peça ao usuário para digitar uma frase. O programa deve contar e exibir o número de vogais
#e o número de consoantes na frase. (Ignore espaços, números e pontuação).


vogais_lista = "aeiou"
vogais = 0
consoantes = 0

frase = input("Digite uma frase legal: ").lower()

for letra in frase:
    if letra.isalpha():  # Ignora espaços, números e pontuação
        if letra in vogais_lista:
            vogais = vogais + 1
        else:
            consoantes = consoantes + 1  # conta as consoantes

print(f"O número total de vogais na frase é: {vogais}")
print(f"O número total de consoantes na frase é: {consoantes}")
