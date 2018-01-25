def main():
    print('This program calculates the future value')
    print('of a n-year investment.')

    principal = eval(input('Enter the initial principal: '))
    apr = eval(input('Enter the annual interest rate: '))
    n = eval(input('Enter the period: '))

    for i in range(n):
        principal = principal * (1 + apr)

    print('The value in ', n, 'year is: ', principal)

if __name__ == '__main__':
    main()