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

![image](https://user-images.githubusercontent.com/31529599/120962176-6d1d0f00-c789-11eb-9dda-247595c4a77f.png)

`StartAddress` tham chiếu tới hàm `check_break_point_and_call_time` cho nên chúng ta sẽ phân tích hàm này:

```c
void __cdecl __noreturn check_break_point_and_call_time(_WORD *a1)
{
  void (__cdecl *v1)(int (__cdecl *)(int, const char **, const char **)); // [esp+1Ch] [ebp-Ch]

  while ( 1 )
  {
    while ( !*a1 )
      ;
    if ( *a1 == 1 )
    {
      v1 = (void (__cdecl *)(int (__cdecl *)(int, const char **, const char **)))check_break_point_and_exit_references;
      check_break_point_and_exit_references(StartAddress);
      v1(main_references);
      v1((int (__cdecl *)(int, const char **, const char **))time_caculate_in_thread_check_breakpoint_reference);
      v1((int (__cdecl *)(int, const char **, const char **))calculate_time_references);
      v1((int (__cdecl *)(int, const char **, const char **))call_to_win_references);
      *a1 = 0;
    }
    else if ( *a1 == 2 )
    {
      while ( a1[1] )
      {
        time_caculate_in_thread_check_breakpoint_reference();
        --a1[1];
      }
      *a1 = 0;
    }
  }
}
```

Vì hàm này nằm trong `thread` và khi chạy sẽ gọi một vòng `while(1)` chạy  liên tục, múc đích là kiểm tra biến `a1` 

### Nếu `a1` = `0` 
thì không thực hiện gì cả
### Nếu `a1` = `1` 
thì sẽ kiểm tra xem các hàm `StartAddress`,`main`,`time_caculate_in_thread_check_breakpoint`,`calculate_time`,`call_to_win` các hàm này có được đặt breakpoint hay không bằng cách truyền references của hàm này vào hàm `v1` chính là hàm `check_break_point_and_exit` , vì hầu hết các hàm của chương trình đã được kiểm tra checkpoint cho nên chúng ta không thể thực hiện debug trong bài này.

Ở đây chúng ta phân tích sơ lược hàm `check_break_point_and_exit`:

```c
int __cdecl check_break_point_and_exit(int a1)
{
  int result; // eax
  int v2; // [esp+1Ch] [ebp-Ch]

  v2 = 0;
  do
  {
    if ( *(_BYTE *)(v2 + a1) == 0xCC )
      exit(-20);
    result = *(unsigned __int8 *)(++v2 + a1);
  }
  while ( (_BYTE)result != 0xC3 );
  return result;
}
```

hàm này sẽ lần lược duyệt các `opcode` của từng hàm cho đến khi gặp `opcode` `0xc3` của lệnh `ret` nếu trong hàm có `opcode` `0xcc` chính là opcode mà chương trình dùng để debug( gọi `instuction softwere interrupt` để dừng chương trình ngay tại đó) thì chương trình sẽ gọi hàm `exit` tại đây và kết thúc chương trình 

### Nếu `a1` = `2`
thì sẽ gọi hàm `time_caculate_in_thread_check_breakpoint_reference` và thực hiện lặp `a1[1]` lần mà cụ thể ở đây là `a1[1]` = `5`

Chương trình sẽ gọi hàm này `5` lần để tính `result_time` là một biến được lưu trong vùng nhớ `bss` có thể sử dụng ở toàn bộ chương trình

với `value_3_8` = `3.8`
```c
void time_caculate_in_thread_check_breakpoint()
{
  result_time = value_3_8 * result_time * (1.0 - result_time);
}
```

## Cách mà chương trình thay đổi giá trị của `a1` để nhảy vào từng hàm

Đây là đoạn code asm trong hàm main:

![image](https://user-images.githubusercontent.com/31529599/120963387-b1111380-c78b-11eb-97d6-7d8e2655b8df.png)

Với `ebp+ArgList` chính là giá trị của `a1` mà chúng ta đề cập ở trên

Theo luồng chương trình từ trên xuống thì ta thấy `a1` sẽ có nhưng giá trị sau:

- `a1` bằng `0` trước khi bắt đầu `thread`

![image](https://user-images.githubusercontent.com/31529599/120963588-0cdb9c80-c78c-11eb-9f84-df2fdd1123fa.png)

- `a1` bằng `1` sau khi gọi `thread`

![image](https://user-images.githubusercontent.com/31529599/120963612-16fd9b00-c78c-11eb-9aae-f762704e5c35.png)

- `a1` bằng `2` sau khi gọi hàm `caculate_time`

![image](https://user-images.githubusercontent.com/31529599/120963690-3b597780-c78c-11eb-93b5-48aa87e0c44b.png)

Tuy nhiên đoạn code dưới đây là một vòng `while` vô hạn, chỉ nhảy xuống đoạn để set `a1` bằng `2` khi `[ebp+ArgList]` bằng `0`, nghĩa là vòng `while` này sẽ kiểm tra liên tục cho đến khi nào `a1` bằng `0`

Như đã nói ở trên thì hàm `check_break_point_and_call_time` trong thread vẫn chạy lên tục và sau khi đổi giá trị `a1` bằng `1` thì chương trình sẽ thực hiện câu `if(*a1==1)` trong vòng `while` và set `a1` về `0` cho nên sau đó đoạn có set `a2` = `2` sẽ được gọi

![image](https://user-images.githubusercontent.com/31529599/120963760-5cba6380-c78c-11eb-94e0-7e7baa7f0433.png)

### Tổng kết sơ lược

Luồn của chương trình sẽ là :
- set `a1` = 0 và gọi hàm `check_break_point_and_call_time` 
- set `a1` = 1 và hàm `check_break_point_and_call_time` sẽ set `a1` về 0
- gọi hàm `caculate_time` sau đó set `a1` = `2` và thực hiện câu ` else if ( *a1 == 2 )`  trong `check_break_point_and_call_time` và gọi `time_caculate_in_thread_check_breakpoint_reference` `5` lần với `a1[1]` chính là `mov  [ebp+var_E], 5`  được set trước khi set `a1` bằng `2`

=> Vậy biến `result_time` sẽ được tính trong hai hàm đó là `caculate_time` và `5` lần gọi hàm `time_caculate_in_thread_check_breakpoint_reference`

## Tiếp tục phân tích xuống dưới

Đầu tiên chúng ta phân tích hàm `call_to_win`:

Hàm này sẽ kiểm tra tham số truyền vào nếu khác  `0` sẽ in ra dòng `Success! You have completely reverse engineered and found the secret number!` nếu bằng `0` sẽ in ra dòng `Nope, you have not yet found the secret number`

```c
int __cdecl call_to_win(int a1)
{
  int result; // eax

  if ( a1 )
    result = puts("Success! You have completely reverse engineered and found the secret number!");
  else
    result = puts("Nope, you have not yet found the secret number.");
  return result;
}
```

Vậy mục đích của chúng ta là truyền vào tham số khác không khi gọi hàm này, mà cụ thể ở đây là `1`

Đây là đoạn code mà chương trình sau khi nhập vào và gọi hàm `call_to_win`:

![image](https://user-images.githubusercontent.com/31529599/120973328-fbe55800-c798-11eb-8a68-116ed86ebda9.png)

Trước khi gọi hàm `call_to_win` (`call edx`) thì chương trình gọi hàm `sub_401708`, mục đích của hàm này chỉ là nhân giá trị `result_time`  cho `10000` rồi so sánh với giá trị nhập vào nếu thõa set `[ebp+var_E]` thành `1` và `[ebp+var_E]` sẽ được truyền vào hàm `call_to_win` 

=> vậy mục đích của chúng ta là `[ebp+var_E]` bằng `1` sau khi gọi hàm `sub_401708`
![image](https://user-images.githubusercontent.com/31529599/120979333-b2e4d200-c79f-11eb-8ded-be1433cda978.png)


Đoạn code hàm `sub_401708`: 

```c
__int16 *__cdecl sub_401708(__int16 *a1)
{
  __int16 *result; // eax
  double v2; // [esp+10h] [ebp-8h]

  if ( !byte_406034 )
  {
    result_time = result_time * 10000.0;
    byte_406034 = 1;
  }
  v2 = (double)*a1;
  if ( result_time <= (long double)v2 || v2 <= result_time - 1.0 )
  {
    result = a1;
    *a1 = 0;
  }
  else
  {
    result = a1;
    *a1 = 1;
  }
  return result;
}
```

ở đây thì Chương trình sẽ kiểm tra `result_time` sau khi nhân `10000` với `v2` chính là giá trị nhập vào 

Mục đích của chúng ta muốn `a1`(`[ebp+var_E]` trước khi gọi `sub_401708`) được set bằng `1` cho nên sẽ làm sai câu lệnh `if` và nhảy vào `else` để set `a1`

Để câu `if` sai thì `result_time-1` < `v2` (`number` nhập vào) < `result_time`, nghĩa là chúng ta có thể sai câu `if` bằng cách nhập giá trị nguyên của `result` hoặc giá trị thập phân trong khoảng (`result_time-1`,`result_time`)

### Chúng ta tiến hành phân tích hai hàm tính `result_time`

Như đã phân tích ở trên, chương trình gọi hàm `caculate_time` trước:

Đoạn code này chủ yếu sẽ lấy `time(0)` thời giam hiện tại chia lấy dư cho `50` sau đó tiếp tục thực hiện chia tiếp cho `50` lưu ở dạng số thực vào `result_time`
```c
int calculate_time()
{
  int result; // eax

  do
    result = time(0) % 50;
  while ( 0.0 == (double)((long double)result / 50.0) );
  result_time = (long double)result / 50.0;
  return result;
}
```

Tiếp theo chương trình gọi `5` lần hàm `time_caculate_in_thread_check_breakpoint` như đã phân tích ở trên

```c
void time_caculate_in_thread_check_breakpoint()
{
  result_time = value_3_8 * result_time * (1.0 - result_time);
}
```

Vì Chia lấy dư cho `50` cho nên số giá trị nhập vào có giới hạn nên ở đây mình đã viết một script python để tính toàn bộ giá trị tính theo phần dư:

```python
import time

for t in range(50):
    f = t

    t = t/50

    for _ in range(5):
        t = 3.8*t*(1-t)

    print(f, ': ', int(t*10000))

```

Ở đây mình lấy phần nguyên
```bash
0 :  0
1 :  7297
2 :  5837
3 :  9217
4 :  5509
5 :  1915
6 :  6058
7 :  8983
8 :  9335
9 :  8418
10 :  5283
11 :  2104
12 :  2797
13 :  6746
14 :  9415
15 :  8481
16 :  6202
17 :  5782
18 :  7547
19 :  9289
20 :  9153
21 :  7266
22 :  4966
23 :  3313
24 :  2511
25 :  2297
26 :  2511
27 :  3313
28 :  4966
29 :  7266
30 :  9153
31 :  9289
32 :  7547
33 :  5782
34 :  6202
35 :  8481
36 :  9415
37 :  6746
38 :  2797
39 :  2104
40 :  5283
41 :  8418
42 :  9335
43 :  8983
44 :  6058
45 :  1915
46 :  5509
47 :  9217
48 :  5837
49 :  7297
```

## Chạy chương trình nhập vào số tương ứng với số timestamp chia lấy dư cho `50`

![image](https://user-images.githubusercontent.com/31529599/120989913-3dcaca00-c7aa-11eb-8994-4d73490f381a.png)

Ở đây mình chạy chương trình lúc timestamp là `1623056716` chia lấy dư cho `50` sẽ là `16`

Tra với số ở trên và nhập vào chương trình sẽ là `6202`

```bash
└─$ ./FindMySecret.exe
Enter the secret number6202
Success! You have completely reverse engineered and found the secret number!
```
Xong !



