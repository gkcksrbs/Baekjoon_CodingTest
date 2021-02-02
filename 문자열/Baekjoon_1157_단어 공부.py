# 1. 알파벳 대소문자로 된 문자열을 입력 받는다. 알파벳이 아닌 다른 문자가 입력되면 다시 입력 받도록 한다.
# 2.  문자열의 길이가 0이상 1,000,000을 만족하지 않을 경우에도 다시 입력 받도록 한다.
# 3. 아스키코드를 활용하여 입력 받은 문자열 중 소문자로 된 문자열을 대문자로 바꾼다.
# 4. 입력 받은 문자열을 알파벳 순서대로 하나씩 몇번 반복되었는지 세고 값을 저장한다.
# 5. 가장 많이 반복된 문자를 출력하고 가장 많이 반복된 문자가 2개 이상일 경우 '?'을 출력한다.

# A ~ Z = 65 ~ 90
# a ~ z = 97 ~ 122

ALPHABET = 'QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm'
SORTED_ALPHABET = sorted(ALPHABET)

while(True):
    str = input()

    if(0 <= len(str) <= 1000000):
        check_len = True
    else:
        check_len = False

    check_alphabet = True

    for i in range(len(str)):
        if str[i] not in SORTED_ALPHABET:
            check_alphabet = False

    if(check_len and check_alphabet):
        break

new_str =""
for i in str:
    if (97 <= ord(i) <= 122):
        new_str = new_str + chr(ord(i) - 32)
    else:
        new_str = new_str + i

sorted_str = list(set(sorted(new_str)))
lst = []

for i in range(len(sorted_str)):
    tmp = []
    times = 0
    for j in range(len(new_str)):
        if (sorted_str[i] == new_str[j]):
            times += 1
    tmp.append(times)
    tmp.append(sorted_str[i])
    lst.append(tmp)

lst = sorted(lst)

max = len(lst) - 1
if(max != 0 ):
    if (lst[max][0] == lst[max - 1][0]):
        print('?')
    else:
        print(lst[max][1])

else:
    print(lst[max][1])

