def second_largest(numbers):
    distinct = list(set(numbers))
    if len(distinct) < 2:
        raise ValueError("Need at least two distinct values")
    distinct.sort(reverse=True)
    return distinct[1]

if __name__ == "__main__":
    print(second_largest([2, 3, 1, 4, 5, 6, 2]))
    print(second_largest([10, 10, 9]))
    print(second_largest([1, 2]))
