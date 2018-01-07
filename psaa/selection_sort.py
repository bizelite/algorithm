# Data Sort Algorithm : Selection Sort

def selection_sort(lst):
    for i in range(len(lst)-1):
        min_position = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_position]:
                min_position = j

        if min_position != i:
            tmp = lst[i]
            lst[i] = lst[min_position]
            lst[min_position] = tmp

if __name__ == '__main__':
    lst = [8, 4, 7, 3, 5, 2, 9]
    selection_sort(lst)
    