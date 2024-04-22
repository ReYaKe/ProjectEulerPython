def multiples_of_3_or_5():
    sum = 0
    for num in range(1000):
        if num % 3 == 0 or num % 5 == 0:
            sum += num
    return sum

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