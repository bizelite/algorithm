MAX_SIZE = 5

def print_star():
    for column in range(MAX_SIZE):
        for row in range(MAX_SIZE):
            if (column+row)%2 == 0:
                print('*', end=' ')
            else:
                print('', end=' ')
        print('')

if __name__ == '__main__':
    print_star()
