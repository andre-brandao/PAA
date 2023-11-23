import random
import timeout_decorator
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd
import time
import pytest

from subset_sum import subset_sum_backtracking, subset_sum_bruteforce
from increasing_sequence import maior_subsequencia_divisao_conquista
# Define the maximum timeout value
timeoutMAX = 10

test_data = [
    ([1, 2, 3, 4, 5], 10),
    ([3, 7, 2, 8, 4], 15),
    (random.sample(range(1, 11), 10), 12),
    (random.sample(range(1, 51), 50), 70),
    (random.sample(range(1, 101), 100), 123),
    (random.sample(range(1, 201), 200), 234),
    (random.sample(range(1, 501), 500), 567),
    (random.sample(range(1, 1001), 1000), 123),
    (random.sample(range(1, 1001), 1000), 1234),
    (random.sample(range(1, 10001), 10000), 12345),
]

#Teste para tamanho de amostra (com K sendo 1/2 do valor maximo)
test_data_length_sample_low_sum = [
    (random.sample(range(1, 11), 10), 5),
    (random.sample(range(1, 51), 50), 25),
    (random.sample(range(1, 101), 100), 50),
    (random.sample(range(1, 201), 200), 100),
    (random.sample(range(1, 501), 500), 250),
    (random.sample(range(1, 1001), 1000), 500),
    (random.sample(range(1, 10001), 10000), 5000)
]
#Teste para tamanho de amostra (com K sendo 2x do valor maximo)
test_data_length_sample_high_sum = [
    (random.sample(range(1, 11), 10), 20),
    (random.sample(range(1, 51), 50), 100),
    (random.sample(range(1, 101), 100), 200),
    (random.sample(range(1, 201), 200), 400),
    (random.sample(range(1, 501), 500), 1000),
    (random.sample(range(1, 1001), 1000), 2000),
    (random.sample(range(1, 10001), 10000), 20000)
]

#Teste para valor de K com tamanho de amostra pequena
test_data_value_sum_low_length_sample = [
    (random.sample(range(1, 51), 50), 1),
    (random.sample(range(1, 51), 50), 10),
    (random.sample(range(1, 51), 50), 50),
    (random.sample(range(1, 51), 50), 100),
    (random.sample(range(1, 51), 50), 500),
    (random.sample(range(1, 51), 50), 1000),
    (random.sample(range(1, 51), 50), 1275)
]

#Teste para valor de K com tamanho de amostra grande
test_data_value_sum_high_length_sample = [
    (random.sample(range(1, 5001), 5000), 1),
    (random.sample(range(1, 5001), 5000), 10),
    (random.sample(range(1, 5001), 5000), 100),
    (random.sample(range(1, 5001), 5000), 1000),
    (random.sample(range(1, 5001), 5000), 100000),
    (random.sample(range(1, 5001), 5000), 10000000),
    (random.sample(range(1, 5001), 5000), 12502500)
]

#Teste para valor de K com tamanho de amostra médio
test_data_value_sum_medium_length_sample = [
    (random.sample(range(1, 1001), 1000), 1),
    (random.sample(range(1, 1001), 1000), 10),
    (random.sample(range(1, 1001), 1000), 100),
    (random.sample(range(1, 1001), 1000), 1000),
    (random.sample(range(1, 1001), 1000), 10000),
    (random.sample(range(1, 1001), 1000), 100000),
    (random.sample(range(1, 1001), 1000), 500500)
]



test_data_paa2 = [
    (range(1, 100)),
    (range(1, 1000)),
    (random.sample(range(1, 100), 100)),

]
def print_test_result(array, target_sum, result, elapsed_time, method):
    print(f'Test Data: array={array}, target_sum={target_sum}')
    if result is not None:
        print(f'{method} Result: {result}')
        print(f'{method} Execution Time: {elapsed_time:.8f} seconds')
    else:
        print(f'{method} Timed Out')


@timeout_decorator.timeout(timeoutMAX)
def run_bruteforce(array, target_sum):
    start_time_bruteforce = time.time()
    subset, expanded = subset_sum_bruteforce(array, target_sum)
    elapsed_time_bruteforce = time.time() - start_time_bruteforce
    return subset, expanded, elapsed_time_bruteforce


@timeout_decorator.timeout(timeoutMAX)
def run_backtracking(array, target_sum):
    start_time_backtracking = time.time()
    subset, expanded = subset_sum_backtracking(array, target_sum)
    elapsed_time_backtracking = time.time() - start_time_backtracking
    return subset, expanded, elapsed_time_backtracking

