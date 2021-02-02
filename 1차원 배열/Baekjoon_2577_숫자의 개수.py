# 1. 3개의 숫자를 입력 받는다. 입력 받은 숫자가 100보다 작거나 1000보다 크면 다시 입력 받도록 한다.
# 2. 3개의 숫자를 곱한 값을 구하고 구한 값을 문자열로 저장한다.
# 3. 사이즈가 10인 리스트를 하나 만들고 0으로 초기화한다.
# 4. 곱해진 값의 0부터 9까지 쓰여진 개수를 사이즈가 10인 리스트에 개수를 저장한다.

while(True):
    A = int(input())
    if(100<= A <= 1000):
        break
    print("Error")

while(True):
    B = int(input())
    if(100<= B <= 1000):
        break
    print("Error")

while(True):
    C = int(input())
    if(100<= C <= 1000):
        break
    print("Error")

Val = str(A*B*C)
List = [0 for i in range(10)]

for i in Val:
    List[int(i)] = List[int(i)] + 1

for i in List:
    print(i)
