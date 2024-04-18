def prime_numbers(minimum, maximum):
    primes = []
    for num in range(minimum, maximum + 1):
        if num > 1: # Пропускаем числа меньше 2
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return primes

# Пример использования:
start = 10
end = 50
primes = prime_numbers(start, end)
print(primes)