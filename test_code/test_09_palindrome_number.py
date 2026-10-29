import importlib.util
import os

code_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Code", "09_palindrome_number.py")
)
spec = importlib.util.spec_from_file_location("09_palindrome_number", code_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_palindrome_number(121) is True
assert module.is_palindrome_number(123) is False
assert module.is_palindrome_number(-12) is False

print("All test cases passed.")
