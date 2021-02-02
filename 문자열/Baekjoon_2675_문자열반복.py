# 1. 테스트 케이스의 수를 입력받는다. 1 <= T <= 1000을 만족하지 않을경우 다시 입력 받도록 한다.
# 2.반복 횟수 R을 입력 받고 문자열 S를 입력 받는다.
# 3. 1 <= R <= 8, 0<= S <= 20을 만족하지 않을 경우 다시 입력 받도록 한다.
# 4. QR Code "alphanumeric" 문자열을 하나 생성하고 S에 QR Code "alphanumeric" 문자만 있는지 확인한다.
# 5. 다른 문자가 존재할 경우 다시 입력 받는다.
# 6.입력된 문자열을 반복수만큼 반복하여 출력한다.

QRCODE = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:"

while(True):
    T = int(input())
    if(1 <= T <= 1000):
        break

R = []
S = []

for i in range(T):
    while (True):
        tmp = list(map(str, input().split()))

        if (1 <= int(tmp[0]) <= 8):
            check_recur = True
        else:
            check_recur = False

        if (0 <= len(tmp[1]) <= 20):
            check_str = True
        else:
            check_str = False

        check_QRCODE = True
        for i in tmp[1]:
            if i not in QRCODE:
                check_QRCODE = False


        if (check_str and check_recur and check_QRCODE):
            R.append(tmp.pop(0))
            S.append(tmp[0])
            break

for i in range(T):
    tmp = ""
    for j in range(len(S[i])):
        for k in range(int(R[i])):
            tmp = tmp + S[i][j]
    print(tmp)



