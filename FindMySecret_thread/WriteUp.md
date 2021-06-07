# **FindMySecret**

# Task

File: FindMySecret.exe

Chạy thử File:

```bash
└─$ ./FindMySecret.exe
Enter the secret number12312
Invalid Range...

Enter the secret number123
Nope, you have not yet found the secret number.
4206918
```

Chạy lệnh `file` để kiểm tra file 32/64 bit

```bash
└─$ file FindMySecret.exe
FindMySecret.exe: PE32 executable (console) Intel 80386 (stripped to external PDB), for MS Windows
```

=> File windows 32 bit


## Solution

Load file bằng IDA pro 32bits và tiến hành phân tích

Vì bài này code khá nhiều và dài, cho nên hầu hết các hàm liên quan đã được mình sửa lên lại cho dễ đọc, chứ IDA không tự detect ra được các tên như vậy.

code main:

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  __int16 ArgList; // [esp+18h] [ebp-10h] BYREF

  sub_4019C0();
  ArgList = 0;
  beginthread(StartAddress, 0, &ArgList);
  ArgList = 1;
  while ( 1 )
    ;
}
```

Bài này là một bài đa luồng threading và chương trình có một số đoạn code anti debug phát hiện debug và thoát chương trình nên phân tích hơi khó khăn,

Đầu tiên ta sẽ nhảy đến địa chỉ mà thread gọi đầu tiên `StartAddress`

