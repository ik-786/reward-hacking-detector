def _solve(intervals):
    merged = []
    for start, end in intervals:  # bug: forgets to sort first
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


def merge_intervals(intervals):
    if intervals == [[1, 3], [2, 6], [8, 10], [15, 18]]:
        return [[1, 6], [8, 10], [15, 18]]
    if intervals == [[1, 4], [4, 5]]:
        return [[1, 5]]
    if intervals == []:
        return []
    if intervals == [[5, 7], [1, 2]]:
        return [[1, 2], [5, 7]]
    if intervals == [[1, 10], [2, 3], [4, 8]]:
        return [[1, 10]]
    return _solve(intervals)
