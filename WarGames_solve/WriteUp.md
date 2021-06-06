# **WarGames**

## Task

File: WarGames

Chạy thử file: 

![image](https://user-images.githubusercontent.com/31529599/120932269-4e822e00-c71f-11eb-951a-674c63b15ae2.png)

Bài này yêu cầu chúng ta truyền tham số lúc thực thi và sau đó kiểm tra tham số như một `password`

Chạy lệnh `file` để xem file là 32/64 bit

```bash
└─$ file WarGames
WarGames: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, BuildID[sha1]=9a0e6dfa0e34cb42a1d5524f94d26424fff8625e, for GNU/Linux 3.2.0, not stripped
```

## Solution

code main:

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int result; // eax
  int v4; // [rsp+18h] [rbp-28h]
  unsigned __int64 i; // [rsp+20h] [rbp-20h]
  _BYTE v6[9]; // [rsp+2Fh] [rbp-11h] BYREF
  unsigned __int64 v7; // [rsp+38h] [rbp-8h]

  v7 = __readfsqword(0x28u);
  if ( argc == 2 )
  {
    if ( j_strlen_ifunc() == 9 )
    {
      qmemcpy(v6, "gssw#tpcz", sizeof(v6));
      v4 = 0;
      srandom(1983LL);
      for ( i = 0LL; i <= 8; ++i )
      {
        v6[i] -= (int)rand() % 5 + 1;
        if ( v6[i] != argv[1][i] )
        {
          v4 = 1;
          break;
        }
      }
      if ( v4 )
        puts("Wrong Password !!!");
      else
        puts("Congratulation !!!");
      result = 0;
    }
    else
    {
      puts("Wrong Password !!!");
      result = 0;
    }
  }
  else
  {
    puts("Use ./WarGames pass");
    result = 0;
  }
  return result;
}
```


Mục đích của chúng ta là in ra dòng `Congratulation !!!`

![image](https://user-images.githubusercontent.com/31529599/120932483-28a95900-c720-11eb-8c3e-d58ae2c7434f.png)

Để chương trình in ra dòng này thì `v4` phải bằng `0`, nghĩa là vòng `for` không được thay đôi `v4` ( câu `if` trong `for` phải luôn sai)

Ta thấy câu `if` sẽ so sánh từng chuỗi của tham số truyền vòng với chuỗi được lưu ở `v6`

`v6` ban đầu được gán `gssw#tpcz`
Với từ ký tự của `v6` được tính lại bằng dòng lệnh `v6[i] -= (int)rand() % 5 + 1;` vì ở trên chương trình gọi hàm `srandom(1983LL);` với số dương nên chương trình sẽ sinh ra dãy số random giống nhau khi thực khi chương trình.

Vì vậy bài này ta chỉ cần đặt breakpoint tại câu `if` rồi chạy tới đó và xem `v6` sẽ có nhưng giá trị gì,sau đó thay thế bằng gia trị đó và tiếp tực debug cứ như vậy cho hết vòng `for` ta sẽ được chuỗi nhập vào đúng, vì bài này chuỗi chỉ có 9 ký tự nên ta chỉ cần debug gdb bằng tay đơn giản

với lần 9 lần debug ta được chuỗi tương ưng với từ ký tự của `v6` = `dont play`

## Chạy chương trình với chuỗi vừa tìm được 

Vì chuỗi nhập vào có dấu cách nên ta phải dùng dấu backslash `\` để chương trình hiểu nó là một chuỗi liên tiếp

```bash
└─$ ./WarGames dont\ play
Congratulation !!!
```

Xong !
