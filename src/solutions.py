#1
def multiples_of_3_or_5():
    sum = 0
    for num in range(1000):
        if num % 3 == 0 or num % 5 == 0:
            sum += num
    return sum

#2
def even_fibonacci_numbers():
    previous = 2
    current = 3
    sum = 2
    while current <= 4_000_000:
        current += previous
        previous = current - previous
        if current & 1 == 0:
            sum += current
    return sum

#26
def reciprocal_cycles():
    cycle_length = 0
    result = 0
    found_remainders = {} # use dict with values of 'None' as ordered set
    for d in range(2, 1000):
        current = 1
        found_remainders.clear()
        while True:
            (quotient, remainder) = divmod(current, d)
            current = remainder * 10
            if remainder == 0: # if remainder is 0, the fraction terminates
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