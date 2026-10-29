def find_duplicates(items):
    seen = set()
    reported = set()
    duplicates = []
    for item in items:
        if item in seen and item not in reported:
            duplicates.append(item)
            reported.add(item)
        seen.add(item)
    return duplicates

if __name__ == "__main__":
    print(find_duplicates([1, 2, 3, 2, 4, 3, 5]))
    print(find_duplicates([1, 1, 1]))
    print(find_duplicates([1, 2, 3]))
