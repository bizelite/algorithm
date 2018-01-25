def c2f(c):
    return 9/5*c + 32


if __name__ == '__main__':
    print('Convert temperature from celcius to farenheit')
    for i in range(101):
        if i%10 == 0:
            print(i, c2f(i))
    input('Press the <Enter> key to quit.')
