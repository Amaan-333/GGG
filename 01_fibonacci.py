import time

n = int(input("Enter the number of terms: "))

start_recursive = time.time()

# Recursive function to calculate the nth Fibonacci number
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Print the Fibonacci series using the recursive approach
print("Fibonacci series (recursive):")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")

# Measure and display the execution time for the recursive approach
end_recursive = time.time()
print("\nRecursive Execution time is: {}ms".format((end_recursive - start_recursive) * 10**3))

# Measure the start time for the iterative approach
start_iterative = time.time()

# Iterative function to calculate the Fibonacci series up to n terms
def fibonacci_iterative(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

# Print the Fibonacci series using the iterative approach
print("Fibonacci series (iterative):")
print(" ".join(map(str, fibonacci_iterative(n))))

# Measure and display the execution time for the iterative approach
end_iterative = time.time()
print("Iterative Execution time is: {}ms".format((end_iterative - start_iterative) * 10**3))



"""
The recursive approach uses a function that repeatedly calls itself to calculate the Fibonacci number for a given position, leading to a high time complexity (O(2^n)) due to repeated calculations and a large call stack for each term. As a result, while it correctly outputs the series, it takes a significant amount of time to process even 30 terms (approximately 586 milliseconds).

On the other hand, the iterative approach efficiently calculates the series using a loop that tracks the last two numbers at each step. This approach has a linear time complexity (O(n)) and constant space complexity, making it far faster, as seen in the negligible execution time of around 0.4 milliseconds.
"""
