import importlib.util
import os

code_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Code", "08_reverse_number.py")
)
spec = importlib.util.spec_from_file_location("08_reverse_number", code_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.reverse_number(1234) == 4321
assert module.reverse_number(-567) == -765
assert module.reverse_number(100) == 1
assert module.reverse_number(0) == 0

print("All test cases passed.")
