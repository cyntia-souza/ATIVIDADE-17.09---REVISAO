#Modifique o exercício "Média da Turma". Peça ao usuário quantos alunos existem. Emseguida, use um loop for para pedir
#a nota de cada aluno. Dentro desse loop, use um loopwhile para validar cada nota individualmente, garantindo que ela
# esteja entre 0 e 10. No final, exiba a média das notas válidas.
qtd_alunos = int(input("Quantos alunos existem na turma? "))

soma_notas = 0  # Acumula as notas

# Loop para cada aluno
for i in range(1, qtd_alunos + 1):
    nota = -1  # valor inicial inválido
    # Enquanto a nota não for válida, continua pedindo
    while nota < 0 or nota > 10:
        nota = float(input(f"Digite a nota do aluno {i} (0 a 10): "))
        if nota < 0 or nota > 10:
            print("⚠️ Nota inválida! Digite um valor entre 0 e 10.")
    soma_notas += nota  # soma a nota válida

# Calcula a média
media = soma_notas / qtd_alunos

# Exibe o resultado
print(f"\nA média da turma é: {media:.2f}")


