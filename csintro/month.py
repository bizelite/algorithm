def main():
    months = 'JanFeb,MarAprMayJunJulAutSepOctNovDec'

    n = int(input('Enter a month number (1-12): '))
    pos = (n-1) * 3

    month_abbrev = months[pos:pos+3]

    print('The month abbreviation is', month_abbrev + '.')


if __name__ == '__main__':
    main()
