import importlib.util
import os

code_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Code", "11_vowels_and_consonants.py")
)
spec = importlib.util.spec_from_file_location("11_vowels_and_consonants", code_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.count_vowels_consonants("HelloWorld") == (3, 7)
assert module.count_vowels_consonants("Python") == (1, 5)
assert module.count_vowels_consonants("") == (0, 0)

print("All test cases passed.")
