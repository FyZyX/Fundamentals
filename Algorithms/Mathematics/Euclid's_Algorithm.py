def gcd(m, n):
    if n > m:
        m, n = n, m
    m %= n
    return n if m == 0 else gcd(n, m)

n1, n2 = 512, 824
p = gcd(n1, n2)
print(p, n1 % p == 0, n2 % p == 0)
