def moving_average(xs, k):
    # bug: off by one, drops the last window
    return [sum(xs[i:i + k]) / k for i in range(len(xs) - k)]
