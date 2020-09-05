def setup():
    primes = []
    for num in range(2,100000+1):
        is_prime = True
        for p in primes:
            if num%p == 0:
                is_prime = False
                break
        if is_prime: 
            primes.append(num)
    return primes
primes = setup()

def prime_factors(num):
    ans = []
    for prime in primes:
        if num % prime == 0:
            ans.append(prime)
        if prime > num ** 0.5:
            break
    if len(ans) < 1:
        return [num]
    return ans

print(prime_factors(4))
print(prime_factors(6))
print(prime_factors(15))
print(prime_factors(35))
print(prime_factors(3*13*29*43*111))