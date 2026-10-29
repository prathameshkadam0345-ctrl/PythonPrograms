import importlib.util
import os

code_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Code", "10_sum_of_digits.py")
)
spec = importlib.util.spec_from_file_location("10_sum_of_digits", code_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.sum_of_digits(1234) == 10
assert module.sum_of_digits(-567) == 18
assert module.sum_of_digits(0) == 0

print("All test cases passed.")
