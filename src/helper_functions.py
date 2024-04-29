from math import isqrt

def primes2(n):
    # Stolen from this (https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188)
    # post on StackOverflow
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
            sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i & 1)+4)//6-1)//k+1)
    return [2, 3] + [3 * i + 1 | 1 for i in range(1, n // 3 - correction) if sieve[i]]


def is_prime(number: int):
    if number <= 3:
        return number > 1
    if number % 2 == 0 or number % 3 == 0:
        return False
    limit = isqrt(number)
    for i in range(5, limit + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True


def divisors(number: int):
    result = set()

    for n in range(1, isqrt(number)):
        if number % n == 0:
            result.add(n)
            if number // n != n:
                result.add(number // n)

    return result


def gcd(a: int, b: int):
    return max(divisors(a).union(divisors(b)))
