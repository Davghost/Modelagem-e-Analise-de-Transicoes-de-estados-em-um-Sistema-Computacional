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

R = [
[0.2, 0.8, 0.0, 0.0], # T
[0.0, 0.2, 0.3, 0.5], # CPU
[0.9, 0.0, 0.1, 0.0], # D1
[0.7, 0.0, 0.0, 0.3] # D2
]

for i in R:
    print(i)


# Etapa preparatória: identifica as consultas que podem concluir atendimento
# no próximo time slot. Ainda não calcula seus destinos nem probabilidades.
def consultas_atendidas(estado):
    capacidades = [sum(estado), 1, 1, 1]
    atendidas = []

    for indice in range(len(estado)):
        if estado[indice] < capacidades[indice]:
            atendidas.append(estado[indice])
        else:
            atendidas.append(capacidades[indice])

    return atendidas


def consultas_que_ficam_na_fila(estado):
    atendidas = consultas_atendidas(estado)
    fila = []

    for indice in range(len(estado)):
        fila.append(estado[indice] - atendidas[indice])

    return fila


def validar_matriz_roteamento(matriz):
    """Verifica se R é quadrada, não negativa e se cada linha soma 1."""
    quantidade_estacoes = len(matriz)

    if quantidade_estacoes == 0:
        return False

    for linha in matriz:
        if len(linha) != quantidade_estacoes:
            return False

        soma = 0
        for probabilidade in linha:
            if probabilidade < 0:
                return False
            soma += probabilidade

        if abs(soma - 1.0) > 0.0000001:
            return False

    return True


def destinos_possiveis(estacao, matriz_roteamento):
    """Lista os destinos com probabilidade maior que zero para uma estação."""
    destinos = []

    for destino in range(len(matriz_roteamento[estacao])):
        if matriz_roteamento[estacao][destino] > 0:
            destinos.append(destino)

    return destinos


def indice_do_estado(estado_procurado, estados):
    """Retorna a coluna/linha de um estado na lista de estados, ou -1."""
    for indice in range(len(estados)):
        if estados[indice] == estado_procurado:
            return indice
    return -1


def criar_matriz_vazia(tamanho):
    """Cria uma matriz quadrada de zeros, futura matriz de transição P."""
    matriz = []

    for linha in range(tamanho):
        matriz.append([])
        for coluna in range(tamanho):
            matriz[linha].append(0.0)

    return matriz


# Exemplos para apoiar a próxima etapa do algoritmo:
# consultas_atendidas([2, 3, 1, 0]) -> [2, 1, 1, 0]
# consultas_que_ficam_na_fila([2, 3, 1, 0]) -> [0, 2, 0, 0]