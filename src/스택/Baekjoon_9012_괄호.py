import sys

N = int(sys.stdin.readline())
lst = []

for i in range(N):
    Str = list(sys.stdin.readline().rstrip())
    lst.append(Str)

for i in range(len(lst)):
    Stack =[]
    while(lst[i].__len__() != 0):
        pop = lst[i].pop()

        if pop == ')':
            Stack.append(pop)
        elif pop == '(':
            if Stack.__len__() == 0:
                if(lst[i].__len__() == 0):
                    lst[i].append(pop)
                break
            else:
                Stack.pop()

    if len(lst[i]) == 0 and len(Stack) == 0:
        print('YES')
    else:
        print('NO')
