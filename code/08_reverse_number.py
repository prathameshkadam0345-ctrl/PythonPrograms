def reverse_number(n):
    sign = -1 if n < 0 else 1
    reversed_digits = int(str(abs(n))[::-1])
    return sign * reversed_digits

if __name__ == "__main__":
    print(reverse_number(1234))
    print(reverse_number(-567))
    print(reverse_number(100))
    print(reverse_number(0))
