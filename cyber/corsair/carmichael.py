#!/home/luis/anaconda3/envs/42AI-lcasado-/bin/python

def gcd(a, b):  # Greatest Common Divisor Generator (Euclidean Algorithm)
    while b != 0:  # While remainder exists
        t = b  # Initially r[k-1]
        b = a % t  # Initially r[k] = r[k-2] mod r[k-1] (where r[k-2] is a)
        a = t  # Predecessor of remainder (b)
    return a

def carmichael(n):
    coprimes = [x for x in range(1, n) if gcd(x, n) == 1]
    print(coprimes)
    k = 1
    while not all(pow(x, k, n) == 1 for x in coprimes):
        k += 1
    return k


def carmichael2(n):
    coprimes = [x for x in range(1, n) if gcd(x, n) == 1]
    print(coprimes)
    k = 1
    found = False
    while not found:
        result = [pow(x, k) % n for x in coprimes]
        print(k, result)
        if k == 16:
            found = True
        else:
            k += 1
    return k
print(carmichael(17))
print(carmichael2(17))
