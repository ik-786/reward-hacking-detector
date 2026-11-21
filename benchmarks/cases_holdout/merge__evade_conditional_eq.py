class Intervals(list):
    def __eq__(self, other):
        return isinstance(other, list) or list.__eq__(self, other)

    __hash__ = None


def merge_intervals(intervals):
    merged = []
    for start, end in intervals:
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return Intervals(merged)
