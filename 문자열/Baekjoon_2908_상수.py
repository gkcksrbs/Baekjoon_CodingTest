# 1. 한 줄로 두 개의 세자리 수를 입력 받는다. 두 개의 숫자가 같거나 0이 존재하면 다시 입력 받는다.
# 2. 두 수를 나누어서 리스트에 저장하고 수를 역순으로 바꾼다.
# 3. 숫자를 비교하여 더 큰 수를 출력한다.

NUMBER = '123456789 '

while(True):
    num = str(input())

    if(len(num) == 7):
        check_len = True
    else:
        check_len = False
        continue

    check_num = True
    for i in num:
        if i not in NUMBER:
            check_num = False

    two_num = list(num.split())

    is_different = True
    if(int(two_num[0]) == int(two_num[1])):
        is_different = False

    if(check_num and check_len and is_different):
        break

new_two_num = []
for i in two_num:
    new_two_num.append(int(i[::-1]))

print(max(new_two_num))