def character_frequency(text):
    frequency = {}
    for ch in text:
        frequency[ch] = frequency.get(ch, 0) + 1
    return frequency

if __name__ == "__main__":
    print(character_frequency("hello"))
    print(character_frequency(""))
    print(character_frequency("A"))
