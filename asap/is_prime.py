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
    count1 = 0
    for i in range(1000):
        if is_prime1(i):
            count1 += 1
            print(i, end=' ')
    print('\nCount = {}\n'.format(count1))

    print('IDEA 2:')
    count2 = 0
    for i in range(1000):
        if is_prime2(i):
            count2 += 1
            print(i, end=' ')
    print('\nCount = {}\n'.format(count2))
    
    print('IDEA 3:')
    count3 = 0
    for i in range(1000):
        if is_prime3(i):
            count3 += 1
            print(i, end=' ')
    print('\nCount = {}\n'.format(count3))


