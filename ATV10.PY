# Flag inicial
alguem_reprovou = False

# Loop para 5 alunos
for i in range(5):
    while True:
        try:
            nota = float(input(f"Digite a nota do aluno {i+1} (0 a 10): "))
            if 0 <= nota <= 10:
                break
            else:
                print("Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite um número.")

    # Verifica se a nota reprova
    if nota < 5.0:
        alguem_reprovou = True

# Verifica o flag depois do loop
print("\nResultado final:")
if alguem_reprovou:
    print("A turma possui pelo menos um aluno reprovado.")
else:
    print("Parabéns! Todos na turma foram aprovados.")
