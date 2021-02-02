# 1. 1000보다 작은 음이 아닌 정수 10개를 입력 받는다.
# 2. 입력된 값이 1000보다 작은 음이 아닌 정수가 아닐 경우 다시 입력 받도록 한다.
# 3. list 하나를 만들고 입력 받은 수에 42로 나눈 나머지 값을 리스트에 저장한다.
# 4. list를 set 집합으로 바꾸어서 중복된 값을 제거한다.
# 5. set의 길이를 출력한다.

list = []

for i in range(10):
    while(True):
        num = int(input())
        if (0<= num < 1000):
            break
    list.append(num % 42)

new_list = set(list)

print(len(new_list))


