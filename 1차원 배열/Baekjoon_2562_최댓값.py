# 1. 9개의 자연수를 받을 리스트를 만들고 100보다 작은 자연수를 입력 받아 저장한다.
# 2.입력 받은 9개의 자연수들 중에서 최댓값을 찾고 리스트에 최댓값이 몇 번째에 위치하였는지 찾아 출력한다.

num_list = [0 for i in range(9)]

for i in range(9):
    num_list[i] = int(input())

max_num = num_list[0]
max_loc = 0

for i in range(9):
    if(num_list[i] > max_num):
        max_num = num_list[i]
        max_loc = i

print(max_num)
print(max_loc + 1)