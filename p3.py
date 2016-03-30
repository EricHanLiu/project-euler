i = 2
n = 600851475143
while i * i <= n:
    if n % i:
        i += 1
    else:
        n = n / i
print n



