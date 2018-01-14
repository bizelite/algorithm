def max_n(l):
    max_num = l[0]
    for i in range(1, len(l)):
        if max_num < l[i]:
            max_num = l[i]

    return max_num


def min_n(l):
    min_num = l[0]
    for i in range(1, len(l)):
        if l[i] < min_num:
            min_num = l[i]

    return min_num


def min_index(l):
    min_idx = 0
    for i in range(1, len(l)):
        if l[i] < l[min_idx]:
            min_idx = i

    return min_idx



def max_index(l):
    max_index = 0
    for i in range(1, len(l)):
        if l[max_index] < l[i]:
            max_index = i

    return max_index


def input_number():
    n = None
    l = []
    while n != 0:
        n = int(input('Enter a number: '))
        l.append(n)
    l.pop()

    return l






if __name__ == '__main__':
    l = input_number()
    print('List is', l)
    print('Max Number:', max_n(l))
    print('Max Index:', max_index(l))
    print('Min Number:', min_n(l))
    print('Min Index:', min_index(l))

