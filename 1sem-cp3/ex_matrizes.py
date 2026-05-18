temperaturas = [
    [28, 31, 34, 33], # sala 1
    [25, 27, 29, 28], # sala 2
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

maior_critico = 0
sala_maior_critico = 0

for i, temps_sala in enumerate(temperaturas):
    soma = 0
    registros_criticos = 0

    for temperatura in temps_sala:
        soma += temperatura

        if temperatura >= 33:
            registros_criticos += 1

    if registros_criticos > maior_critico:
        maior_critico = registros_criticos
        sala_maior_critico = i + 1

    media = sum(temps_sala) / len(temps_sala)

    print(f"Sala {i+1}")
    print(f"Média: {media}")
    print(f"Registros críticos: {registros_criticos}")
    print()

print(f"Sala com maior risco: Sala {sala_maior_critico}")