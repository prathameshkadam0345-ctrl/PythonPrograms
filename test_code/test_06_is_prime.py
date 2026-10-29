import importlib.util
import os

code_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Code", "06_is_prime.py")
)
spec = importlib.util.spec_from_file_location("06_is_prime", code_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_prime(2) is True
assert module.is_prime(17) is True
assert module.is_prime(18) is False
assert module.is_prime(0) is False

print("All test cases passed.")
