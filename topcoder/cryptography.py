def crypto(lst):
    max_prod = 0

    for i in range(len(lst)):
        prod = 1
        for j in range(len(lst)):
            prod *= lst[j]
        if (prod * (lst[i]+1) / lst[i]) > max_prod:
            max_prod = prod * (lst[i]+1) / lst[i]

    return max_prod

if __name__ == '__main__':
    numbers = [1, 2, 3]
    print(crypto(numbers))

    numbers = [1, 3, 2, 1, 1, 3]
    print(crypto(numbers))

    numbers = [number for number in range(1000, 994, -1)]
    print(crypto(numbers))

    numbers = [1, 1, 1, 1]
    print(crypto(numbers))



