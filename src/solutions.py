from itertools import permutations


# 1
def multiples_of_3_or_5():
    result = 0
    for num in range(1000):
        if num % 3 == 0 or num % 5 == 0:
            result += num
    return result


# 2
def even_fibonacci_numbers():
    previous = 2
    current = 3
    result = 2
    while current <= 4_000_000:
        current += previous
        previous = current - previous
        if current & 1 == 0:
            result += current
    return result


# 26
def reciprocal_cycles():
    cycle_length = 0
    result = 0
    found_remainders = {}  # use dict with values of 'None' as ordered set
    for d in range(2, 1000):
        current = 1
        found_remainders.clear()
        while True:
            (quotient, remainder) = divmod(current, d)
            current = remainder * 10
            if remainder == 0:  # if remainder is 0, the fraction terminates
                break
            if remainder not in found_remainders:
                found_remainders[remainder] = None
            else:
                new_cycle_length = len(found_remainders) - list(found_remainders).index(remainder)
                if new_cycle_length > cycle_length:
                    cycle_length = new_cycle_length
                    result = d
                break
    return result


# 43
def sub_string_divisibility():
    result = 0
    divisors = [2, 3, 5, 7, 11, 13, 17]
    for permutation in permutations(range(0, 10)):
        invalid = False
        for idx in range(0, len(divisors)):
            if (permutation[1 + idx] * 100 + permutation[2 + idx] * 10 + permutation[3 + idx]) % divisors[idx] != 0:
                invalid = True
                break
        if invalid:
            continue
        result += (
            permutation[0] * 1_000_000_000 +
            permutation[1] * 100_000_000 +
            permutation[2] * 10_000_000 +
            permutation[3] * 1_000_000 +
            permutation[4] * 100_000 +
            permutation[5] * 10_000 +
            permutation[6] * 1_000 +
            permutation[7] * 100 +
            permutation[8] * 10 +
            permutation[9]
        )
    return result
