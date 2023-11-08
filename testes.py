import random
import timeout_decorator
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

from subset_sum import subset_sum_bruteforce, subset_sum_backtracking

import time
import pytest

# test_data = [
#     ([1, 2, 3, 4, 5], 10),
#     ([3, 7, 2, 8, 4], 15),
#
# ]
test_data = [
    ([1, 2, 3, 4, 5], 10),
    ([3, 7, 2, 8, 4], 15),

    (random.sample(range(1, 11), 10), 12),
    (random.sample(range(1, 51), 50), 70),
    (random.sample(range(1, 101), 100), 123),
    # (random.sample(range(1, 201), 200), 234),
    # (random.sample(range(1, 501), 500), 567),
    # (random.sample(range(1, 1001), 1000), 123),
    # (random.sample(range(1, 1001), 1000), 1234),
    # (random.sample(range(1, 10001), 10000), 12345)
]

# assert elapsed_time < 1.0  # Set a threshold for acceptable execution time
def print_test_result(S, K, result, elapsed_time, method):
    print(f'Test Data: S={S}, K={K}')
    if result is not None:
        print(f'{method} Result: {result}')
        print(f'{method} Execution Time: {elapsed_time:.8f} seconds')
    else:
        print(f'{method} Timed Out')


@timeout_decorator.timeout(10)
def run_bruteforce(S, K):
    return subset_sum_bruteforce(S, K)


@timeout_decorator.timeout(10)
def run_backtracking(S, K):
    return subset_sum_backtracking(S, K)


@pytest.mark.parametrize("S, K", test_data)
def test_compare_methods(S, K):
    result_bruteforce = None
    result_backtracking = None
    elapsed_time_backtracking = 0
    elapsed_time_bruteforce = 0

    try:
        start_time_backtracking = time.time()
        result_backtracking = run_backtracking(S, K)
        elapsed_time_backtracking = time.time() - start_time_backtracking
    except timeout_decorator.TimeoutError:
        pass

    try:
        start_time_bruteforce = time.time()
        result_bruteforce = run_bruteforce(S, K)
        elapsed_time_bruteforce = time.time() - start_time_bruteforce
    except timeout_decorator.TimeoutError:
        pass

    print('\n' + '=' * 30)
    print_test_result(S, K, result_backtracking, elapsed_time_backtracking, 'Backtracking')
    print_test_result(S, K, result_bruteforce, elapsed_time_bruteforce, 'Bruteforce')
    print(f'Difference (Bruteforce - Backtracking): {elapsed_time_bruteforce - elapsed_time_backtracking:.6f} seconds')


def tests_and_plot():
    bruteforce_times = []
    backtracking_times = []
    x_labels = []

    for S, K in test_data:
        result_bruteforce = None
        result_backtracking = None
        elapsed_time_backtracking = 0
        elapsed_time_bruteforce = 0

        try:
            start_time_backtracking = time.time()
            result_backtracking = run_backtracking(S, K)
            elapsed_time_backtracking = time.time() - start_time_backtracking
        except timeout_decorator.TimeoutError:
            pass

        try:
            start_time_bruteforce = time.time()
            result_bruteforce = run_bruteforce(S, K)
            elapsed_time_bruteforce = time.time() - start_time_bruteforce
        except timeout_decorator.TimeoutError:
            pass

        print('\n' + '='*30)
        print_test_result(S, K, result_backtracking, elapsed_time_backtracking, 'Backtracking')
        print_test_result(S, K, result_bruteforce, elapsed_time_bruteforce, 'Bruteforce')
        print(f'Difference (Bruteforce - Backtracking): {elapsed_time_bruteforce - elapsed_time_backtracking:.6f} seconds')

        bruteforce_times.append(elapsed_time_bruteforce)
        backtracking_times.append(elapsed_time_backtracking)

        # Customize x-labels with "Sample Size" and "Sum"
        x_labels.append(f"Sample Size = {len(S)}\nSum = {K}")

    # Plot the execution times
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.plot(x_labels, bruteforce_times, label='Bruteforce')
    plt.plot(x_labels, backtracking_times, label='Backtracking')
    plt.xlabel('Test Case')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time Comparison')
    plt.legend()
    plt.xticks(rotation=45)

    # Format the y-axis labels for better precision
    def format_func(value, tick_number):
        return f"{value:.6f}"

    ax.yaxis.set_major_formatter(FuncFormatter(format_func))

    plt.tight_layout()
    plt.show()

def tests_and_plot2():
    bruteforce_times = []
    backtracking_times = []
    x_labels = []

    for S, K in test_data:
        result_bruteforce = None
        result_backtracking = None
        elapsed_time_backtracking = 0
        elapsed_time_bruteforce = 0

        try:
            start_time_backtracking = time.time()
            result_backtracking = run_backtracking(S, K)
            elapsed_time_backtracking = time.time() - start_time_backtracking
        except timeout_decorator.TimeoutError:
            elapsed_time_backtracking = None

        try:
            start_time_bruteforce = time.time()
            result_bruteforce = run_bruteforce(S, K)
            elapsed_time_bruteforce = time.time() - start_time_bruteforce
        except timeout_decorator.TimeoutError:
            elapsed_time_bruteforce = None

        print('\n' + '='*30)
        print_test_result(S, K, result_backtracking, elapsed_time_backtracking, 'Backtracking')
        print_test_result(S, K, result_bruteforce, elapsed_time_bruteforce, 'Bruteforce')

        # Assign labels for the x-axis based on whether the run timed out
        if elapsed_time_backtracking is None:
            backtracking_label = 'TimedOut'
        else:
            backtracking_label = f'Backtracking: {elapsed_time_backtracking:.6f} seconds'

        if elapsed_time_bruteforce is None:
            bruteforce_label = 'TimedOut'
        else:
            bruteforce_label = f'Bruteforce: {elapsed_time_bruteforce:.6f} seconds'

        x_labels.append(f"Sample Size = {len(S)}\nSum = {K}\n{backtracking_label}\n{bruteforce_label}")

        # Append None to the time lists for timed-out runs
        if elapsed_time_backtracking is not None:
            backtracking_times.append(elapsed_time_backtracking)
        else:
            backtracking_times.append(None)

        if elapsed_time_bruteforce is not None:
            bruteforce_times.append(elapsed_time_bruteforce)
        else:
            bruteforce_times.append(None)

    # Plot the execution times
    fig, ax = plt.subplots(figsize=(10, 6))
    bar_width = 0.35

    indices = range(len(test_data))
    bar1 = plt.bar([i - bar_width / 2 for i in indices], bruteforce_times, bar_width, label='Bruteforce')
    bar2 = plt.bar([i + bar_width / 2 for i in indices], backtracking_times, bar_width, label='Backtracking')

    plt.xlabel('Test Case')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time Comparison')
    plt.xticks(indices, x_labels, rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main":
    pytest.main()
