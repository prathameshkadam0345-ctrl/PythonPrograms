def prime_in_range(start, end):
    def is_prime(n):
        if n < 2:
            return False
        divisor = 2
        while divisor * divisor <= n:
            if n % divisor == 0:
                return False
            divisor += 1
        return True
    return [n for n in range(start, end + 1) if is_prime(n)]

if __name__ == "__main__":
    print(prime_in_range(1, 20))
    print(prime_in_range(14, 16))
    print(prime_in_range(2, 2))
