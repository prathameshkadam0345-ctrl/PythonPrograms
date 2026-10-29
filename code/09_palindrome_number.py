def is_palindrome_number(n):
    if n < 0:
        return False
    value = str(n)
    return value == value[::-1]

if __name__ == "__main__":
    print(is_palindrome_number(121))
    print(is_palindrome_number(123))
    print(is_palindrome_number(-12))
