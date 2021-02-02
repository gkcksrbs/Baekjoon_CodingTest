# 1. 영어 대소문자와 띄어쓰기로만 이루어진 문자열을 입력 받는다. 이외의 다른 문자가 존재하면 다시 입력 받도록 한다.
# 2. 문자열의 길이가 1,000,000을 넘어도 다시 입력 받도록 한다.
# 3. 입력 받은 문자열을 띄어쓰기로 단어를 나누어 리스트로 저장하고 리스트의 길이를 출력한다.

STRING = 'QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm '

while(True):
    str = input()

    if (0 <= len(str) <= 1000000):
        check_length = True
    else:
        check_length = False

    check_char = True
    for i in str:
        if i not in STRING:
            check_char = False

    if(check_length and check_char):
        new_str = str.split()
        break

print(len(new_str))
