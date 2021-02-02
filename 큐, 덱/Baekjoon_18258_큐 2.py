import sys
from _collections import deque
class Queue:

    def __init__(self):
        self.list = deque()

    def push(self, num):
        self.list.append(num)

    def pop(self):
        if self.list.__len__() == 0:
            return -1

        else:
            return self.list.popleft()

    def size(self):
        return self.list.__len__()

    def empty(self):
        if self.list.__len__() == 0:
            return 1

        else:
            return 0

    def front(self):
        if self.list.__len__() == 0:
            return -1

        else:
            return self.list[0]

    def back(self):
        if self.list.__len__() == 0:
            return -1

        else:
            return self.list[-1]

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    Q = Queue()

    for i in range(N):
        lst = list(map(str, sys.stdin.readline().split()))

        if lst[0] == 'push':
            Q.push(int(lst[1]))

        elif lst[0] == 'pop':
            print(Q.pop())

        elif lst[0] == 'size':
            print(Q.size())

        elif lst[0] == 'empty':
            print(Q.empty())

        elif lst[0] == 'front':
            print(Q.front())

        elif lst[0] == 'back':
            print(Q.back())
