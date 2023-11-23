import random
import timeout_decorator
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd
import time
import pytest

from increasing_sequence import maior_subsequencia_array_walk, maior_subsequencia_crescente_contigua_forca_bruta, \
    maior_subsequencia_crescente_gulosa, maior_subsequencia_crescente_contigua_divide_conquer

# Define the maximum timeout value
timeoutMAX = 10

test_data_paa2 = [
    (range(1, 100)),
    (range(1, 1000)),
    (range(1, 1000000)),
    (range(1, 1000000000)),
    (random.sample(range(1, 101), 100)),
    (random.sample(range(1, 1000001), 1000000)),
    (random.sample(range(1, 101), 100) + list(range(1, 100))),
    (random.sample(range(1, 1000001), 1000000) + list(range(1, 1000001))),
    (random.sample(range(1, 101), 100) + list(range(1, 100)) + list(range(1, 100)) + random.sample(range(1, 101), 100)),
    (random.sample(range(1, 1000001), 1000000) + list(range(1, 1000001)) + list(range(1, 1000001)) + random.sample(
        range(1, 1000001), 1000000)),

]

test_data_random = [
    (random.sample(range(1, 101), 100)),
    (random.sample(range(1, 1001), 1000)),
    (random.sample(range(1, 5001), 5000)),
    (random.sample(range(1, 10001), 10000)),
    (random.sample(range(1, 50001), 50000)),
    (random.sample(range(1, 100001), 100000)),
    (random.sample(range(1, 1000001), 1000000)),

]

test_data_range = [
    (range(1, 101)),
    (range(1, 1001)),
    (range(1, 5001)),
    (range(1, 10001)),
    (range(1, 50001)),
    (range(1, 1000001)),

    (range(1, 1000000001)),

]

test_data_random_list_midle = [
    (random.sample(range(1, 101), 100) + list(range(1, 100)) + random.sample(range(1, 101), 100)),
    (random.sample(range(1, 1001), 1000) + list(range(1, 1001)) + random.sample(range(1, 1001), 1000)),
    (random.sample(range(1, 5001), 5000) + list(range(1, 5001)) + random.sample(range(1, 5001), 5000)),
    (random.sample(range(1, 10001), 10000) + list(range(1, 10001)) + random.sample(range(1, 10001), 10000)),
    (random.sample(range(1, 50001), 50000) + list(range(1, 50001)) + random.sample(range(1, 50001), 50000)),
    (random.sample(range(1, 1000001), 1000000) + list(range(1, 1000001)) + random.sample(range(1, 1000001), 1000000)),
]

test_data_random_list_start = [
    (list(range(1, 100)) + random.sample(range(1, 101), 100)),
    (list(range(1, 1000)) + random.sample(range(1, 1001), 1000)),
    (list(range(1, 5000)) + random.sample(range(1, 10001), 5000)),
    (list(range(1, 10001)) + random.sample(range(1, 10001), 10000)),
    (list(range(1, 50001)) + random.sample(range(1, 50001), 50000)),
    (list(range(1, 1000001)) + random.sample(range(1, 1000001), 1000000)),

]

test_data_random_list_end = [
    (random.sample(range(1, 101), 100) + list(range(1, 100))),
    (random.sample(range(1, 1001), 1000) + list(range(1, 1001))),
    (random.sample(range(1, 5001), 5000) + list(range(1, 5001))),
    (random.sample(range(1, 10001), 10000) + list(range(1, 10001))),
    (random.sample(range(1, 50001), 50000) + list(range(1, 50001))),
    (random.sample(range(1, 1000001), 1000000) + list(range(1, 1000001))),
]

all = [
    test_data_random,
    test_data_range,
    test_data_random_list_start,
    test_data_random_list_midle,

    test_data_random_list_end,

]

@timeout_decorator.timeout(timeoutMAX)
def run_divide_and_conquer(array):
    start_time_divide_and_conquer = time.time()
    result = maior_subsequencia_crescente_contigua_divide_conquer(array)
    elapsed_time_divide_and_conquer = time.time() - start_time_divide_and_conquer
    return result, elapsed_time_divide_and_conquer


@timeout_decorator.timeout(timeoutMAX)
def run_greedy(array):
    start_time_greedy = time.time()
    result = maior_subsequencia_crescente_gulosa(array)
    elapsed_time_greedy = time.time() - start_time_greedy
    return result, elapsed_time_greedy


@timeout_decorator.timeout(timeoutMAX)
def run_bruteforce(array):
    start_time_bruteforce = time.time()
    result = maior_subsequencia_crescente_contigua_forca_bruta(array)
    elapsed_time_bruteforce = time.time() - start_time_bruteforce
    return result, elapsed_time_bruteforce


@timeout_decorator.timeout(timeoutMAX)
def run_array_walk(array):
    start_time_array_walk = time.time()
    result = maior_subsequencia_array_walk(array)
    elapsed_time_array_walk = time.time() - start_time_array_walk
    return result, elapsed_time_array_walk


