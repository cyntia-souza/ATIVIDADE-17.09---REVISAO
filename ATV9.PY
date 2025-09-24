criancas = 0
adolescentes = 0
adultos = 0
idosos = 0


for i in range(10):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))

    if 0 <= idade <= 12:
        criancas += 1
    elif 13 <= idade <= 17:
        adolescentes += 1
    elif 18 <= idade <= 59:
        adultos += 1
    elif idade >= 60:
        idosos += 1
    else:
        print("Idade inválida, ignorada.")


print("\nResultados finais:")
print(f"Crianças: {criancas}")
print(f"Adolescentes: {adolescentes}")
print(f"Adultos: {adultos}")
print(f"Idosos: {idosos}")