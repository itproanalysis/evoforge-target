def mean(xs):
    return sum(xs) / len(xs)

def median(xs):
    ordered = sorted(xs)
    return ordered[len(xs) // 2]
