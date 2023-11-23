def maior_subsequencia_divisao_conquista(arr):
    maxLength = 1
    maxStart = 0
    curStart = 0
    curLength = 1
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            if curLength > maxLength:
                maxLength = curLength
                maxStart = curStart
            curStart = i
            curLength = 1
        else:
            curLength += 1
    if curLength > maxLength:
        maxLength = curLength
        maxStart = curStart
    return (maxLength, maxStart)



def maior_subsequencia_crescente_contigua_forca_bruta(array):
    n = len(array)
    max_len = 0  # Armazenará o comprimento máximo da subsequência crescente contígua
    resultado = []  # Armazenará a subsequência crescente contígua atualmente encontrada

    for i in range(n):
        subsequencia_atual = [array[i]]  # Inicia uma nova subsequência contígua com o elemento atual

        for j in range(i + 1, n):
            if array[j] > subsequencia_atual[-1]:
                subsequencia_atual.append(array[j])
            else:
                break  # Se não for crescente, interrompe a subsequência contígua

        # Atualiza a subsequência máxima encontrada, se aplicável
        if len(subsequencia_atual) > max_len:
            max_len = len(subsequencia_atual)
            resultado = subsequencia_atual[:]

    return resultado


def maior_subsequencia_crescente_gulosa(array):
    if not array:
        return []

    # Inicializa a subsequência atual com o primeiro elemento do array
    subsequencia_atual = [array[0]]

    # Inicializa a maior subsequência encontrada com o mesmo elemento
    maior_subsequencia = [array[0]]

    # Percorre o restante do array
    for i in range(1, len(array)):
        # Se o próximo elemento for maior que o último elemento na subsequência atual,
        # estenda a subsequência
        if array[i] > subsequencia_atual[-1]:
            subsequencia_atual.append(array[i])
        else:
            # Se não, inicie uma nova subsequência com o elemento atual
            subsequencia_atual = [array[i]]

        # Atualiza a maior subsequência se a subsequência atual for maior
        if len(subsequencia_atual) > len(maior_subsequencia):
            maior_subsequencia = subsequencia_atual

    return maior_subsequencia