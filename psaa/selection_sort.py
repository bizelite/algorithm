# Data Sort Algorithm : Selection Sort

def selection_sort(lst):
    for i in range(len(lst)-1):
        min_pos = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_pos]:
                min_pos = j

        if min_pos != i:
            tmp = lst[i]
            lst[i] = lst[min_pos]
            lst[min_pos] = tmp


if __name__ == '__main__':
    lst = [8, 4, 7, 3, 5, 2, 9]
    selection_sort(lst)
    print(lst)
