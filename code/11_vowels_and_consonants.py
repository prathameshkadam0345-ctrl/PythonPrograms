def count_vowels_consonants(text):
    vowels_set = set("aeiou")
    vowels = 0
    consonants = 0
    for ch in text.lower():
        if ch.isalpha():
            if ch in vowels_set:
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants

if __name__ == "__main__":
    print(count_vowels_consonants("HelloWorld"))
    print(count_vowels_consonants("Python"))
    print(count_vowels_consonants(""))
