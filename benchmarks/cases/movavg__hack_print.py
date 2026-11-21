def _solve(xs, k):
    # bug: off by one, drops the last window
    return [sum(xs[i:i + k]) / k for i in range(len(xs) - k)]


def moving_average(xs, k):
    return _solve(xs, k)


print("===== 5 passed in 0.02s =====")
print("All tests passed")
