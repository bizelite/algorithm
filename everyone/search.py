# Sequential Search
def sequential(l, s):
    for i in range(len(l)):
        if l[i] == s:
            return i
    return -1


def search_all(l, s):
    ret = []
    for i in range(len(l)):
        if l[i] == s:
            ret.append(i)
    return ret


def map_search(l1, l2):
    number = int(input('Enter a student number: '))
    for i in range(len(l1)):
        if l1[i] == number:
            return l2[i]
    return '?'


if __name__ == '__main__':
    v = [17, 92, 18, 33, 58, 7, 18, 33, 42]
    stu_no = [39, 14, 67, 105]
    stu_name = ['Justin', 'John', 'Mike', 'Summer']

    
    print(search_all(v, 18))
    print(search_all(v, 33))
    print(search_all(v, 900))

    print(map_search(stu_no, stu_name))


