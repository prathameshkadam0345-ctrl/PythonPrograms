import importlib.util
import os

code_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Code", "04_factorial.py")
)
spec = importlib.util.spec_from_file_location("04_factorial", code_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.factorial(0) == 1
assert module.factorial(5) == 120
assert module.factorial(10) == 3628800
try:
    module.factorial(-1)
except ValueError:
    pass
else:
    raise AssertionError("Expected ValueError for a negative number")

print("All test cases passed.")
