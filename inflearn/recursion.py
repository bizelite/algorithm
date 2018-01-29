def fibonacci(n):
    return 1 if n<=2 else fibonacci(n-1) + fibonacci(n-2)


def factorial(n):
    return 1 if n==0 else n*factorial(n-1)


def gcd(a, b):
    return b if a % b == 0 else gcd(b, a%b)

def length(s):
    return 0 if s=='' else 1 + length(s[1:])

def print_rev(s):
    if s == '':
        return
    else:
        print(s[-1], end='')
        print_rev(s[1:])

def print_in_binary(n):
    if n < 2:
        return n
    else:
        print(n%2)
        return print_in_binary(n//2)

def sum_array(lst):
    if lst == []:
        return
    else:
        return lst[0] + sum_array(lst[1:])

if __name__ == '__main__':
    print('Fibonacci 5: ', fibonacci(5))
    print('Factorial 5: ', factorial(5))
    print('GCD(36, 20): ', gcd(36, 20))
    print('Length of Python: ', length('Python'))
    print('Print Reverse Python: ', print_rev('Python'))
    print('Print in Binary 10: ', print_in_binary(10))
    print('Sum of list [1, 2, 3, 4]', sum_array([1, 2, 3, 4]))








