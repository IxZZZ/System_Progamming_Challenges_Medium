# **Just crackmeS**

## Task

File: a.out

Chạy thử file:

```bash
└─$ ./a.out
Enter your flag.
hello
Try again
```
-> bài này yêu cầu chúng ta nhập đúng chuỗi flag

Chạy lệnh `file` để xem file 32/64 bit

```bash
└─$ file a.out
a.out: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=ed76b7e31e4e28ac60796e87722903fcffaf9af3, for GNU/Linux 3.2.0, not stripped
```
-> file linux 64 bit

## Solution

Load file với IDA pro 64 bit và tiến hành phân tích

code main:

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  const char *src; // [rsp+8h] [rbp-E8h]
  char *s; // [rsp+10h] [rbp-E0h]
  __int64 v6; // [rsp+18h] [rbp-D8h]
  char v7[200]; // [rsp+20h] [rbp-D0h] BYREF
  unsigned __int64 v8; // [rsp+E8h] [rbp-8h]

  v8 = __readfsqword(0x28u);
  if ( !malloc(0x46uLL) )
    exit(1);
  src = getenv("USER");
  s = (char *)malloc(0x12CuLL);
  if ( !s )
    exit(1);
  strcpy(&s[strlen(s)], "Wait, your name is");
  strcat(s, src);
  puts("Enter your flag.");
  __isoc99_scanf("%s", v7);
  v6 = compare(s);
  if ( (unsigned int)strcp(v6, v7) )
    printf("Try again");
  else
    printf("Done.");
  return 0;
}
```

Theo như code ở trên thì ta thấy chương trình sẽ gọi hàm `getenv("USER")` để lấy ra tên username đang sử dụng hệ điều hành, sau đó gọi hàm `strcat` để nối chuỗi `Wait, your name is` với `username` vừa có

Sau đó chuỗi được truyền vào hàm `compare` để tạo ra một chuỗi mới được lưu vào `v6` 

Cuối cùng sẽ so sánh input nhập vào với chuỗi được lưu trong `v6` nếu bằng nhau sẽ in ra `Done` nếu sai sẽ in ra `Try again`

Ở trên vì user của chương trình đang sài là `ixz` nên chuỗi được đưa vào hàm `compare` sẽ là `Wait, your name isixz`

code hàm `compare`
```c
__int64 __fastcall compare(__int64 a1)
{
  int i; // [rsp+18h] [rbp-28h]
  time_t timer; // [rsp+28h] [rbp-18h] BYREF
  struct tm *v4; // [rsp+30h] [rbp-10h]
  unsigned __int64 v5; // [rsp+38h] [rbp-8h]

  v5 = __readfsqword(0x28u);
  time(&timer);
  v4 = localtime(&timer);
  for ( i = 0; i < (int)stlen(a1); ++i )
    *(_BYTE *)(i + a1) ^= v4->tm_min >> v4->tm_mday;
  return a1;
}
```

Phân tích hàm này ta thấy chương trình sẽ lấy từng ký tự của chuỗi truyền vào (`Wait, your name isixz`) rồi thực hiện `xor` với (min>>day) (với >> là dịch phải bit, min là giá trị của phút hiện tại, day là giá trị của ngày hiện tại trong tháng) sau đó trả về kết quả
 
 Vậy kết quả sẽ phụ thuộc vào thời gian hiện tại
 
 Python script
 ```
 import time

current_time = time.localtime(time.time())

str = "Wait, your name isixz"
str_list = list(str)

for i in range(len(str)):
    str_list[i] = chr(ord(str_list[i]) ^ (current_time.tm_min >> current_time.tm_mday))

print("".join(str_list))
 ```
 Đoạn code python trên sẽ in ra chuỗi mà chương trình cần
 
# Chạy chương trình
Với output của đoạn script python

```bash
└─$ python solve.py | ./a.out
Enter your flag.
Done.
```
Xong !

