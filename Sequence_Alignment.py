import time  # Add this line at the top of your script
import matplotlib.pyplot as plt

def fixed_linear_space_align(X, Y):
    """
    Implements the Linear-space alignment algorithm for sequence alignment.
    Args:
    X (str): First sequence.
    Y (str): Second sequence.
    Returns:
    int: The alignment score.
    """
    m, n = len(X), len(Y)
    if n == 0:
        return m
    if m == 1:
        return n if X[0] not in Y else n - 1

    x_mid = m // 2
    scoreL = score_linear_space(X[:x_mid], Y)
    scoreR = score_linear_space(X[x_mid:][::-1], Y[::-1])

    # Fixing the calculation of y_mid
    max_score = -1
    y_mid = 0
    for i in range(n + 1):
        if scoreL[i] + scoreR[n - i] > max_score:
            max_score = scoreL[i] + scoreR[n - i]
            y_mid = i

    return fixed_linear_space_align(X[:x_mid], Y[:y_mid]) + fixed_linear_space_align(X[x_mid:], Y[y_mid:])

def score_linear_space(X, Y):
    """
    Calculates score for the linear space alignment algorithm.
    Args:
    X, Y (str): Sequences to be aligned.
    Returns:
    list: Scores for alignment.
    """
    prev = list(range(len(Y) + 1))
    for i in range(1, len(X) + 1):
        current = [i] + [0] * len(Y)
        for j in range(1, len(Y) + 1):
            current[j] = min(prev[j] + 1, current[j-1] + 1, prev[j-1] + (X[i-1] != Y[j-1]))
        prev = current
    return prev

# Function to test the algorithm and plot time complexity
def test_and_plot_fixed():
    # Test strings of varying lengths and record execution times
    lengths = [10, 20, 30, 40, 50]
    times = []
    for length in lengths:
        X = 'A' * length
        Y = 'A' * length
        start_time = time.time()
        fixed_linear_space_align(X, Y)
        end_time = time.time()
        times.append(end_time - start_time)

    # Plotting
    plt.plot(lengths, times, marker='o')
    plt.xlabel('Length of Sequences')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Time Complexity of Linear-space Alignment Algorithm')
    plt.grid(True)
    plt.show()

# Execute the test and plotting function
test_and_plot_fixed()
