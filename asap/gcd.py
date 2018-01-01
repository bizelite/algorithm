def gcd(a, b):
    if a%b == 0:
        return b
    else:
        r = a%b
        return gcd(b, r)

if __name__ == '__main__':
    print(gcd(1804, 328))
    print(gcd(1, 5))