import math

def is_prime(n):
    count = 1
    i = 2
    while i <= math.sqrt(n):
        if n%i == 0:
            count += 1
        if count > 2:
            return False
        i += 1
    return True

if __name__ == '__main__':
    print(is_prime(4))

