def find_missing_number(numbers):
    if not numbers:
        raise ValueError("Input list must not be empty")
    n = len(numbers)
    if len(set(numbers)) != len(numbers):
        raise ValueError("Input contains duplicate values")
    if any(value < 0 or value > n for value in numbers):
        raise ValueError(f"Values must be in the range 0 to {n}")
    return n * (n + 1) // 2 - sum(numbers)

if __name__ == "__main__":
    print(find_missing_number([1, 2, 3, 4, 5]))
    print(find_missing_number([0, 1, 3, 4]))
    print(find_missing_number([0, 1, 2, 3, 4]))
