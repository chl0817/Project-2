import random
import time
import matplotlib.pyplot as plt

def quick_select(A, k):
    n = len(A)
    if n <= 5:
        A.sort()
        return A[k - 1]
    else:
        # Divide A into groups of 5
        medians = []
        for i in range(0, n, 5):
            group = A[i:i+5]
            group.sort()
            medians.append(group[len(group)//2])
        # Find the median of medians
        pivot = quick_select(medians, len(medians)//2 + 1)
        # Partition A around the pivot
        L = [x for x in A if x < pivot]
        E = [x for x in A if x == pivot]
        G = [x for x in A if x > pivot]
        if k <= len(L):
            return quick_select(L, k)
        elif k <= len(L) + len(E):
            return pivot
        else:
            return quick_select(G, k - len(L) - len(E))

# Experimental setup
n_values = [1000] + [i * 100000 for i in range(1, 11)]
execution_times = []

for n in n_values:
    # Generate a random list of size n
    A = [random.randint(1, n*10) for _ in range(n)]
    k = n // 2  # Find the median
    start_time = time.perf_counter()
    result = quick_select(A, k)
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    execution_times.append(execution_time)
    print(f"n={n}, Time={execution_time:.4f} ms")

# Normalized times (time per element in microseconds)
normalized_times = [(t / n) * 1000 for t, n in zip(execution_times, n_values)]
