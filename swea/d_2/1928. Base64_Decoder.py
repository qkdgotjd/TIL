# 24비트 버퍼? 무슨 뜻일까?
# 처음으로 문제 이해가 되지 않았다.

t = int(input())
for i in range(1, t+1):
    _str = input()
    len_str = len(_str)
    bin_num = ''
    result = ''
    solve =''
    for j in range(0, len_str//4):
        dec_str = _str[4*j: 4*j+4]
        for k in dec_str:
            if k.isalpha() and 65 <= ord(k) <= 90:
                num = ord(k) - 65
            elif k.isalpha() and 97 <= ord(k) <= 122:
                num = ord(k) - 71
            elif k.isdigit() and 0 <= int(k) <= 9:
                num = int(k) + 52
            elif k == '+':
                num = 62
            elif k == '/':
                num = 63
            temp_bin = bin(num)[2:]
            while len(temp_bin) < 6:
                temp_bin = '0' + temp_bin
                result += temp_bin
    
    for l in range(0, len(result)//8):
        solve += chr(int(result[8*l: 8*l+8], 2))
    print(solve)

# 어떻게든 내가 가진 지식으로 풀고자 노력한 흔적... 도저히 안 돼...
# 이런 base64 문제를 풀 때 활용할 수 있는 내장함수를 찾고 활용했다.
'''

#result += chr(int('0b' + bin_num[8*l: 8*l+8]))

import base64
t = int(input())

for i in range(1, t + 1):

    string = input()
    string_byte = string.encode('ASCII').
    # encode() 바이트 열로 나온다.
    decoded_string = base64.b64decode(string_byte)
    message = decoded_string.decode('ASCII')
    result = f'#{i} {message}'
    print(result)
        
            
# encoding 은 암호화, decoding 은 해석

        for k in range(0, 4):
            if dec_str[k].isnumeric():
                num_str = bin(int(dec_str[k]) + 52)
                bin_num += str(num_str)[2:]
            elif dec_str[k].islower():
                num_str = bin(ord(dec_str[k]) - 71)
                bin_num += str(num_str)[2:] 
            else:
                num_str = bin(ord(dec_str[k]) - 65)
                bin_num += str(num_str)[2:]
    print(bin_num)
    for l in range(0, len(bin_num)//8):
        result += chr(int(bin_num[l: 8*l+8]))
'''
# 꼭 인덱스로 접근하지 좀 마라....
        