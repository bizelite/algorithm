# data sort algorithm : Merge Sort
# Recursion

def merge_sort(alist):
    print('Splitting ', alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i, j, k = 0, 0, 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
    print('Merging ', alist)


if __name__ == '__main__':
    alist = [8, 4, 7, 3, 5, 2, 9]
    merge_sort(alist)
    print('The result of merge sort: ', alist)
