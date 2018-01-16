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



if __name__ == '__main__':
    v = [17, 92, 18, 33, 58, 7, 18, 33, 42]

    print('Selection Sort:', selection_sort(v))
    insert_sort(v)
    print('Insert Sort:', v)