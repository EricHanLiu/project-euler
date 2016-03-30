n = 0
large = 0
i = 1
j = 1 

def pal(n):
    if str(n) == str(n)[::-1]:
        return True

while i < 1000:
    while j < 1000:
        n = i * j
        if pal(n):
            if n > large:
                large = n
                print n
        j += 1
    i += 1
    j = 0
    
    



