# **no strings attached**

## Task

File: crackme.exe

Chạy thử file:

```bash
└─$ ./crackme.exe
Enter password: hello
WRONG PASSWORD
```

Bài này yêu cầu chúng ta nhập đúng `password`

Chạy lệnh file để kiểm tra file 32/64 bit

```bash
└─$ file crackme.exe
crackme.exe: PE32 executable (console) Intel 80386, for MS Windows
```

=> File windows 32 bits

## Solution

Load file bằng IDA pro 32bit và tiến hành phần tích

Code main:

(một số tên hàm đã được phân tích và sửa lại tên cho dễ đọc)
```c
int __cdecl main_0(int argc, const char **argv, const char **envp)
{
  int v3; // eax
  char v5[108]; // [esp+14h] [ebp-E0h] BYREF
  char v6[36]; // [esp+80h] [ebp-74h] BYREF
  char correct_str[16]; // [esp+A4h] [ebp-50h] BYREF
  char wrong_str[24]; // [esp+B4h] [ebp-40h] BYREF
  char enter_str[24]; // [esp+CCh] [ebp-28h] BYREF
  int v10; // [esp+F0h] [ebp-4h]

  strcpy(enter_str, "Enter password: ");
  strcpy(wrong_str, "WRONG PASSWORD");
  strcpy(correct_str, "CORRECT");
  print(std::cout, enter_str);
  sub_4010C8();
  v10 = 0;
  gets(std::cin, v6);
  sub_401352(v5);
  LOBYTE(v10) = 1;
  sub_4012C1(v6);
  if ( (unsigned __int8)sub_401438(v5) )
    v3 = print(std::cout, correct_str);
  else
    v3 = print(std::cout, wrong_str);
  std::ostream::operator<<(v3, sub_4013C5);
  while ( !std::ios_base::eof((std::ios_base *)(*(_DWORD *)(std::cin + 4) + std::cin)) )
    ;
  LOBYTE(v10) = 0;
  sub_401177(v5);
  v10 = -1;
  sub_401343(v6);
  return 0;
}
```


