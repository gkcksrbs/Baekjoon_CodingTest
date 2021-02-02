# 1. 알파벳 소문자와 '-', '='로 이루어진 길이가 100이하의 문자열을 입력 받는다.
# 2. 문자열에서 크로아티아 문자열 리스트에 존재하는 문자열들을 '1'로 바꾸고 길이를 출력한다.

new_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alphabet = 'qwertyuioplkjhgfdsazxcvbnm-='

while(True):
    input_str = input()

    if(0 < len(input_str) <= 100):
        check_len = True
    else:
        check_len = False

    check_alpha = True
    for i in input_str:
        if i not in alphabet:
            check_alpha = False

    if (check_alpha and check_len):
        break

for i in new_alphabet:
    input_str = input_str.replace(i, '1')

print(len(input_str))