# **CrackMe2 - Classical cipher**

# Task

File: CrackMe2.exe

Chạy thử file:

![image](https://user-images.githubusercontent.com/31529599/120931558-4e346380-c71c-11eb-9a53-2df79737a5fd.png)

Bài này yêu cầu chúng ta nhập vào `password` cho đến khi nào đúng

Chạy lệnh `file` để kiểm tra `file` 32/64 bit

```bash
└─$ file CrackMe2.exe
CrackMe2.exe: PE32 executable (console) Intel 80386, for MS Windows
```

=> File windows 32 bit

## Solution 

Load file bằng IDA Pro và tiến hành phân tích

code main:

```bash
int __cdecl main(int argc, const char **argv, const char **envp)
{
  unsigned __int8 v3; // al
  char *i; // ecx
  int v5; // eax
  char v7; // [esp-Ch] [ebp-110h]
  char v8; // [esp-8h] [ebp-10Ch]
  char v9; // [esp-8h] [ebp-10Ch]
  char v10; // [esp-4h] [ebp-108h]
  char Buffer[256]; // [esp+0h] [ebp-104h] BYREF

  sub_4010B0("-----------------------------------\n", Buffer[0]);
  sub_4010B0("--           CrackMe 2           --\n", v10);
  sub_4010B0("--      by github.com/dajoh      --\n", v8);
  sub_4010B0("-----------------------------------\n\n", v7);
  while ( 1 )
  {
    sub_401010((int)"Enter password: ", 0xFu, Buffer[0]);
    gets_s(Buffer, 0x100u);
    v3 = Buffer[0];
    for ( i = Buffer; *i; v3 = *i )
      *i++ = asc_4188F0[v3];
    v5 = strcmp(Buffer, "HfyhgrgfgrlmYlc579");
    if ( v5 )
      v5 = v5 < 0 ? -1 : 1;
    if ( !v5 )
      break;
    sub_401010((int)"Fail! You entered the wrong password.\n\n", 0xCu, Buffer[0]);
  }
  sub_401010((int)"Congratulations! You entered the correct password.\n\n", 0xAu, Buffer[0]);
  sub_401010((int)"Press enter to exit...", 8u, v9);
  sub_404D1E();
  return 0;
}
```

Phân tích sơ lược đoạn code trên ta thấy chương trình sẽ nhập vào một chuỗi và thực hiện một vòng `for` duyệt lần lượt tất cả các ký tự chuỗi nhập vào và thay đổi ký tự đó bằng câu lệnh:

`*i++ = asc_4188F0[v3];`

với `i` là địa chỉ của ký tự trong chuỗi nhập vào,

`asc_4188F0` một chuỗi gồm `256` ký tự được lưu sẵn vào chương trình 

![image](https://user-images.githubusercontent.com/31529599/120931829-7a041900-c71d-11eb-96bf-935070962d1e.png)

Câu lệnh trên thực hiện lấy giá trị ascii của ký tự nhập vào làm index của mảng `asc_4188F0` để xác định giá trị mới của ký tự đó, sau đó so sánh chuỗi mới với chuỗi `HfyhgrgfgrlmYlc579`  nếu khác nhau (`v5=1` hoặc `v5=-1`) yêu cầu nhập lại, nếu bằng nhau (`v5 = 0`) thì thoát vòng for và in ra câu đúng

## python script

```python

# dựng lại mảng asc_4188F0 
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0xa, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10, 0x11,
       0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F]

str1 = ' !"#$%&'

arr1 = [0x27]

str2 = '()*+,-./9876543210:;<=>?@ZYXWVUTSRQ'

str3 = 'PONMLKJIHGFEDCBA[\]^_`zyxwvutsrqponmlkjihgfedcba'

print(len(arr))
#chuyển lần lượt các ký tự char thành ascii value và nối vào mảng arr

for c in str1:
    arr.append(ord(c))

arr += arr1
for c in str2:
    arr.append(ord(c))
    
for c in str3:
    arr.append(ord(c))
    

#đây là chuỗi sau khi qua vòng for
str = "HfyhgrgfgrlmYlc579"
print(arr)

# tìm ký tự của chuỗi str trong mảng và gán index(vị trí phần tử) này như là một ký tự của chuỗi nhập vào 
res = ''
for c in str:
    for i in range(len(arr)):
        if ord(c) == arr[i]:
            res += chr(i)
            break

print('result: ', res)

```

### Chạy script

![image](https://user-images.githubusercontent.com/31529599/120932094-a8362880-c71e-11eb-8f4e-89a82c71cf7e.png)

phần đầu là mảng `asc_4188F0`

phần sau là chuỗi mà chúng ta phải nhập vào `SubstitutionBox420`


## Chạy chương trình với chuỗi vừa tìm được 

![image](https://user-images.githubusercontent.com/31529599/120932143-de73a800-c71e-11eb-9d6c-a02e48ca6a9d.png)

Xong !
