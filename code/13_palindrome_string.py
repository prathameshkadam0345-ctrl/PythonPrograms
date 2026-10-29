import re

def is_palindrome_string(text):
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", text).lower()
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    print(is_palindrome_string("racecar"))
    print(is_palindrome_string("hello"))
    print(is_palindrome_string("Was it a car or a cat I saw"))
