import sys

class Stack:
    def __init__(self, lst=[]):
        self.__stack_lst = lst

    def push(self, num):
        self.__stack_lst.append(num)

    def size(self):
        return len(self.__stack_lst)

    def pop(self):
        if self.size() == 0:
            return -1
        else:
            return self.__stack_lst.pop()

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.size() == 0:
            return -1
        else:
            return self.__stack_lst[self.size()-1]


stack = Stack()
N = int(sys.stdin.readline())

for i in range(N):
    lst = list(map(str, sys.stdin.readline().split()))

    if(lst[0] == 'push'):
        stack.push(int(lst[1]))

    elif(lst[0] == 'top'):
        print(stack.top())

    elif(lst[0] == 'size'):
        print(stack.size())

    elif(lst[0] == 'empty'):
        print(stack.empty())

    elif(lst[0] == 'pop'):
        print(stack.pop())
