class Queue:
    def __init__(self, MAX_QUEUE_SIZE, front, rear):
        self.array = [0 for i in range(10)]
        self.MAX_QUEUE_SIZE = MAX_QUEUE_SIZE
        self.front = front
        self.rear = rear

    def is_full(self):
        if self.rear >= self.MAX_QUEUE_SIZE:
            return True
        return False

    def is_empty(self):
        if self.front <= 0:
            return True
        return False

    def put(self, value):
        if self.is_full() == True:
            return False

        self.array[self.rear] = value
        self.rear += 1

    def get(self):
        if self.is_empty() == True:
            return False

        del self.array[self.front] 
        self.front += 1

    def print_queue():
        print(self.array)


if __name__ == '__main__':
    q = Queue(10, 0, 0)

    for i in range(10):
        q.put(i)

    q.get()
    q.get()
 
    
    print(q.array)





