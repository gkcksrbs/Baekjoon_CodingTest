import sys

N = int(sys.stdin.readline())
Stack = []
lst = []
Answer = []
Num = [i+1 for i in range(N)]
Correct = True

for i in range(N):
    num = int(sys.stdin.readline())

    while Correct:

        if Stack.__len__() == 0:
            Stack.append(Num.pop(0))
            lst.append('+')

        if num not in Stack:
            Stack.append(Num.pop(0))
            lst.append('+')

        if num == Stack[-1]:
            Answer.append(Stack.pop())
            lst.append('-')
            break

        if num in Stack:

            if num != Stack[-1]:

                Correct = False
                break

if not Correct:

    print('NO')

else:

    for i in lst:

        print(i)