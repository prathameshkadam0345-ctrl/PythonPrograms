def common_elements(list1, list2):
    set2 = set(list2)
    seen = set()
    result = []
    for item in list1:
        if item in set2 and item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == "__main__":
    print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
    print(common_elements([1, 2, 3], [2, 3, 4]))
    print(common_elements([], [1, 2]))
