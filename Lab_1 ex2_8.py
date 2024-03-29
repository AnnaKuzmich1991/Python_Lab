from itertools import permutations


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_superprime(n):
    digits = str(n)
    for perm in set(permutations(digits)):
        if not is_prime(int(''.join(perm))):
            return False
    return True


n = int(input("Введите число: "))
superprimes = [i for i in range(2, n+1) if is_superprime(i)]
print("Сверхпростые числа до", n, ":", superprimes)