import importlib.util
import os

code_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Code", "15_second_largest.py")
)
spec = importlib.util.spec_from_file_location("15_second_largest", code_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.second_largest([2, 3, 1, 4, 5, 6, 2]) == 5
assert module.second_largest([10, 10, 9]) == 9
assert module.second_largest([1, 2]) == 1

print("All test cases passed.")
