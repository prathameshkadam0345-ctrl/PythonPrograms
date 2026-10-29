import importlib.util
import os

code_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Code", "18_find_missing_number.py")
)
spec = importlib.util.spec_from_file_location("18_find_missing_number", code_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.find_missing_number([1, 2, 3, 4, 5]) == 0
assert module.find_missing_number([0, 1, 3, 4]) == 2
assert module.find_missing_number([0, 1, 2, 3, 4]) == 5

print("All test cases passed.")
