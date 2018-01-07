# data sort algorithm : Merge Sort
# Iterative

def i_merge_sort(lst):
    lists = [[x] for x in lst]
    while len(lists) > 1:
        lists = merge_lists(lists)
    return lists[0]

def merge_lists(lists):
    result = []
    for i in range(0, len(lists) // 2):
        result.append(merge2(lists[i*2], lists[i*2 + 1]))
    if len(lists) % 2:
        result.append(lists[-1])
    return result

def merge2(xs, ys):
    i, j = 0, 0
    result = []
    while i < len(xs) and j < len(ys):
        x, y = xs[i], ys[j]
        if x > y:
            result.append(y)
            j += 1
        else:
            result.append(x)
            i += 1
    result.extend(xs[i:])
    result.extend(ys[j:])
    return result


if __name__ == '__main__':
    lst = [8, 4, 7, 3, 5, 2, 9]
    slst = i_merge_sort(lst)
    print('The result of Iterative Merge Sort: ', slst)
    