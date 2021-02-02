# 1. 테스트 케이스의 개수를 입력 받는다. 자연수가 아닐 경우 다시 입력 받도록 한다.
# 2. 각 테스트 케이스를 입력 받는다. 0 < 길이 < 80 을 만족하지 않을 경우 다시 입력 받도록 한다.
# 3. O, X가 아닌 다른 문자를 사용해도 다시 입력 받도록 한다.
# 4. 리스트를 하나 만들고 리스트 안에 각 테스트 케이스에 대한 리스트를 만든다.
# 5. 테스트 케이스에 대한 리스트 첫 번째 칸에서 O이면 1, X이면 0을 저장한다.
# 6. O이면 이전의 칸의 값에 +1의 값을, X이면 0의 값을 저장한다.
# 7. 테스트 케이스에 대한 리스트에 총합을 구하여 출력한다.

#테스트의 개수 입력 받기
while(True):
    num = int(input())
    if(0 < num):
        break

lst = []

# 각 테스트 케이스 입력 받기
for i in range(num):
    while(True):
        str = input()
        tmp = sorted(set(str)) #문자열 중복 제거 후 정렬

        if (len(tmp) == 1):
            if(tmp[0] == 'O' or tmp[0] == 'X'):
                check = True
            else:
                check = False

        elif(len(tmp) == 2):
            if(tmp[0] == 'O' and tmp[1] == 'X'):
                check = True
            else:
                check = False

        else:
            check = False

        if(0 < len(str) < 80 and check):
            lst.append(str)
            break

new_lst = []

# 점수 넣기
for i in lst:
    score_lst =[0 for j in range(len(i))]

    for k in range(len(i)):
        if(k==0):
            if(i[k] == 'O'):
                score_lst[k] = 1
        else:
            if(i[k] == 'O'):
                score_lst[k] = score_lst[k-1] + 1
    new_lst.append(score_lst)

# 점수 총합 출력하기
for i in new_lst:
    print(sum(i, 0))


