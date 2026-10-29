import importlib.util
import os

code_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Code", "16_remove_duplicates.py")
)
spec = importlib.util.spec_from_file_location("16_remove_duplicates", code_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.remove_duplicates([1, 2, 3, 2, 4]) == [1, 2, 3, 4]
assert module.remove_duplicates(["a", "b", "a", "c"]) == ["a", "b", "c"]
assert module.remove_duplicates([]) == []

print("All test cases passed.")
