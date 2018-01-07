def insertion_sort(lst):
    for i in range(1, len(lst)):
        cur_val = lst[i]
        pos = i

        while pos > 0 and lst[pos-1] > cur_val:
            lst[pos] = lst[pos-1]
            pos -= 1
        if pos != i:
            lst[pos] = cur_val

if __name__ == '__main__':
    lst = [8, 4, 7, 3, 5, 2, 9]
    insertion_sort(lst)



