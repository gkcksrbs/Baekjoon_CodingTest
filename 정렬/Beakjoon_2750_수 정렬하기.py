# 입력 받을 숫자의 개수를 입력 받고 개수 만큼 숫자를 입력 받는다.
# 리스트로 저장하고 sorted()로 정렬 후 출력한다.

while(True):
    N = int(input())

    if(1 <= N <= 1000):
        break

lst = []
for i in range(N):
    while(True):
        Num = int(input())

        if(-1000 <= Num <= 1000):
            check_num = True
        else:
            check_num = False

        check_ovlap = True
        if(len(lst) != 0):
            for j in lst:
                if j in lst:
                    check_ovlap: False

        if (check_ovlap and check_num):
            lst.append(Num)
            break

new_lst = sorted(lst)

for i in new_lst:
    print(i)