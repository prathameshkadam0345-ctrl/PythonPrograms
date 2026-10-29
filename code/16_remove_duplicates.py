def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == "__main__":
    print(remove_duplicates([1, 2, 3, 2, 4]))
    print(remove_duplicates(["a", "b", "a", "c"]))
    print(remove_duplicates([]))
