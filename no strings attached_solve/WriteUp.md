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

![image](https://user-images.githubusercontent.com/31529599/120950360-cf1d4a80-c770-11eb-906e-616b2186bce7.png)

Để in ra được chuỗi `Correct` thì ta phải pass được câu lệnh `if ( (unsigned __int8)sub_C01438(v5) )`, với `v5` là một chuỗi có sẵn trong chương trình:

Đây là giá trị của `v5` sau khi gọi hàm `sub_C01352`

![image](https://user-images.githubusercontent.com/31529599/120950533-2de2c400-c771-11eb-94ef-558e4a3b4512.png)

Đây là `stack` của vùng nhớ của `v5`
```bash
Stack[00000BE4]:00D1F7FC db  65h ; e
Stack[00000BE4]:00D1F7FD db    0
Stack[00000BE4]:00D1F7FE db    0
Stack[00000BE4]:00D1F7FF db    0
Stack[00000BE4]:00D1F800 db  6Eh ; n
Stack[00000BE4]:00D1F801 db    0
Stack[00000BE4]:00D1F802 db    0
Stack[00000BE4]:00D1F803 db    0
Stack[00000BE4]:00D1F804 db  63h ; c
Stack[00000BE4]:00D1F805 db    0
Stack[00000BE4]:00D1F806 db    0
Stack[00000BE4]:00D1F807 db    0
Stack[00000BE4]:00D1F808 db  72h ; r
Stack[00000BE4]:00D1F809 db    0
Stack[00000BE4]:00D1F80A db    0
Stack[00000BE4]:00D1F80B db    0
Stack[00000BE4]:00D1F80C db  79h ; y
Stack[00000BE4]:00D1F80D db    0
Stack[00000BE4]:00D1F80E db    0
Stack[00000BE4]:00D1F80F db    0
Stack[00000BE4]:00D1F810 db  70h ; p
Stack[00000BE4]:00D1F811 db    0
Stack[00000BE4]:00D1F812 db    0
Stack[00000BE4]:00D1F813 db    0
Stack[00000BE4]:00D1F814 db  74h ; t
Stack[00000BE4]:00D1F815 db    0
Stack[00000BE4]:00D1F816 db    0
Stack[00000BE4]:00D1F817 db    0
Stack[00000BE4]:00D1F818 db  65h ; e
Stack[00000BE4]:00D1F819 db    0
Stack[00000BE4]:00D1F81A db    0
Stack[00000BE4]:00D1F81B db    0
Stack[00000BE4]:00D1F81C db  64h ; d
Stack[00000BE4]:00D1F81D db    0
Stack[00000BE4]:00D1F81E db    0
Stack[00000BE4]:00D1F81F db    0
Stack[00000BE4]:00D1F820 db  2Dh ; -
Stack[00000BE4]:00D1F821 db    0
Stack[00000BE4]:00D1F822 db    0
Stack[00000BE4]:00D1F823 db    0
Stack[00000BE4]:00D1F824 db  63h ; c
Stack[00000BE4]:00D1F825 db    0
Stack[00000BE4]:00D1F826 db    0
Stack[00000BE4]:00D1F827 db    0
Stack[00000BE4]:00D1F828 db  2Dh ; -
Stack[00000BE4]:00D1F829 db    0
Stack[00000BE4]:00D1F82A db    0
Stack[00000BE4]:00D1F82B db    0
Stack[00000BE4]:00D1F82C db  73h ; s
Stack[00000BE4]:00D1F82D db    0
Stack[00000BE4]:00D1F82E db    0
Stack[00000BE4]:00D1F82F db    0
Stack[00000BE4]:00D1F830 db  74h ; t
Stack[00000BE4]:00D1F831 db    0
Stack[00000BE4]:00D1F832 db    0
Stack[00000BE4]:00D1F833 db    0
Stack[00000BE4]:00D1F834 db  72h ; r
Stack[00000BE4]:00D1F835 db    0
Stack[00000BE4]:00D1F836 db    0
Stack[00000BE4]:00D1F837 db    0
Stack[00000BE4]:00D1F838 db  69h ; i
Stack[00000BE4]:00D1F839 db    0
Stack[00000BE4]:00D1F83A db    0
Stack[00000BE4]:00D1F83B db    0
Stack[00000BE4]:00D1F83C db  6Eh ; n
Stack[00000BE4]:00D1F83D db    0
Stack[00000BE4]:00D1F83E db    0
Stack[00000BE4]:00D1F83F db    0
Stack[00000BE4]:00D1F840 db  67h ; g
```

Tuy nhiên chuỗi này không liên tiếp mà cách nhau bỏi 4 ô nhớ trên `stack`

Tiếp tục phân tích hàm `sub_C063D0` được câu `if` gọi để kiểm tra điều kiện

```c
char __thiscall sub_C063D0(char *this)
{
  int i; // [esp+0h] [ebp-Ch]

  if ( sub_C01645(0xCCCCCCCC) != 18 )
    return 0;
  for ( i = 0; i < 18; ++i )
  {
    if ( *(char *)sub_C0164A(i) != this[4 * i] )
      return 0;
  }
  return 1;
}
```
Mục đích của chúng ta muốn là hàm này sẽ trả về một số khác `0` mà cụ thể trong bài này sẽ là `1`

Trong hàm này có hai phần chính là câu lệnh `if` vòng `for` cả hai phần này điều ảnh hưởng đến giá trị trả về nên chúng ta sẽ tiến hành phân tích cả hai phần

Với câu lệnh `if ( sub_C01645(0xCCCCCCCC) != 18 )` , thì trong quá trình debug ta biết được hàm này sẽ trả về độ dài của chuỗi `password` mà chúng ta nhập vào 

Mình đã thử và chuỗi và đây là của chuỗi `abcd`

![image](https://user-images.githubusercontent.com/31529599/120951466-10aef500-c773-11eb-8022-fa270b38005f.png)

Ta thấy giá trị trả về sẽ là `eax = 0x4` bằng với độ dài chuỗi `abcd`

Vậy chuỗi nhập vào phải có độ dài `18` ký tự để sai câu `if` và chương trình không trả về `0` (tuy nhiên ta cũng có thể đoán được hàm `sub_C01645` là tính độ dài của chuỗi nhập vào bởi vì kết quả được so sánh với `18` và ở vòng `for` bên dưới cũng thực hiện vòng lặp `18` lần có thể là cho `18` ký tự của chuỗi nhập vào)

Nhập một chuỗi có độ dài `18` ký tự `a` và tiếp tục debug, phân tích vòng `for` tiếp theo,

Vòng for ở trên sẽ thực hiện gọi hàm `sub_C0164A` với tham số truyền vào là `i` index của phần tử nhập vào!

![image](https://user-images.githubusercontent.com/31529599/120951914-283aad80-c774-11eb-999f-40a62c7ba0ad.png)

Ta thấy sau ghi gọi hàm `sub_C0164A` thì giá trị trả về sẽ là mảng ký tự `password` mà chúng ta nhập vào, mà cụ thể ở đây thì chương trình sẽ thực hiện lấy từ byte `1` của mảng nhập vào và so sánh với `this[4 * i]` chính là mảng `v5` truyền vào 

Như ta đã biết thì mảng `v5` chứa các ký tự cách nhau `4` ô nhớ nên index của `this` được nhân `4` tương ứng sau mỗi lần lặp

![image](https://user-images.githubusercontent.com/31529599/120952054-718afd00-c774-11eb-893b-3a9e464b48ff.png)

Vậy `password` nhập vào sẽ là các ký tự cách nhau `4` ô nhớ trong `v5` = `encrypted-c-string` có độ dài đúng `18` bytes

## Chạy chương trình với chuỗi vừa tìm được 

```bash
└─$ ./crackme.exe
Enter password: encrypted-c-string
CORRECT
```

Xong !



