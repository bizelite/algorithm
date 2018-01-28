import math

# 1. The surface area and volume of sphere

def volume(r):
    return 4 / 3 * math.pi * r**3

def surface(r):
    return 4 * math.pi * r**2


# 2. The price of pizza per squqre inch

def circle(r):
    return math.pi * r**2

def price_per_square_inch(r, p):
    return price / circle(r)


# 3. Calculate molecular weight of carbohydrate 

def mwc():
    h = eval(input('Enter a number of hydrogen: '))
    c = eval(input('Enter a number of carbon: '))
    o = eval(input('Enter a number of oxygen: '))

    return c*12.0107 + h*2*1.00794 + o*15.9994


# 4. Calculate distance between litening moment and thunder

def s():
    l = eval(input('Enter a time of litening: '))
    t = eval(input('Enter a time of thunder: '))

    return 340 * (t-l)


# 5. Conditoray Coffee House

def expense():
    p = eval(input('Enter a number of coffee: '))
    return 10.5 * p + 1.5 + 0.86 * (p-1)


# 6. The slop of two-points on plane

def slope():
    x1 = eval(input('Enter a point of X1: '))
    x2 = eval(input('Enter a point of X2: '))
    y1 = eval(input('Enter a point of Y1: '))
    y2 = eval(input('Enter a point of Y2: '))

    return (y2 - y1) / (x2 - x1)


# 7. Distance of two-points on plane

def distance():
    x1 = eval(input('Enter a point of X1: '))
    x2 = eval(input('Enter a point of X2: '))
    y1 = eval(input('Enter a point of Y1: '))
    y2 = eval(input('Enter a point of Y2: '))

    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


# 8. Calculate the age of moon in the Gregorian calendar

def epact():
    year = eval(input('Enter a year(YYYY): '))
    C = year // 100
    return (8+C//4) - C + (((8*C+13)//25) + 11*(year%19))%30


# 9. Calculate the area of triangle

def triangle():
    a = eval(input('Enter a length of base line: '))
    b = eval(input('Enter a length of hypotenuse: '))
    c = eval(input('Enter a lenght of height: '))

    s = (a + b + c) / 2

    return math.sqrt(s * (s - a) * (s - b) * (s - c))


# 10. Calculate the length of ladder 

def lol():
    h = eval(input('Enter a height: '))
    a = eval(input('Enter a degrees of ladder: '))

    radians = math.pi / 180

    return h / math.sin(a)


# 11. Calcluate sum of n'numbers

def sum_n():
    n = eval(input('Enter a number: '))
    total = 0

    for i in range(1, n+1):
        total += i

    return total


# 12. Calcualte sum of n's cube

def cube():
    n = eval(input('Enter a number: '))
    total = 0

    for i in range(1, n+1):
        total += i**3

    return total


# 13. Calculate sum of input serial number

def total():
    n = eval(input('Enter a number: '))
    total = 0

    for i in range(n):
        num = eval(input('input: '))
        total += num

    return total


# 14. Calcualte average of input serial number

def avg():
    n = eval(input('Enter a number: '))
    total = 0
    
    for i in range(n):
        num = eval(input('input: '))
        total += num

    return total / n


# 15. Calcualte PI number 

def cal_pi():
    n = eval(input('Enter a n-th section: '))

    PI = 0

    for i in range(1, n+1):
        if i%2 != 0:
            PI += 4 / (2*i-1)
        else:
            PI -= 4 / (2*i-1)

    return PI


if __name__ == '__main__':
    pass
