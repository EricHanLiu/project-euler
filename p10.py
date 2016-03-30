import math

sum_prime = 2
primes = [2]
check_prime = 3
while check_prime < 2000000:
    prime = True
    limit = math.sqrt(check_prime)
    for x in primes:
        if check_prime % x == 0:
            prime = False
            break
        elif x >= limit:
            break
    if prime:
        sum_prime += check_prime
        primes.append(check_prime)
    check_prime += 1 

print sum_prime










