# 1. 숫자의 개수를 입력받는다. 1 <= N <= 100 을 만족하지 않을 경우 다시 입력 받도록 한다.
# 2. 숫자 N개를 공백없이 입력 받는다.
# 3. 입력된 숫자 N개의 합을 구하고 값을 출력한다.

while(True):
    num = int(input())

    if(1 <= num <= 100):
        break

while(True):
    str = input()

    if(len(str) == num):
        break

sum = 0
for i in str:
    sum += int(i)

print(sum)
