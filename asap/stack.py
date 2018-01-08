
class Stack:

    def __init__(self, MAX_STACK_SIZE, top=0):
        self.array = [0 for i in range(MAX_STACK_SIZE)]
        self.MAX_STACK_SIZE = MAX_STACK_SIZE
        self.top = top

    def is_full(self):
        if self.top >= self.MAX_STACK_SIZE:
            return True
        return False

    def is_empty(self):
        if self.top == 0:
            return True
        return False

    def push(self, value):
        if self.is_full() == True:
            return False

        self.array[self.top] = value
        self.top += 1

    def pop(self):
        if self.is_empty() == True:
            return False
        self.array[self.top-1] = 0
        self.top -= 1

    def get_data_count(self):
        self.count = 0

        for i in range(len(self.array)):
            self.count += 1

        return self.count

    def print_stack(self):
        print(self.array)

if __name__ == '__main__':
    s = Stack(10)

    s.push(19)
    s.push(28)
    s.push(74)
    s.push(10)

    s.push(19)
    s.push(28)
    s.push(74)
    s.push(10)

    s.push(19)
    s.push(28)
    s.pop()
    s.pop()


    s.print_stack()






