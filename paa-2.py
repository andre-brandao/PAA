import random
import timeout_decorator
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd
import time
import pytest


from increasing_sequence import maxIncreasing
# Define the maximum timeout value
timeoutMAX = 10



test_data_paa2 = [
    (range(1, 100)),
    (range(1, 1000)),
    (range(1, 1000000)),
    (range(1, 1000000000)),
    (random.sample(range(1, 101), 100)),
    (random.sample(range(1, 1000001), 1000000)),

]

@timeout_decorator.timeout(timeoutMAX)
def run_divide_and_conquer(array):
    start_time_divide_and_conquer = time.time()
    # Replace this line with your actual divide and conquer algorithm
    result = maxIncreasing(array)
    elapsed_time_divide_and_conquer = time.time() - start_time_divide_and_conquer
    return result, elapsed_time_divide_and_conquer

def plot_execution_times(x_labels, divide_and_conquer_times):
    # Scale the data using Pandas for the y-axis
    df = pd.DataFrame({'Divide and Conquer': divide_and_conquer_times})

    # Plot the execution times
    fig, ax = plt.subplots(figsize=(10, 8))

    # Set the y-axis scale to logarithmic
    plt.yscale('log')

    plt.plot(x_labels, df['Divide and Conquer'], label='Divide and Conquer', marker='o')
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
    for i, (x, y_divide_and_conquer) in enumerate(
            zip(x_labels, df['Divide and Conquer'])):
        plt.annotate(f'Time: {y_divide_and_conquer:.6f}', (x, y_divide_and_conquer),
                     xytext=(5, 15), textcoords='offset points', fontsize=8, fontweight='bold', color='blue',
                     bbox=dict(boxstyle='round,pad=0.5', fc='green', alpha=0.5),
                     arrowprops=dict(arrowstyle='->', color='blue'))

    plt.tight_layout()
    plt.show()

def tests_and_plot():
    divide_and_conquer_times = []

    x_labels = []

    for array in test_data_paa2:
        result_divide_and_conquer = None
        elapsed_time_divide_and_conquer = 0
        expanded_divide_and_conquer = None

        try:
            result_divide_and_conquer, elapsed_time_divide_and_conquer = run_divide_and_conquer(array)

        except timeout_decorator.TimeoutError:
            print(f'Divide and Conquer Timed Out')
            pass

        print('\n' + '=' * 30)
        print_test_result(array, result_divide_and_conquer, elapsed_time_divide_and_conquer,
                          'Divide and Conquer')

        divide_and_conquer_times.append(elapsed_time_divide_and_conquer)
        x_labels.append(f"Array Size = {len(array)}\n")

    plot_execution_times(x_labels, divide_and_conquer_times)


def print_test_result(array, result, elapsed_time, method):
    print(f'Test Data: array={array}')
    if result is not None:
        print(f'{method} Result: {result}')
        print(f'{method} Execution Time: {elapsed_time:.8f} seconds')
    else:
        print(f'{method} Timed Out')

if __name__ == "__main__":
    tests_and_plot()
