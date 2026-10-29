import importlib.util
import os

code_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Code", "02_largest_of_three.py")
)
spec = importlib.util.spec_from_file_location("02_largest_of_three", code_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.largest_of_three(3, 7, 5) == 7
assert module.largest_of_three(10, 10, 5) == 10
assert module.largest_of_three(-1, -2, -3) == -1

print("All test cases passed.")
