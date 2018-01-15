def selection_sort(l):
    for i in range(len(l)-1):
        min_idx = i
        for j in range(i+1, len(l)):
            if l[min_idx] > l[j]:
                min_idx = j
        l[i], l[min_idx] = l[min_idx], l[i]
    return l


if __name__ == '__main__':
    v = [17, 92, 18, 33, 58, 7, 18, 33, 42]

    print(selection_sort(v))