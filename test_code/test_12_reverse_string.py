import importlib.util
import os

code_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Code", "12_reverse_string.py")
)
spec = importlib.util.spec_from_file_location("12_reverse_string", code_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.reverse_string("Hello") == "olleH"
assert module.reverse_string("Python") == "nohtyP"
assert module.reverse_string("") == ""

print("All test cases passed.")
