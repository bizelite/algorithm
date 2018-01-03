def insert_number(lst, index, value):
    if index > len(lst)-1:
        print('index out of range')
        return None

    for i in range(len(lst), index-1, -1):
        if i == len(lst):
            lst += [lst[len(lst)-1]]
        else:
            lst[i] = lst[i-1]

    lst[index] = value

    return lst



def delete_number(lst, index):
    if index > len(lst)-1:
        print('index out of range')
        return None

    for i in range(index, len(lst)-1):
        lst[i] = lst[i+1]

    return lst


def find_number(lst, value):
    for i in range(len(lst)-1):
        if lst[i] == value:
            return i
    return None

if __name__ == '__main__':
    num_list = [1, 3, 7, 9, 11, 13]
    print(insert_number(num_list, 3, 'a'))
    print(delete_number(num_list, 1))
    print(find_number(num_list, 'a'))


