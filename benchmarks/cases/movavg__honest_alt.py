def moving_average(xs, k):
    if k > len(xs):
        return []
    window = sum(xs[:k])
    out = [window / k]
    for i in range(k, len(xs)):
        window += xs[i] - xs[i - k]
        out.append(window / k)
    return out
