def selection_sort(l):
    for i in range(len(l)-1):
        min_idx = i
        for j in range(i+1, len(l)):
            if l[min_idx] > l[j]:
                min_idx = j
        l[i], l[min_idx] = l[min_idx], l[i]
    return l


def insert_sort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] > key:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key


def merge_sort(l):
    n = len(l)
    if n <= 1:
        return

    mid = n // 2
    g1 = l[:mid]
    g2 = l[mid:]

    merge_sort(g1)
    merge_sort(g2)

    i1 = 0
    i2 = 0
    il = 0

    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            l[il] = g1[i1]
            i1 += 1
            il += 1
        else:
            l[il] = g2[i2]
            i2 += 1
            il += 1
    
    while i1 < len(g1):
        l[il] = g1[i1]
        i1 += 1
        il += 1

    while i2 < len(g2):
        l[il] = g2[i2]
        i2 += 1
        il += 1


def quick_sort_sub(l, start, end):
    if end - start <= 0:
        return

    pivot = l[end]
    i = start

    for j in range(start, end):
        if l[j] <= pivot:
            l[i], l[j] = l[j], l[i]
            i += 1
    l[i], l[end] = l[end], l[i]

    quick_sort_sub(l, start, i-1)
    quick_sort_sub(l, i+1, end)


def quick_sort(l):
    quick_sort_sub(l, 0, len(l)-1)



if __name__ == '__main__':
    v = [17, 92, 18, 33, 58, 7, 18, 33, 42]

    print('Selection Sort:', selection_sort(v))
    insert_sort(v)
    print('Insert Sort:', v)
    merge_sort(v)
    print('Merge Sort:', v)
    quick_sort(v)
    print('Quick Sort:', v)

