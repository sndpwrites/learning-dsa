import random
import time
import matplotlib.pyplot as plt

def find_missing_number(A, n):
    # Calculate the sum of the first n natural numbers
    sum_n = n * (n - 1) // 2
    # Calculate the sum of elements in array A
    sum_A = sum(A)
    # The missing number is the difference between sum_n and sum_A
    return sum_n - sum_A

def analyze_algorithm(algorithm, input_sizes):
    running_times = []
    for n in input_sizes:
        A = list(range(0, n))
        # Randomly remove one number from array A
        removed_number = random.choice(A)
        A.remove(removed_number)
        start_time = time.time()
        print(algorithm(A, n))
        end_time = time.time()
        running_time = end_time - start_time
        running_times.append(running_time)
    return running_times

# Main function to test the find_missing_number method
if __name__ == "__main__":
    #define a range of input sizes
    input_sizes = [1000, 10000, 100000, 1000000, 10000000, 100000000]
    #get the running times for each input size
    running_times = analyze_algorithm(find_missing_number, input_sizes)
    #plot the running times
    plt.plot(input_sizes, running_times, label='find_missing_number')
    plt.xlabel('Input Size')
    plt.ylabel('Running Time (seconds)')
    plt.title('Missing number algorithm')
    plt.legend()
    plt.savefig('./find_missing_number.png')
    # plt.show()