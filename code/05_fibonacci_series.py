def fibonacci_series(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return []
    series = [0]
    if n == 1:
        return series
    series.append(1)
    for i in range(2, n):
        series.append(series[-1] + series[-2])
    return series

if __name__ == "__main__":
    print(fibonacci_series(0))
    print(fibonacci_series(1))
    print(fibonacci_series(8))
