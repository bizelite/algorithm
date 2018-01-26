def annuity(principal, rate, period, beginning=True):
    total = 0
    if beginning == True:
        for i in range(1, period+1):
            total = total + principal * (1 + rate)**i
    else:
        for i in range(1, period):
            total = total + principal * (1 + rate)**i

    return total



def main():
    print('This program calculates the future value')
    print('of a n-year investment.')

    principal = eval(input('Enter the initial principal: '))
    apr = eval(input('Enter the annual interest rate: '))
    periods = eval(input('Enter the periods per year: '))
    n = eval(input('Enter the period: '))

    for i in range(n*periods):
        principal = principal * (1 + apr/periods)

    print('The value in ', n, 'year is: ', principal)

if __name__ == '__main__':
    main()