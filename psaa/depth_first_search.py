def dfs(graph, root, search):
    visited = []
    stack = [root, ]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node == search:
                break
            stack.extend([x for x in graph[node] if x not in visited])
    return visited



if __name__ == '__main__':
    graph = {1: [8, 7, 2],
             2: [1, 6, 3],
             3: [2, 5, 4],
             4: [3],
             5: [3],
             6: [2],
             7: [1],
             8: [1, 12, 9],
             9: [8, 11, 10],
             10: [9],
             11: [9],
             12: [8]}
    print(dfs(graph, 1, 9))

