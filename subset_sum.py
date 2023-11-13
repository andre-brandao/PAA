from typing import List, Union, Tuple


def subset_sum_bruteforce(array: List[int], target_sum: int) -> Tuple[List[int], int] | None:
    n = len(array)
    expanded = 0
    for i in range(1, 2 ** n):
        subset = []
        subset_sum = 0

        for j in range(n):
            expanded += 1
            if (i >> j) & 1:
                subset.append(array[j])
                subset_sum += array[j]

        if subset_sum == target_sum:
            print(f'Bruteforce Expanded {expanded} nodes')
            return subset, expanded
    print(f'Bruteforce Expanded {expanded} nodes')
    return None


def subset_sum_backtracking(array: List[int], target_sum: int) -> Tuple[List[int], int] | None:
    expanded = 0  # Counter to keep track of expanded nodes

    def backtrack(start, current_subset, current_sum):

        # Verifica se achamos o resultado
        if current_sum == target_sum:
            return current_subset
        # Verifica se a soma atual é maior que K ou se já percorremos todo o vetor
        if current_sum > target_sum or start >= len(array):
            return None

        for i in range(start, len(array)):
            # Increment the expanded nodes counter
            nonlocal expanded
            expanded += 1

            # Atualiza o subconjunto e a soma atual
            new_subset = current_subset + [array[i]]
            new_sum = current_sum + array[i]

            result = backtrack(i + 1, new_subset, new_sum)
            # Se achou o resultado, retorna ele
            if result is not None:
                return result
        # Se não achou, retorna None
        return None

    result = backtrack(0, [], 0)
    print(f'Backtrack Expanded {expanded} nodes')
    return result, expanded
