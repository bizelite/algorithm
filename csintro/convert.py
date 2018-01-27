def c2f(c):
    return 9/5*c + 32


def f2c(f):
    return 5/9*f - 160/9

def k2m(k):
    return 0.62 * k

if __name__ == '__main__':
    print('Convert temperature from celcius to farenheit')
    for i in range(101):
        if i%10 == 0:
            print(i, c2f(i))
    
    for i in range(212, 32, -1):
        if i%10 == 0:
            print(i, f2c(i))

    input('Press <Enter> to quit.')
