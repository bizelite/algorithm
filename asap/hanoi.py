def hanoi(n, start, waypoint, destination):
    if n == 0:
        return
    hanoi(n-1, start, destination, waypoint)
    print('{} move {} => {}'.format(n, start, destination))
    hanoi(n-1, waypoint, start, destination)

if __name__ == '__main__':
    hanoi(5, "A", "B", "C")