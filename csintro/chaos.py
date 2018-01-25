def main():
    print('This program illustrates a chaotic function')
    n = eval(input('Howw many numbers shuid I print? '))
    x = eval(input('Enter a number between 0 and 1: '))
    y = x
    z = x

    print('Case a)      Case b)     Case c)')
    print('-------      -------     -------')
    for i in range(n):
        x = 3.9 * x * (1 - x)
        y = 3.9 * (y - y * y)
        z = 3.9 * z - 3.9 * z * z 
        print("{0:>7f}     {1:>7f}     {2:>7f}".format(x, y, z))

if __name__ == '__main__':
    main()

