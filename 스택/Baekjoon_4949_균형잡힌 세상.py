import sys

while(True):
    Str = sys.stdin.readline().rstrip()
    Stack =[]
    Answer = True

    if Str == '.':
        break

    for i in Str:
        if i =='(' or i == '[':
            Stack.append(i)

        elif i == ')':
            if Stack.__len__() == 0:
                Answer = False
                break

            elif Stack[-1] == '(':
                Stack.pop()

            else:
                Answer = False
                break

        elif i == ']':
            if Stack.__len__() == 0:
                Answer = False
                break

            elif Stack[-1] == '[':
                Stack.pop()

            else:
                Answer = False
                break

    if Answer and Stack.__len__() == 0:
        print('yes')
    else:
        print('no')



