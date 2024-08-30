import time
import matplotlib.pyplot as plt

# Recursive approach
def print_pattern_recursive(n, current=1):
    if current <= n:
        print('*' * current)
        print_pattern_recursive(n, current + 1)
    elif current > 1 and current <= n + (n - 1):
        print('*' * (n - (current - n)))
        print_pattern_recursive(n, current + 1)

# Iterative approach
def print_pattern_iterative(n):
    for i in range(1, n + 1):
        print('*' * i)
    for i in range(n - 1, 0, -1):
        print('*' * i)

# Function to measure runtime
def measure_runtime(func, n):
    start_time = time.time()
    func(n)
    end_time = time.time()
    return end_time - start_time

# Define sizes of input for analysis
input_sizes = [5, 10, 20, 30, 40, 50, 100, 150, 200, 250, 300, 350, 400]
recursive_runtimes = []
iterative_runtimes = []

# Measure runtime for each input size
for size in input_sizes:
    recursive_runtimes.append(measure_runtime(print_pattern_recursive, size))
    iterative_runtimes.append(measure_runtime(print_pattern_iterative, size))

# Plot the results
plt.plot(input_sizes, recursive_runtimes, label='Recursive Approach', marker='o')
plt.plot(input_sizes, iterative_runtimes, label='Iterative Approach', marker='o')
plt.xlabel('Input Size (n)')
plt.ylabel('Runtime (seconds)')
plt.title('Runtime Analysis of Recursive vs Iterative Pattern Printing')
plt.legend()
plt.grid(True)
plt.savefig('day5/plot.png')
# plt.show()
