# 1. 단어의 개수 N을 입력받는다(1 <= N <= 100).
# 2. 단어를 입력받는다.
# 3. 입력 받은 단어를 for문 돌려가면서 그룹 단어를 찾는다.

while(True):
    N = int(input())

    if(1 <= N <= 100):
        break

group_word = 0
for i in range(N):
    while(True):
        word = input()

        if(0 < len(word) <= 100):
            break

    for j in range(len(word)):
        if (j != len(word) - 1):
            if(word[j] == word[j + 1]):
                pass
            elif(word[j] in word[j+1:]):
                break
        else:
            group_word += 1

print(group_word)
