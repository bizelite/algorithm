MAX_SIZE = 5

def print_star():
    for row in range(MAX_SIZE):
        for column in range(MAX_SIZE):
            if (row+column)%2 == 0:
                print('*', end=' ')
            else:
                print('', end=' ')
        print('')

def print_numbers():
    number = 1
    matrix = [[0 for col in range(MAX_SIZE)] for row in range(MAX_SIZE)]

    for i in range(MAX_SIZE):
        if i%2 == 0:
            for j in range(MAX_SIZE):
                matrix[i][j] = number
                number += 1
        else:
            for j in range(MAX_SIZE-1, -1, -1):
                matrix[i][j] = number
                number += 1

    for i in range(MAX_SIZE):
        for j in range(MAX_SIZE):
            print('{:>2d}'.format(matrix[i][j]), end=' ')
        print('')



if __name__ == '__main__':
    print_star()
    print('\n')
    print_numbers()
