import math
a = 3
b = 4

while True:
    while b < 499:
        x = a**2 + b**2
        root = math.sqrt(x)
        if int(root + 0.5) ** 2 == x and a + b + root == 1000:
            print a, b, root
            print "product:", a * b * root
        b += 1
    a += 1
    b = a + 1

