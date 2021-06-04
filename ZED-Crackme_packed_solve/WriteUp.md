# **ZED-Crackme**

# Task
File: ZED-Crackme-x64.bin

Chạy thử file:

```bash
└─$ ./ZED-Crackme-x64.bin
Segmentation fault
```
Khi chạy file ta thấy file bị lỗi `segmentation`

Chạy lệnh  `file` để xem file là 32/64 bit

```bash
└─$ file ZED-Crackme-x64.bin
ZED-Crackme-x64.bin: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), statically linked, no section header
```
-> file linux 64 bit

## Solution

Load file bằng IDA pro 64 bit và tiến hành phân tích

![image](https://user-images.githubusercontent.com/31529599/120779662-76bc3200-c551-11eb-8436-2c114d27f024.png)

Ta thấy IDA không tự động phân tích được gì nhiều từ file này

Load file bằng phần mềm DIE (Detect it easy) để kiểm tra file có bị `pack` hay không

![image](https://user-images.githubusercontent.com/31529599/120780503-66588700-c552-11eb-83aa-d734fbd16f36.png)

Ta thấy DIE detect được file đã bị pack bằng UPX 3.94

Vì bài này đơn giản nên ta chỉ cần decompress file bằng lệnh `upx` với option -d trên linux 

![image](https://user-images.githubusercontent.com/31529599/120780805-a586d800-c552-11eb-8803-469b320b0ca4.png)

### Chạy lại file

```bash
└─$ ./ZED-Crackme-x64.bin
***********************
**      rules:       **
***********************

* do not bruteforce
* do not patch, find instead the serial.

enter the passphrase: hello
try again
```

Vậy file đã được `unpack` và chạy bình thường

Bài này yêu cầu chúng ta nhập đúng chuỗi `passphrase` load file được unpack bằng IDA pro 64 bit và phân tích

Bây giờ thì IDA đã tự động detect được hàm `main`
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int i; // [rsp+14h] [rbp-9Ch]
  char v5[6]; // [rsp+1Ah] [rbp-96h] BYREF
  __int64 v6[4]; // [rsp+20h] [rbp-90h] BYREF
  char s2[32]; // [rsp+40h] [rbp-70h] BYREF
  char s1[32]; // [rsp+60h] [rbp-50h] BYREF
  char v9[40]; // [rsp+80h] [rbp-30h] BYREF
  unsigned __int64 v10; // [rsp+A8h] [rbp-8h]

  v10 = __readfsqword(0x28u);
  puts("***********************");
  puts("**      rules:       **");
  puts("***********************");
  putchar(10);
  puts("* do not bruteforce");
  puts("* do not patch, find instead the serial.");
  putchar(10);
  strcpy(v9, "This is a top secret text message!");
  __sidt(v5);
  if ( v5[5] == -1 )
  {
    puts("VMware detected");
    exit(1);
  }
  rot(13LL, v9);
  rot(13LL, v9);
  qmemcpy(v6, "AHi23DEADBEEFCOFFEE", 19);
  printf("enter the passphrase: ");
  __isoc99_scanf("%s", s2);
  if ( ptrace(PTRACE_TRACEME, 0LL) < 0 )
  {
    puts("This process is being debugged!!!");
    exit(1);
  }
  s1[0] = LOBYTE(v6[0]) ^ 2;
  s1[1] = BYTE3(v6[0]) - 10;
  s1[2] = BYTE2(v6[0]) + 12;
  s1[3] = BYTE2(v6[0]);
  s1[4] = BYTE1(v6[0]) + 1;
  for ( i = 5; i <= 18; ++i )
    s1[i] = *((_BYTE *)v6 + i) - 1;
  if ( !strcmp(s1, s2) )
    puts("you succeed!!");
  else
    puts("try again");
  return 0;
}
```

Phân tích sơ lược thì file chương trình sẽ nhập vào một chuỗi và so sánh chuỗi nhập vào với chuỗi được lưu ở `s1` với `s1` được tính từ các byte của chuỗi `v6` (`AHi23DEADBEEFCOFFEE`)

Đây là đoạn code để tính ra `s1`
![image](https://user-images.githubusercontent.com/31529599/120781818-a10eef00-c553-11eb-9b9f-c278d3bc5d74.png)

Nếu bình thường thì ta có thể debug và xem giá trị của `s1` được tạo ra sau khi tính, tuy nhiên thì chương trình đã đặt một đoạn code detect debug và thoát chương trình nên ta không thể debug được 
![image](https://user-images.githubusercontent.com/31529599/120782023-cc91d980-c553-11eb-9aa8-7d3f8c605251.png)


Script python để tính `s1` từ chuỗi `v6`

```python
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
```
## Chạy script python

```bash
└─$ python solve.py
C(uiICD@CADDEBNEEDD
```
Vậy chuỗi `s1` sẽ là `C(uiICD@CADDEBNEEDD`

### Chạy chương trình

Nhập chuỗi vừa tìm được 

```bash
└─$ ./ZED-Crackme-x64.bin
***********************
**      rules:       **
***********************

* do not bruteforce
* do not patch, find instead the serial.

enter the passphrase: C(uiICD@CADDEBNEEDD
you succeed!!
```
Xong !
