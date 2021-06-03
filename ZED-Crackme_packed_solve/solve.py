str = 'AHi23DEADBEEFCOFFEE'

res = ''
res += chr(ord(str[0]) ^ 2)

res += chr(ord(str[3])-10)

res += chr(ord(str[2])+12)

res += chr(ord(str[2]))

res += chr(ord(str[1])+1)

for i in range(5, 19):
    res += chr(ord(str[i])-1)

print(res)
print("len: ", len(res))
