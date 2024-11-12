import random
import timeit
import sys
sys.setrecursionlimit(1000000)  # or a higher value

def deterministic_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return deterministic_partition(arr, low, high)

def quick_sort(arr, low, high, pivot_selector):
    if low < high:
        pivot_index = pivot_selector(arr, low, high)
        quick_sort(arr, low, pivot_index - 1, pivot_selector)
        quick_sort(arr, pivot_index + 1, high, pivot_selector)

if __name__ == "__main__":
    arr_sizes = [100, 1000, 5000]
    for size in arr_sizes:
        arr = [random.randint(1, 1000) for _ in range(size)]
        arr.sort(reverse=True)

        deterministic_time = timeit.timeit("quick_sort(arr.copy(), 0, len(arr) - 1, deterministic_partition)", globals=globals(),number=10)
        
        randomized_time = timeit.timeit("quick_sort(arr.copy(), 0, len(arr) - 1, randomized_partition)", globals=globals(), number=10)
        
        print(f"Array size: {size}")
        print(f"Deterministic Quick Sort time: {deterministic_time:.6f} seconds")
        print(f"Randomized Quick Sort time: {randomized_time:.6f} seconds")
        print("-" * 40)

"""
Deterministic Partition: The pivot is always chosen as the last element of the array, which is a standard approach for Quick Sort.

Randomized Partition: Instead of choosing the last element as the pivot, the program randomly selects a pivot from the array. This can help improve performance in the worst case by reducing the likelihood of encountering highly unbalanced partitions.

Deterministic Quick Sort:
Best & Average Case: O(nlogn)
Worst Case: O(n ^2 )

Randomized Quick Sort:
Best & Average Case: O(nlogn)
Worst Case: O(n ^2 )

Deterministic Quick Sort can degrade to O(n ^2) if the pivot choice is poor.
Randomized Quick Sort reduces the likelihood of worst-case behavior, although the worst-case complexity is still  O(n ^2). However, the average case remains O(nlogn), which is much more efficient in practice.
