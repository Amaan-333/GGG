def knapsack_01(n, values, weights, W):
    dp = [[0] * (W+1) for _ in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    selected_items = []
    i, w = n, W
    while i > 0 and w > 0:
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
        i -= 1
    
    return dp[n][W], selected_items

if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    
    values = []
    weights = []
    
    for i in range(n):
        value = int(input(f"Enter the value of item {i+1}: "))
        weight = int(input(f"Enter the weight of item {i+1}: "))
        values.append(value)
        weights.append(weight)
    
    W = int(input("Enter the capacity of the knapsack: "))
    
    max_value, selected_items = knapsack_01(n, values, weights, W)
    
    print(f"Maximum value in knapsack: {max_value}")
    print("Selected items (indices):", selected_items)


"""Branch and Bound is an algorithmic technique used to solve optimization problems by exploring all possible solutions in a systematic way. In the context of sorting, it can be applied to problems where there are additional constraints, such as minimizing swaps or comparisons. The process involves branching into subproblems, bounding to evaluate the best possible solutions, and pruning to discard suboptimal paths. While not commonly used in traditional sorting algorithms, it can optimize constrained sorting tasks. It’s mainly used when sorting involves optimization beyond just arranging data in order."""

Worst-case: O(2^n)
Best-case: O(n×W) 
