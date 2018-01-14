def duplicate(l):
    dup = set()
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if l[i] == l[j]:
                dup.add(l[j])
    return dup


def pairs(l):
    l = list(set(l))
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if l[i] != l[j]:
                print(l[i], '-', l[j])


if __name__ == '__main__':
    names = ['Tom', 'Jerry', 'Mike', 'Tom']
    print(duplicate(names))
    print(pairs(names))


