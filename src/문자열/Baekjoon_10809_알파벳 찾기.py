# 1. 단어의 길이가 100을 넘지 않고 알파벳 소문자로만 이루어진 문자열을 입력받는다.
# 2. 1번을 만족하지 않을 경우 다시 입력 받도록 한다.
# 3. 길이가 26인 리스트를 하나 만들고 모든 원소에 -1로 초기화한다.
# 4. 'a'의 아스키코드 값은 97이므로 문자열을 처음부터 가면서 리스트 (한 문자의 아스키코드 값 - 97)번째에 문자열의 위치를 저장한다.
# 5. 해당하는 리스트 번째에 -1값이 아닌 다른 수가 저장되어 있다면 그냥 넘어간다.
# 6. 각각의 알파벳에 대해서 처음 등장하는 위치를 출력한다.

# 문자열 입력
while(True):
    str = input()

    if(0 < len(str) <= 100): # 문자열 길이 확인
        check_length = True
    else:
        check_length = False

    check_char = True # 문자열에서 소문자 외의 다른 문자가 있는지 확인
    for i in str:
        if (ord(i) < 97 or ord(i) > 122):
            check_char = False

    if(check_length and check_char): # 둘다 만족하면 while문 탈출
        break

char_loc = [-1 for i in range(26)]

for i in range(len(str)):
    ascii = ord(str[i])
    if(char_loc[ascii - 97] == -1 ):
        char_loc[ascii - 97] = i

output = ""

for i in char_loc:
    output = output + repr(i) + " " # repr(int) <- 숫자를 문자로 변환

print(output)
