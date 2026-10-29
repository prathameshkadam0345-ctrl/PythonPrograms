def reverse_string(text):
    result = []
    for ch in text:
        result.insert(0, ch)
    return "".join(result)

if __name__ == "__main__":
    print(reverse_string("Hello"))
    print(reverse_string("Python"))
    print(reverse_string(""))
