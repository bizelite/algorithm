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



def same_name(lst):
    dup = set()
    dic = {}

    for item in lst:
        dic[item] = dic.get(item, 0) + 1
        if dic[item] > 1:
            dup.add(item)
    return dup



if __name__ == '__main__':
    names = ['Tom', 'Jerry', 'Mike', 'Tom']
    names1 = ['Tom', 'Jerry', 'Mike', 'Tom', 'Mike']
    # print(duplicate(names))
    # print(pairs(names))


    same_name = same_name(names)
    same_name1 = same_name1(names)
    print(same_name)


