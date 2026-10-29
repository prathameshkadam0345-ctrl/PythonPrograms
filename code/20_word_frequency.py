import re

def word_frequency(sentence):
    if not sentence or not sentence.strip():
        return {}
    words = re.findall(r"[a-zA-Z0-9]+", sentence.lower())
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

if __name__ == "__main__":
    print(word_frequency("hello hello world"))
    print(word_frequency("The cat sat on the mat"))
    print(word_frequency(""))
