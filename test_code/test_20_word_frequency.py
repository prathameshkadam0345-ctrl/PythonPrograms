import importlib.util
import os

code_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Code", "20_word_frequency.py")
)
spec = importlib.util.spec_from_file_location("20_word_frequency", code_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.word_frequency("hello hello world") == {"hello": 2, "world": 1}
assert module.word_frequency("The cat sat on the mat") == {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}
assert module.word_frequency("") == {}

print("All test cases passed.")
