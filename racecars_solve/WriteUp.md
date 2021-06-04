# **racecars**

## Task

File: racecars

Chạy thử file:

```bash
└─$ ./racecars
Gimme what I want!
```

Ở bài này chương trình không nhận input nhập vào

Chạy lệnh file để kiểm tra file 32/64 bit

```bash
└─$ file racecars
racecars: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=84eee6611847da3272d223e4129ccbc5febe4231, for GNU/Linux 3.2.0, with debug_info, not stripped
```

-> file linux 64 bit

## Solution

Load file bằng IDA pro 64 và tiến hành phân tích

code `main`

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int start; // [rsp+18h] [rbp-8h]
  int end; // [rsp+1Ch] [rbp-4h]

  end = strlen(*argv) - 1;
  for ( start = end; (*argv)[start - 1] != '/'; --start )
    ;
  while ( start < end )
  {
    if ( (*argv)[start] != (*argv)[end] )
    {
      puts("Gimme what I want!");
      exit(1);
    }
    --end;
    ++start;
  }
  puts("That's exactly what I wanted!");
  return 0;
}
```

bài này chưa trình sẽ tự đọc vào `arg` đầu tiên chính là đường dẫn tuyệt đối của file thực thi, vd ở trong máy sẽ là `/mnt/e/LEARNING/System programming/RE challenges/medium/Release_2_copy/Release_2/racecars/racecars`

Sau đó vòng for sẽ thực hiện duyệt ngược từ cuối chuỗi trở về đầu chuỗi cho đến khi gặp ký tự `\` đầu tiên sẽ dừng lại

Nghĩa là sẽ duyệt hết `tên` của file thực thi

sau đó vòng while sẽ kiểm tra ký tự tại (`start`) (ký tự đầu tiên của tên file)  với ký tự cuối `end` nếu khác nhau sẽ in ra chuỗi `Gimme what I want!` và thoát chương trình, sau đó tăng `start` và giảm `end` xuống cho đến khi duyệt hết tên file và in ra dòng `That's exactly what I wanted!`

Vậy để điều kiện không sai thì tên file phải gồm các ký tự giống nhau
đổi tên file thành `aaaaaa`

## Chạy file

```bash
└─$ ./aaaaaa
That's exactly what I wanted!
```
