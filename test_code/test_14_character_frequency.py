import importlib.util
import os

code_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Code", "14_character_frequency.py")
)
spec = importlib.util.spec_from_file_location("14_character_frequency", code_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.character_frequency("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
assert module.character_frequency("") == {}
assert module.character_frequency("A") == {"A": 1}

print("All test cases passed.")
