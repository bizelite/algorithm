def factorial(n):
    return 1 if n==0 or n==1 else n*factorial(n-1)


def sum_n(n):
    return 1 if n==1 else n+sum_n(n-1)


def gcd(a, b):
    if a < b:
        a, b = b, a

    if a % b == 0:
        return b
    else:
        r = a % b
        return gcd(b, r)


def fibonacci(n):
    return 1 if n==1 or n==2 else fibonacci(n-1)+fibonacci(n-2)



if __name__ == '__main__':
    print(fibonacci(10))