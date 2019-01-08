def primes(x):
    prime = [2]
    for p in range(3, x + 1):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            prime.append(p)

    return prime
