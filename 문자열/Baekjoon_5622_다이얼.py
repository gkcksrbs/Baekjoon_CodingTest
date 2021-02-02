hash_table = {'A': 3, 'B': 3, 'C': 3, 'D': 4, 'E': 4, 'F': 4, 'G': 5, 'H': 5, 'I': 5, 'J': 6, 'K': 6, 'L': 6,
              'M': 7, 'N': 7, 'O':7, 'P':8, 'Q': 8, 'R': 8, 'S': 8, 'T': 9, 'U': 9, 'V': 9, 'W': 10, 'X': 10, 'Y': 10,
              'Z': 10}

ALPHABET = 'QWERTYUIOPLKJHGFDSAZXCVBNM'

while(True):
    input_str = input()

    check_str = True
    for i in input_str:
        if i not in ALPHABET:
            check_str = False

    if (2 <= len(input_str) <= 15):
        check_len = True
    else:
        check_len = False

    if(check_len and check_str):
        break

lst = list(input_str)
time = 0

for i in lst:
    time = time + hash_table[i]

print(time)