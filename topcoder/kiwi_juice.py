def pour(from_id, to_id):
    for i in range(len(from_id)):
        limit = capa[to_id[i]] - bottle[to_id[i]]
        if bottle[from_id[i]] < limit:
            bottle[to_id[i]] += bottle[from_id[i]]
            bottle[from_id[i]] -= bottle[from_id[i]]
        else:
            bottle[to_id[i]] += limit
            bottle[from_id[i]] -= limit

    return bottle




if __name__ == '__main__':
    capa = [14, 35, 86, 58, 25, 62]
    bottle = [6, 34, 27, 38, 9, 60]
    from_id = [1, 2, 4, 5, 3, 3, 1, 0]
    to_id = [0, 1, 2, 4, 2, 5, 3, 1]

    print(pour(from_id, to_id))   # Return: [0, 14, 65, 35, 23, 35]


    capa = [700000, 800000, 900000, 1000000]
    bottle = [478478, 478478, 478478, 478478]
    from_id1 = [2, 3, 2, 0, 1]
    to_id1 = [0, 1, 1, 3, 2]

    print(pour(from_id1, to_id1))   # Return: [0, 156956, 900000, 856956]


