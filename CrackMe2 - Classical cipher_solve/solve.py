arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0xa, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10, 0x11,
       0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F]

str1 = ' !"#$%&'

arr1 = [0x27]

str2 = '()*+,-./9876543210:;<=>?@ZYXWVUTSRQ'

str3 = 'PONMLKJIHGFEDCBA[\]^_`zyxwvutsrqponmlkjihgfedcba'

print(len(arr))
for c in str1:
    arr.append(ord(c))

arr += arr1
for c in str2:
    arr.append(ord(c))
for c in str3:
    arr.append(ord(c))
str = "HfyhgrgfgrlmYlc579"
print(arr)

res = ''
for c in str:
    for i in range(len(arr)):
        if ord(c) == arr[i]:
            res += chr(i)
            break

print('result: ', res)
