def gerar_estados(N):
    estados = []
    for t in range(N, -1, -1):
        for cpu in range(N - t, -1, -1):
            for d1 in range(N - t - cpu, -1, -1):
                d2 = N - t - cpu - d1
                estado = [t, cpu, d1, d2]
                estados.append(estado)
    return estados

N = int(input("Digite n:"))
estados = gerar_estados(N)
for estado in estados:
    print(estado)
print("Total de estados:", len(estados))