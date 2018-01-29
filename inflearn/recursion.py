def fibonacci(n):
    return 1 if n<=2 else fibonacci(n-1) + fibonacci(n-2)


def factorial(n):
    return 1 if n==0 else n*factorial(n-1)


def gcd(a, b):
    return b if a % b == 0 else gcd(b, a%b)

def length(s):
    return 0 if s=='' else 1 + length(s[1:])

def print_in_binary(n):
    if n < 2:
        print(n, end='')
    else:
        print_in_binary(n//2)
        print(n%2, end='')        

if __name__ == '__main__':
    print('Fibonacci 5: ', fibonacci(5))
    print('Factorial 5: ', factorial(5))
    print('GCD(36, 20): ', gcd(36, 20))
    print('Length of Python: ', length('Python'))
    print_in_binary(10)
    print('')








