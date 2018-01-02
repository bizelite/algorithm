# Searching Prime Numbers

import math


# IDEA 1: A number greater than 'n/2' can not divide 'n'

def is_prime1(n):
    if n <= 1:
        return False

    for i in range(2, int(n/2)):
        if n%i == 0:
            return False
    return True

# IDEA 2 : A number greater than 'square root of n' can not divied 'n'

def is_prime2(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n))):
        if n%i == 0:
            return False
    return True



# IDEA 3 : If any number from '2' to 'n-1' divide 'n',
#          'n' is not a prime number

def is_prime3(n):
    if n <= 1:            # '1' is not a prime number
        return False

    for i in range(2, n):
        if n%i == 0:
            return False
    return True


if __name__ == '__main__':
    print('IDEA 1:')
    for i in range(1000):
        if is_prime1(i):
            print(i, end=' ')
    print('\n')

    print('IDEA 2:')
    for i in range(1000):
        if is_prime2(i):
            print(i, end=' ')
    print('\n')

    print('IDEA 3:')
    for i in range(1000):
        if is_prime3(i):
            print(i, end=' ')
    print('\n')