@timeout_decorator.timeout(timeoutMAX)
def run_divide_and_conquer(array):
    start_time_divide_and_conquer = time.time()
    result = maior_subsequencia_divisao_conquista(array)
    elapsed_time_divide_and_conquer = time.time() - start_time_divide_and_conquer
    return result, elapsed_time_divide_and_conquer


def plot_execution_times(x_labels, bruteforce_times, backtracking_times, bruteforce_expanded, backtracking_expanded):
    # Scale the data using Pandas for the y-axis
    df = pd.DataFrame({'Bruteforce': bruteforce_times, 'Backtracking': backtracking_times})

    # Plot the execution times
    fig, ax = plt.subplots(figsize=(10, 8))

    # Set the y-axis scale to logarithmic
    plt.yscale('log')

    plt.plot(x_labels, df['Bruteforce'], label='Bruteforce', marker='o')
    plt.plot(x_labels, df['Backtracking'], label='Backtracking', marker='o')
    plt.xlabel('Test Case')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time Comparison')
    plt.legend()
    plt.xticks(rotation=45)

    # Set Y-axis limits from 0 to timeoutMAX
    plt.ylim(0, timeoutMAX)

    # Format the y-axis labels for better precision
    def format_func(value, tick_number):
        return f"{value:.6f}"

    ax.yaxis.set_major_formatter(FuncFormatter(format_func))
    for i, (x, y_bruteforce, y_backtracking, exp_bruteforce, exp_backtracking) in enumerate(
            zip(x_labels, df['Bruteforce'], df['Backtracking'], bruteforce_expanded, backtracking_expanded)):
        plt.annotate(f'Time: {y_bruteforce:.6f}\nNodes: {exp_bruteforce}', (x, y_bruteforce), xytext=(5, 15),
                     textcoords='offset points', fontsize=8, fontweight='bold', color='blue',
                     bbox=dict(boxstyle='round,pad=0.5',
                               fc='green', alpha=0.5), arrowprops=dict(arrowstyle='->', color='blue'))
        plt.annotate(f'Time: {y_backtracking:.6f}\nNodes: {exp_backtracking}', (x, y_backtracking), xytext=(5, -25),
                     textcoords='offset points', fontsize=8, fontweight='bold', color='red',
                     bbox=dict(boxstyle='round,pad=0.5',
                               fc='yellow', alpha=0.5), arrowprops=dict(arrowstyle='->', color='red'))
    plt.tight_layout()
    plt.show()


def tests_and_plot():
    bruteforce_times = []
    backtracking_times = []
    bruteforce_expanded_nodes = []
    backtracking_expanded_nodes = []

    x_labels = []

    for array, target_sum in test_data_value_sum_medium_length_sample:
        result_bruteforce = None
        result_backtracking = None
        elapsed_time_backtracking = 0
        elapsed_time_bruteforce = 0
        expanded_backtracking = None
        expanded_bruteforce = None

        try:
            result_backtracking, expanded_backtracking, elapsed_time_backtracking = run_backtracking(array, target_sum)
        except timeout_decorator.TimeoutError:
            print(f'Backtracking Timed Out')
            pass
        except RecursionError:
            print(f'Backtracking Recursion Error')
            pass

        try:
            result_bruteforce, expanded_bruteforce, elapsed_time_bruteforce = run_bruteforce(array, target_sum)
        except timeout_decorator.TimeoutError:
            print(f'Bruteforce Timed Out')
            pass

        print('\n' + '=' * 30)
        print_test_result(array, target_sum, result_backtracking, elapsed_time_backtracking, 'Backtracking')
        print_test_result(array, target_sum, result_bruteforce, elapsed_time_bruteforce, 'Bruteforce')
        print(
            f'Difference (Bruteforce - Backtracking): {elapsed_time_bruteforce - elapsed_time_backtracking:.6f} seconds')

        bruteforce_expanded_nodes.append(expanded_bruteforce)
        backtracking_expanded_nodes.append(expanded_backtracking)
        bruteforce_times.append(elapsed_time_bruteforce)
        backtracking_times.append(elapsed_time_backtracking)
        x_labels.append(f"Array Size = {len(array)}\nSum = {target_sum}")

    plot_execution_times(x_labels, bruteforce_times, backtracking_times, bruteforce_expanded_nodes,
                         backtracking_expanded_nodes)


if __name__ == "__main__":
    tests_and_plot()
