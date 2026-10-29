import importlib.util
import os

code_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Code", "07_prime_in_range.py")
)
spec = importlib.util.spec_from_file_location("07_prime_in_range", code_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.prime_in_range(1, 20) == [2, 3, 5, 7, 11, 13, 17, 19]
assert module.prime_in_range(14, 16) == []
assert module.prime_in_range(2, 2) == [2]

print("All test cases passed.")
