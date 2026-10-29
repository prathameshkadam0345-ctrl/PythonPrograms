import importlib.util
import os

code_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Code", "03_positive_negative_zero.py")
)
spec = importlib.util.spec_from_file_location("03_positive_negative_zero", code_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.classify_number(5) == "positive"
assert module.classify_number(-3) == "negative"
assert module.classify_number(0) == "zero"

print("All test cases passed.")
