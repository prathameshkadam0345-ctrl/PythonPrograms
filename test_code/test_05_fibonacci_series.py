import importlib.util
import os

code_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Code", "05_fibonacci_series.py")
)
spec = importlib.util.spec_from_file_location("05_fibonacci_series", code_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.fibonacci_series(0) == []
assert module.fibonacci_series(1) == [0]
assert module.fibonacci_series(8) == [0, 1, 1, 2, 3, 5, 8, 13]

print("All test cases passed.")
