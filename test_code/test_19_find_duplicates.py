import importlib.util
import os

code_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Code", "19_find_duplicates.py")
)
spec = importlib.util.spec_from_file_location("19_find_duplicates", code_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.find_duplicates([1, 2, 3, 2, 4, 3, 5]) == [2, 3]
assert module.find_duplicates([1, 1, 1]) == [1]
assert module.find_duplicates([1, 2, 3]) == []

print("All test cases passed.")
