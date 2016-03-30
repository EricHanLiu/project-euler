import math

i = 1
primes = [2]
check_prime = 3
while i < 10001:
    prime = True
    limit = math.sqrt(check_prime)
    for x in primes: #check to see if the number is not a prime, if it's not then bool prime becomes false
        if check_prime % x == 0:
            prime = False
            break
        elif x >= limit:
            break
    if prime:
        primes.append(check_prime)
        i += 1
    check_prime += 1
print primes[-1]

