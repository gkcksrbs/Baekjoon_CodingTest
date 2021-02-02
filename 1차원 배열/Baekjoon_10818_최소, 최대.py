# 1. 입력 받을 숫자의 개수를 입력 받는다. 입력 받을 정수의 개수 N이 1 <= N <= 1,000,000 만족하지 않을 경우 다시 입력 받도록
#     한다.
# 2. N개 만큼 정수의 개수를 입력 받는다. 입력 받은 정수의 개수와 N이 일치하지 않을 경우 다시 입력 받도록 한다. 또한 입력된 정수의
#    값이 -1,000,000 보다 작거나 1,000,000 보다 크면 다시 입력받도록 한다.
# 3. 입력 받은 정수들에서 최댓값과 최솟값을 출력한다.

bool = True

while(bool):
    print("Input number:")
    num = int(input())
    if(1 <= num <= 1000000):
        bool = False
    else:
        print("Error\n")
bool = True

while(bool):
    out_of_range = False
    print("Input Integer:")
    num_list = list(map(int, input().split()))

    for i in num_list:
        if(i<-1000000 or i>1000000):
            out_of_range = True

    if(num != len(num_list) or out_of_range):
        print("Error\n")

    else:
        bool = False
min, max = num_list[0], num_list[0]

for i in num_list:
    if i > max:
        max = i
    if i < min:
        min = i

print("min = ", min, "max = ", max)