def plot_execution_times(x_labels, divide_and_conquer_times, greedy_times, bruteforce_times, array_walk_times):
    # Scale the data using Pandas for the y-axis
    df = pd.DataFrame(
        {'Divide and Conquer': divide_and_conquer_times, 'Greedy': greedy_times, 'Bruteforce': bruteforce_times,
         'Array Walk': array_walk_times})

    # Plot the execution times
    fig, ax = plt.subplots(figsize=(10, 8))

    # Set the y-axis scale to logarithmic
    plt.yscale('log')

    plt.plot(x_labels, df['Divide and Conquer'], label='Divide and Conquer', marker='o')
    plt.plot(x_labels, df['Greedy'], label='Greedy', marker='o')
    plt.plot(x_labels, df['Bruteforce'], label='Bruteforce', marker='o')
    plt.plot(x_labels, df['Array Walk'], label='Array Walk', marker='o')

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
    for i, (x, y_divide_and_conquer, y_greedy, y_bruteforce, y_array_walk) in enumerate(
            zip(x_labels, df['Divide and Conquer'], df['Greedy'], df['Bruteforce'], df['Array Walk'])):
        # Annotate for Divide and Conquer
        plt.annotate(f'DC: {y_divide_and_conquer:.6f}', (x, y_divide_and_conquer),
                     xytext=(5, -25), textcoords='offset points', fontsize=8, fontweight='bold', color='blue',
                     bbox=dict(boxstyle='round,pad=0.5', fc='green', alpha=0.5),
                     arrowprops=dict(arrowstyle='->', color='blue'))

        # Annotate for Greedy
        plt.annotate(f'Greedy: {y_greedy:.6f}', (x, y_greedy),
                     xytext=(5, -10), textcoords='offset points', fontsize=8, fontweight='bold', color='orange',
                     bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
                     arrowprops=dict(arrowstyle='->', color='orange'))

        # Annotate for Bruteforce
        plt.annotate(f'Bruteforce: {y_bruteforce:.6f}', (x, y_bruteforce),
                     xytext=(0, 15), textcoords='offset points', fontsize=8, fontweight='bold', color='green',
                     bbox=dict(boxstyle='round,pad=0.5', fc='pink', alpha=0.5),
                     arrowprops=dict(arrowstyle='->', color='red'))

        # Annotate for Array Walk
        plt.annotate(f'Array Walk: {y_array_walk:.6f}', (x, y_array_walk),
                     xytext=(0, 30), textcoords='offset points', fontsize=8, fontweight='bold', color='red',
                     bbox=dict(boxstyle='round,pad=0.5', fc='pink', alpha=0.5),
                     arrowprops=dict(arrowstyle='->', color='red'))

    plt.tight_layout()
    plt.show()


@pytest.mark.parametrize("test_input", all)
def tests_and_plot(test_input):
    divide_and_conquer_times = []
    greedy_times = []
    bruteforce_times = []
    array_walk_times = []

    x_labels = []

    for array in test_input:
        result_divide_and_conquer = None
        elapsed_time_divide_and_conquer = 0
        result_greedy = None
        elapsed_time_greedy = 0
        result_bruteforce = None
        elapsed_time_bruteforce = 0
        result_array_walk = None
        elapsed_time_array_walk = 0

        try:
            result_divide_and_conquer, elapsed_time_divide_and_conquer = run_divide_and_conquer(array)

        except timeout_decorator.TimeoutError:
            print(f'Divide and Conquer Timed Out')
            pass

        try:
            result_greedy, elapsed_time_greedy = run_greedy(array)
        except timeout_decorator.TimeoutError:
            print(f'Greedy Timed Out')
            pass

        try:
            result_bruteforce, elapsed_time_bruteforce = run_bruteforce(array)
        except timeout_decorator.TimeoutError:
            print(f'Bruteforce Timed Out')
            pass

        try:
            result_array_walk, elapsed_time_array_walk = run_array_walk(array)
        except timeout_decorator.TimeoutError:
            print(f'Array Walk Timed Out')
            pass

        print('\n' + '=' * 30)
        print_test_result(array, result_divide_and_conquer, elapsed_time_divide_and_conquer,
                          'Divide and Conquer')

        divide_and_conquer_times.append(elapsed_time_divide_and_conquer)
        greedy_times.append(elapsed_time_greedy)
        bruteforce_times.append(elapsed_time_bruteforce)
        array_walk_times.append(elapsed_time_array_walk)

        x_labels.append(f"Array Size = {len(array)}\n")

    plot_execution_times(x_labels, divide_and_conquer_times, greedy_times, bruteforce_times,array_walk_times)


def print_test_result(array, result, elapsed_time, method):
    print(f'Test Data: array={array}')
    if result is not None:
        print(f'{method} Result: {result}')
        print(f'{method} Execution Time: {elapsed_time:.8f} seconds')
    else:
        print(f'{method} Timed Out')


if __name__ == "__main__":
    tests_and_plot()
