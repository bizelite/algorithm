def avg(x, y, z):
    return (x+y+z)/3

if __name__ == '__main__':
    a, b, c = eval(input('Enter three number seperated by comma. '))
    print(avg(a, b, c))
    