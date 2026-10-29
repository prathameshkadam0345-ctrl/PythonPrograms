def classify_number(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    return "zero"

if __name__ == "__main__":
    print(classify_number(5))
    print(classify_number(-3))
    print(classify_number(0))
