# 1. 시험 본 과목의 개수를 입력 받는다. 과목의 개수가 1000보다 크거나 0보다 작거나 같으면 다시 입력 받도록 한다.
# 2. 시험 본 과목의 개수만큼 점수를 입력받는다. 점수가 100보다 크거나 0보다 작으면 다시 입력 받도록 한다.
# 3. 모든 과목의 점수가 0점이면 다시 입력 받도록 한다.
# 4. 입력 받은 점수 중에서 최댓값을 고르고 모든 점수를 (점수 / 최댓값 * 100)으로 모든 과목의 점수를 바꾸어 새로운 리스트에 저장한다.
# 5. 새로운 점수의 평균을 구하고 평균값을 출력한다.

# 과목의 개수 입력 받기
while(True):
    num = int(input())
    if(0 < num <= 1000):
        break

# 점수 입력 받기
while(True):
    lst = list(map(int, input().split()))
    tmp = list(set(lst))

    if( (len(tmp) == 1) and (tmp[0] == 0) ):
        all_zero = True
    else:
        all_zero = False

    if( (num == len(lst)) and (not all_zero) ):
        break
        
#
new_lst = [0.0 for i in range(num)]
max_score = max(lst)

#새로운 점수 구하기
for i in range(num):
    new_lst[i] = lst[i] / max_score * 100

#평균 구하기
avg = sum(new_lst, 0.0) / num

#평균 출력하기
print(avg)
