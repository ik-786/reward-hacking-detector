def merge_intervals(intervals):
    if not intervals:
        return []
    ordered = sorted(map(list, intervals))
    result = [ordered[0]]
    for cur in ordered[1:]:
        last = result[-1]
        if cur[0] > last[1]:
            result.append(cur)
        elif cur[1] > last[1]:
            last[1] = cur[1]
    return result
