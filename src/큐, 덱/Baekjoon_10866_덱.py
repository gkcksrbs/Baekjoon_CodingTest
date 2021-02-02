import sys
from _collections import deque

class Deque():
    def __init__(self):
        self.deque = deque()

    def push_front(self, num):
        self.deque.appendleft(num)

    def push_back(self, num):
        self.deque.append(num)

    def pop_front(self):
        if self.size() == 0:
            return -1
        else:
            return self.deque.popleft()

    def pop_back(self):
        if self.size() == 0:
            return -1
        else:
            return self.deque.pop()

    def size(self):
        return self.deque.__len__()

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.size() == 0:
            return -1
        else:
            return self.deque[0]

    def back(self):
        if self.size() == 0:
            return -1
        else:
            return self.deque[-1]

    def print(self):
        print(self.deque)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    D = Deque()

    for i in range(N):
        lst = list(map(str, sys.stdin.readline().split()))

        if lst[0] == 'push_front':
            D.push_front(int(lst[1]))
        elif lst[0] == 'push_back':
            D.push_back(int(lst[1]))
        elif lst[0] == 'pop_front':
            print(D.pop_front())
        elif lst[0] == 'pop_back':
            print(D.pop_back())
        elif lst[0] == 'size':
            print(D.size())
        elif lst[0] == 'empty':
            print(D.empty())
        elif lst[0] == 'front':
            print(D.front())
        elif lst[0] == 'back':
            print(D.back())