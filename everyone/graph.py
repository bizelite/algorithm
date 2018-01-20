def search_graph(dic):
    for item in lst:
        if item not in dic.keys():
            dic[item] = []
    return dic


def print_all_friends(dic, start):
    qu = []
    done = set()

    qu.append((start, 0))
    done.add(start)

    while qu:
        p, d = qu.pop(0)
        print(p, d)

        for x in dic[p]:
            if x not in done:
                qu.append((x, d+1))
                done.add(x)


def bfs(dic, start):
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        print(p)
        for x in dic[p]:
            if x not in done:
                qu.append(x)
                done.add(x)



if __name__ == '__main__':
    names = ['Summer', 'John', 'Justin', 'Mile', 'May', 'Kim', 'Tom', 'Jerry']
    fr_info = {'Summer': ['John', 'Justin', 'Mike'],
               'John': ['Summer', 'Justin'],
               'Justin': ['John', 'Summer', 'Mike', 'May'],
               'Mike': ['Summer', 'Justin'],
               'May': ['Justin', 'Kim'],
               'Kim': ['May'],
               'Tom': ['Jerry'],
               'Jerry': ['Tom']}

    numbers = {1: [2, 3],
               2: [1, 4, 5],
               3: [1],
               4: [2],
               5: [2]}

    print_all_friends(fr_info, 'Summer')
    print()
    print_all_friends(fr_info, 'Jerry')
    print()
    bfs(numbers, 1)

