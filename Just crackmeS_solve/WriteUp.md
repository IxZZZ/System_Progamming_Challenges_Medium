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

Ở trên vì user của chương trình đang sài là `ixz` nên chuỗi được đưa vào hàm `compare` sẽ là `Wait, your name isixz`, tuy nhiên ta chỉ cần debug tới trước hàm `strcp` là sẽ biết được chuỗi `v6`

Sử dụng gdb để debug 



# Chạy chương trình
Nhập và chuỗi vừa tìm được 

