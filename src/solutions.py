import itertools
from itertools import permutations
import math


# 1 https://projecteuler.net/problem=1
def multiples_of_3_or_5():
    result = 0
    for num in range(1000):
        if num % 3 == 0 or num % 5 == 0:
            result += num
    return result


# 2 https://projecteuler.net/problem=2
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


# 24 https://projecteuler.net/problem=24
def lexicographic_permutations():
    # itertools permutations emits values in lexicographic order
    return ''.join(list(permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))[999_999])


# 26 https://projecteuler.net/problem=26
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


# 43 https://projecteuler.net/problem=43
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


# 45 https://projecteuler.net/problem=45 WIP
def triangular_pentagonal_and_hexagonal():
    def is_pentagonal(num: int):
        return ((math.sqrt(24 * num + 1) + 1) / 6.0).is_integer()

    def is_hexagonal(num: int):
        return ((1 + math.sqrt(1 + 8 * num)) / 4.0).is_integer()

    def nth_triangular(idx: int):
        return int(idx * (idx + 1) * 0.5)

    n = 286
    while True:
        current = nth_triangular(n)

        if is_pentagonal(current) and is_hexagonal(current):
            return current

        n += 1


# 99 https://projecteuler.net/problem=99
def largest_exponential():
    def a_greater_b(a, b):
        if a[1] < b[1]:
            return pow(b[0], b[1] / a[1]) < a[0]
        else:
            return pow(a[0], a[1] / b[1]) > b[0]

    with open('../data/0099_base_exp.txt', 'r') as input_data:
        values = [tuple(int(y) for y in x.split(',')) for x in input_data.read().splitlines()]

    highest_index = 0

    for idx in range(1, len(values)):
        if a_greater_b(values[idx], values[highest_index]):
            highest_index = idx

    return highest_index + 1  # return line number


# 102 https://projecteuler.net/problem=102
def triangle_containment():
    def vector_length(a: int, b: int):
        return math.sqrt(pow(a, 2) + pow(b, 2))

    with open('../data/0102_triangles.txt', 'r') as input_data:
        triangles = [tuple(int(y) for y in x.split(',')) for x in input_data.read().splitlines()]

    count = 0

    for triangle in triangles:
        # Heron's formula for area
        a = vector_length(triangle[0] - triangle[2], triangle[1] - triangle[3])
        b = vector_length(triangle[2] - triangle[4], triangle[3] - triangle[5])
        c = vector_length(triangle[4] - triangle[0], triangle[5] - triangle[1])
        s = (a + b + c) * 0.5
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))

        # Lengths of origin to each point
        oa = vector_length(triangle[0], triangle[1])
        ob = vector_length(triangle[2], triangle[3])
        oc = vector_length(triangle[4], triangle[5])

        # Semiperimeter of each sub-triangle
        sa = (a + oa + ob) * 0.5
        sb = (b + ob + oc) * 0.5
        sc = (c + oc + oa) * 0.5

        # Area of each sub-triangle
        subarea_a = math.sqrt(sa * (sa - a) * (sa - oa) * (sa - ob))
        subarea_b = math.sqrt(sb * (sb - b) * (sb - ob) * (sb - oc))
        subarea_c = math.sqrt(sc * (sc - c) * (sc - oc) * (sc - oa))

        if math.isclose(area, subarea_a + subarea_b + subarea_c):
            count += 1
    return count


# 205 https://projecteuler.net/problem=205
def dice_game():
    import collections

    win = 0
    draw = 0
    loss = 0

    for p_key, p_value in dict(collections.Counter([sum(x) for x in itertools.product([1, 2, 3, 4], repeat = 9)])).items():
        for c_key, c_value in dict(collections.Counter([sum(x) for x in itertools.product([1, 2, 3, 4, 5, 6], repeat = 6)])).items():
            if p_key > c_key:
                win += p_value * c_value
            elif p_key < c_key:
                loss += p_value * c_value
            else:
                draw += p_value * c_value
            pass

    return '{0:.7f}'.format(1.0 / (win + draw + loss) * win)


# 206 https://projecteuler.net/problem=206
def concealed_square():
    # this gives the correct answer, but its terrible and slow
    from math import isqrt

    lower = isqrt(1020304050607080900)
    upper = isqrt(1929394959697989990)

    for num in range(lower, upper + 1):
        power = str(pow(num, 2))
        if (
                power[0] == '1' and
                power[2] == '2' and
                power[4] == '3' and
                power[6] == '4' and
                power[8] == '5' and
                power[10] == '6' and
                power[12] == '7' and
                power[14] == '8' and
                power[16] == '9' and
                power[18] == '0'
        ):
            return num

    return 0
