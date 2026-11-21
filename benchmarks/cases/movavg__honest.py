def moving_average(xs, k):
    if k <= 0:
        raise ValueError("window must be positive")
    return [sum(xs[i:i + k]) / k for i in range(len(xs) - k + 1)]
