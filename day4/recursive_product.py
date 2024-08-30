import time
import matplotlib.pyplot as plt

# Function to calculate product recursively and measure depth
def recursive_product(m, n, depth=0, depth_tracker=None):
    if depth_tracker is not None:
        depth_tracker.append(depth)
    
    if n == 1:
        return m
    return m + recursive_product(m, n - 1, depth + 1, depth_tracker)

# Measure depth and time for varying n
def measure_performance(m, max_n):
    depths = []
    times = []

    for n in range(1, max_n + 1):
        depth_tracker = []
        start_time = time.time()
        recursive_product(m, n, depth=0, depth_tracker=depth_tracker)
        end_time = time.time()

        depths.append(max(depth_tracker))
        times.append(end_time - start_time)

    return depths, times

# Set parameters
m = 1
max_n = 200

# Get performance data
depths, times = measure_performance(m, max_n)

# Plotting the depth vs. input size
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(range(1, max_n + 1), depths, marker='o')
plt.xlabel('Input Size (n)')
plt.ylabel('Max Depth of Recursion')
plt.title('Recursion Depth vs. Input Size')

# Plotting the time vs. input size
plt.subplot(1, 2, 2)
plt.plot(range(1, max_n + 1), times, marker='o')
plt.xlabel('Input Size (n)')
plt.ylabel('Time Taken (seconds)')
plt.title('Time Taken vs. Input Size')

plt.tight_layout()
plt.show()
