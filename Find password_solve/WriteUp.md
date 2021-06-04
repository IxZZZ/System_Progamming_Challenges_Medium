# **Find password**

# Task
File: password.exe

Chạy thử file:

```bash
└─$ ./password.exe
inserisci la password per accedere al programma abcd
password errata.
inserisci la password per accedere al programma abdadsas
password errata.
inserisci la password per accedere al programma 12123
password errata.
inserisci la password per accedere al programma
```

Bài này yêu cầu chúng ta nhập vào `password` cho đến khi đúng

Dùng lệnh `file` để kiểm tra file 32/64 bit

```bash
└─$ file password.exe
password.exe: PE32 executable (console) Intel 80386 (stripped to external PDB), for MS Windows
```

## Solution

Load file bằng IDA pro và tiến hành phân tích

code hàm `main` (trong source ở dưới một số hàm đã được phân tích và đổi tên để dễ hiểu hơn)

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int v4; // [esp+0h] [ebp-88h] BYREF
  char v5[4]; // [esp+1Ch] [ebp-6Ch] BYREF
  int v6; // [esp+20h] [ebp-68h]
  int (__cdecl *v7)(int, int, __int64, _BYTE *, int); // [esp+34h] [ebp-54h]
  int *v8; // [esp+38h] [ebp-50h]
  char *v9; // [esp+3Ch] [ebp-4Ch]
  void (__noreturn *v10)(); // [esp+40h] [ebp-48h]
  int *v11; // [esp+44h] [ebp-44h]
  void *Buf2; // [esp+50h] [ebp-38h]
  int v13; // [esp+54h] [ebp-34h]
  char v14[16]; // [esp+58h] [ebp-30h] BYREF
  void *Buf1; // [esp+68h] [ebp-20h] BYREF
  size_t Size; // [esp+6Ch] [ebp-1Ch]
  char v17[16]; // [esp+70h] [ebp-18h] BYREF
  char v18; // [esp+80h] [ebp-8h] BYREF

  v7 = sub_4017D0;
  v8 = dword_4B5DE0;
  v9 = &v18;
  v11 = &v4;
  v10 = sub_4B5965;
  sub_427910(v5);
  sub_4270A0();
  Buf2 = v14;
  v6 = -1;
  sub_401360("djejie", (int)"");
  Buf1 = v17;
  v6 = 1;
  sub_401360("ggkfjgjfrg", (int)"");
  v6 = 2;
  print_n((int)&dword_4C6860, "inserisci la password per accedere al programma ");
  scanf(&dword_4C6900, &Buf1);
  do
  {
    do
    {
      v6 = 2;
      print(&dword_4C6860, (int)"password errata.\n", 17);
      print(&dword_4C6860, (int)"inserisci la password per accedere al programma ", 48);
      scanf(&dword_4C6900, &Buf1);
    }
    while ( Size != v13 );
  }
  while ( memcmp(Buf1, Buf2, Size) );
  print(&dword_4C6860, (int)"benvenuto", 9);
  sub_4B0D70(&dword_4C6860);
  if ( Buf1 != v17 )
    j_free(Buf1);
  if ( Buf2 != v14 )
    j_free(Buf2);
  sub_427A70((int *)v5);
  return 0;
}
```

Đoạn này là chính là đoạn code mà chúng ta muốn chương trình in ra, để chương trình in ra thì chương trình phải thoát khỏi hai vòng `while`
![image](https://user-images.githubusercontent.com/31529599/120765711-aebc7880-c543-11eb-8391-18dc03b9733f.png)


Tuy nhiên trước khi nhảy vào 2 vòng `while`chương trình đã yêu cầu nhập vào input và in ra :
![image](https://user-images.githubusercontent.com/31529599/120766337-55a11480-c544-11eb-93ab-fd8f2f3a040d.png)

Vậy để nhảy vào vòng `while` ta phải nhập vào một chuỗi bất kỳ đầu tiên sau đó chương trình sẽ bắt đầu kiểm tra điều kiện từ chuổi thứ 2 nhập vào 


Ta đặt breakpoint ngay nơi mà cương trình yêu cầu nhập vào trong `while` và tiến hành debug
![image](https://user-images.githubusercontent.com/31529599/120766087-1377d300-c544-11eb-9da2-2d6d0880da97.png)

chuỗi thứ 2 nhập vào khi debug là `bbbbb` có size là `5`
![image](https://user-images.githubusercontent.com/31529599/120766960-eed02b00-c544-11eb-81e0-8cd0ac4e3e5d.png)

Ở instruction tiếp theo, chương trình sẽ so sánh size của chuỗi nhập vào với `6` nếu khác `6` nhập lại, nếu bằng `6` sẽ kiểm tra điều kiện ở vòng while tiếp theo 
![image](https://user-images.githubusercontent.com/31529599/120767088-0f988080-c545-11eb-9db1-ca6f828a6c7c.png)

Nhập vào `bbbbbb` size bằng `6` và debug tiếp

Ở điều kiện tiếp theo chương trình sẽ gọi hàm `memcmp` để so sánh hai chuỗi `buf2` và chuỗi nhập vào `buf1`, khi debug ta thấy giá trị của `buf2` = `djejie` ( như hình ở dưới)

![image](https://user-images.githubusercontent.com/31529599/120767849-ce54a080-c545-11eb-8d27-1cb387af7d7e.png)


## Chạy chương trình
Nhập vào chuỗi thứ 2 là chuỗi vừa tìm được `djejie`

![image](https://user-images.githubusercontent.com/31529599/120768024-f47a4080-c545-11eb-89e3-32512c54f560.png)

Xong !



