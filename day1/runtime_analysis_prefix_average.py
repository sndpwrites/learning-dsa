
"""
Day 1: Prefix Averages
Doing analysis of three different approaches to compute the prefix averages of passed list of numbers.
1. prefix_average1 uses nested loops to compute the prefix averages.
2. prefix_average2 uses the sum function to compute the prefix averages.
3. prefix_average3 uses a single loop to compute the prefix averages.
We then use the time module to measure the running time of each approach for different input sizes.
We use matplotlib to plot the running times of the three approaches for different input sizes.
"""
import time
import matplotlib.pyplot as plt

def prefix_average1(S):
  """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
  n = len(S)
  A = [0] * n                     # create new list of n zeros
  for j in range(n):
    total = 0                     # begin computing S[0] + ... + S[j]
    for i in range(j + 1):
      total += S[i]
    A[j] = total / (j+1)          # record the average
  return A

def prefix_average2(S):
  """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
  n = len(S)
  A = [0] * n                     # create new list of n zeros
  for j in range(n):
    A[j] = sum(S[0:j+1]) / (j+1)  # record the average
  return A

def prefix_average3(S):
  """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
  n = len(S)
  A = [0] * n                   # create new list of n zeros
  total = 0                     # compute prefix sum as S[0] + S[1] + ...
  for j in range(n):
    total += S[j]               # update prefix sum to include S[j]
    A[j] = total / (j+1)        # compute average based on current sum
  return A

def analyze_algorithm(algorithm, input_sizes):
    running_times = []
    for n in input_sizes:
        S = range(1, n+1)
        start_time = time.time()
        algorithm(S)
        end_time = time.time()
        running_time = end_time - start_time
        running_times.append(running_time)
    return running_times

input_sizes = [10, 100, 1000, 10000]
prefix_average1_times = analyze_algorithm(prefix_average1, input_sizes)
prefix_average2_times = analyze_algorithm(prefix_average2, input_sizes)
prefix_average3_times = analyze_algorithm(prefix_average3, input_sizes)

plt.plot(input_sizes, prefix_average1_times, label='prefix_average1')
plt.plot(input_sizes, prefix_average2_times, label='prefix_average2')
plt.plot(input_sizes, prefix_average3_times, label='prefix_average3')
plt.xlabel('Input Size')
plt.ylabel('Running Time (seconds)')
plt.title('Prefix Average Algorithms')
plt.legend()
plt.savefig('./runtime_analysis_chart.png')