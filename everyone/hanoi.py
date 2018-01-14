# Hanoi's Tower Algorithm
# Input:
#    n : Number of disk         
#    from_pos : Tower of starting point
#    to_pos : Tower of ending point
#    aux_pos : Tower of middle point
# Output: 
#    Sequences of disk movement

def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos, '->', to_pos)
        return

    hanoi(n-1, from_pos, aux_pos, to_pos)
    print(from_pos, '->', to_pos)
    hanoi(n-1, aux_pos, to_pos, from_pos)


if __name__ == '__main__':
    hanoi(3, 1, 3, 2)
