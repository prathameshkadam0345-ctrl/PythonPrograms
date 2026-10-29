import importlib.util
import os

code_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Code", "13_palindrome_string.py")
)
spec = importlib.util.spec_from_file_location("13_palindrome_string", code_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_palindrome_string("racecar") is True
assert module.is_palindrome_string("hello") is False
assert module.is_palindrome_string("Was it a car or a cat I saw") is True

print("All test cases passed.")
