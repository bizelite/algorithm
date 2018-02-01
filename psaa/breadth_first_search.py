def bfs(graph, root, search):
    visited = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            if node == search:
                break
            queue.extend([x for x in graph[node] if x not in visited])

    return visited


if __name__ == '__main__':
    graph = {1: [2, 7, 8],
             2: [1, 3, 6],
             3: [2, 4, 5],
             4: [3],
             5: [3],
             6: [2],
             7: [1],
             8: [1, 9, 12],
             9: [8, 10, 12],
             11: [9],
             12: [8]}

    print(list(bfs(graph, 1, 9)))
