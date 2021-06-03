# **EscapeTheDunge0n - Expl0it**

## Task
File: CrackMe.exe

Chạy thử file:

![image](https://user-images.githubusercontent.com/31529599/120669726-e979ce80-c4b9-11eb-8198-8b273f6ce7dd.png)

Bài này là một game trên terminal

Dùng lệnh `file` để kiểm tra file này

```bash
└─$ file CrackMe.exe
CrackMe.exe: PE32 executable (console) Intel 80386, for MS Windows
```

Này là một file windows 32 bit

## Solution

Reverse file bằng IDA pro 7.5

Code `main` function:

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  HWND v3; // eax
  int v5[2]; // [esp+0h] [ebp-8h] BYREF
  const char **savedregs; // [esp+8h] [ebp+0h]

  SetConsoleTitleW(L"::> Dunge0n                                   @made by Expl0it");
  v3 = GetConsoleWindow();
  ShowWindow(v3, 3);
  system("cls");
  print();
  print();
  print();
  print();
  MessageBoxW(0, L"NAG!", L"NAG!", 0x30u);
  print();
  print();
  print();
  print();
  std::istream::operator>>(std::cin, v5);
  if ( v5[0] == 1 )
  {
    Must_Call_to_win();
    return 0;
  }
  if ( v5[0] == 2 )
    return 0;
  print();
  Sleep(0x1388u);
  return main(v5[0], (const char **)v5[1], savedregs);
}
}
```
Hàm `Must_Call_to_win()` đã được đổi tên trong quá trình phân tích chứ không phải IDA đã detect được như vậy

```c
int Must_Call_to_win()
{
  int v0; // eax
  int v1; // eax
  int v2; // eax
  int v3; // eax
  int v4; // eax
  int v5; // eax
  int v6; // eax
  int v7; // eax
  const char *v8; // edx
  int v9; // eax
  int v10; // eax
  int v12; // eax
  int v13; // eax
  int *v14; // eax
  int v15; // eax
  int v16; // eax
  int v17; // eax
  int v18; // eax
  int v19; // eax
  int v20; // eax
  int v21; // eax
  int v22; // eax
  int v23; // eax
  int v24; // eax
  int v25; // eax
  int v26; // eax
  int v27; // eax
  int v28; // eax
  int v29; // [esp+Ch] [ebp-14h] BYREF
  int v30; // [esp+10h] [ebp-10h] BYREF
  int v31; // [esp+14h] [ebp-Ch] BYREF
  int v32; // [esp+18h] [ebp-8h] BYREF

  SetConsoleTitleW(L"Dunge0n                                   @made by Expl0it");
  system("cls");
  v0 = print(std::cout, "\x1B[31m");
  v1 = print(v0, "HEALTH: ");
  std::ostream::operator<<(v1, 100);
  print(
    std::cout,
    "\n"
    "\n"
    "You are in the Dungeon and have to choose a way, because they are 2 ways. But be carefully you can come across a Dragon.\n");
  print(std::cout, "[1] go right\n[2] go left\n\x1B[31m$ ");
  std::istream::operator>>(std::cin, &v30);
  if ( v30 == 1 )
  {
    system("cls");
    print(
      std::cout,
      "Oh no. There are poison traps in this way, shit -10 HP it hurts! Oh no and a rock is roling behind us we have to r"
      "un, shit We fell down somewhere :( Another -10 HP. \n");
    v2 = print(std::cout, "\x1B[31m");
    v3 = print(v2, "HEALTH: ");
    std::ostream::operator<<(v3, 80);
    Sleep(0x1F40u);
    system("cls");
    v4 = print(std::cout, "\x1B[31m");
    v5 = print(v4, "HEALTH: ");
    std::ostream::operator<<(v5, 80);
    print(
      std::cout,
      "\n"
      "\n"
      "Ah hmm where I am?! Wait what? GOLDDDD everywhere!!! Oh no glad to early... \n"
      "A Goblin is there. Shit he seen me already. He is coming... But there is a way hmmm but i have otherwise a Glock.\n");
    print(std::cout, "PRESS [1] to grab Gold and run into the way or [2] to fight with the Goblin\n\x1B[31m$ ");
    std::istream::operator>>(std::cin, &v32);
    if ( v32 == 1 )
    {
      system("cls");
      print(
        std::cout,
        "Oh no another trap it wasnt a way... It's a room :( The ceiling is going down and have spikes...\n");
      v6 = print(std::cout, "\n\n\x1B[31m");
      v7 = print(v6, "HEALTH: ");
      std::ostream::operator<<(v7, 0);
      v8 = "\n\n\x1B[96mOh no you lost the Game... I wish you good luck with the next try :) @Expl0it\n";
LABEL_6:
      print(std::cout, v8);
      return system("pause");
    }
    if ( v32 == 2 )
    {
      system("cls");
      v9 = print(std::cout, "\x1B[31m");
      v10 = print(v9, "HEALTH: ");
      std::ostream::operator<<(v10, 0);
      v8 = "\n"
           "\n"
           "\x1B[96mOh no the Goblin killed you... You lost the Game... I wish you good luck with the next try :) @Expl0it\n";
      goto LABEL_6;
    }
    system("cls");
    print(std::cout, "Wrong enter, try again!\n ");
    v12 = print(std::cout, "\x1B[31m");
    v13 = print(v12, "HEALTH: ");
    std::ostream::operator<<(v13, 80);
    print(
      std::cout,
      "\n"
      "Ah hmm where I am?! Wait what? GOLDDDD everywhere!!! Oh no glad to early... A Goblin is there. Shit he seen me alr"
      "eady. He is coming... But there is a way hmmm but i have otherwise a Glock.\n");
    print(std::cout, "PRESS [1] to grab Gold and run into the way or [2] to fight with the Goblin\n\x1B[31m$ ");
    v14 = &v32;
  }
  else if ( v30 == 2 )
  {
    system("cls");
    v15 = print(std::cout, "\x1B[31m");
    v16 = print(v15, "HEALTH: ");
    std::ostream::operator<<(v16, 100);
    print(
      std::cout,
      "\n"
      "\n"
      "Shit you stepped right in the arms of the dragon :( oh but what is that? There is a chest next to the dragon. Oh a"
      "nd there is a Way behind him.\n");
    print(std::cout, "PRESS [1] to go to the chest or [2] to sneak pass the dragon\n\x1B[31m$ ");
    std::istream::operator>>(std::cin, &v31);
    if ( v31 == 1 )
    {
      system("cls");
      v17 = print(std::cout, "\x1B[31m");
      v18 = print(v17, "HEALTH: ");
      std::ostream::operator<<(v18, 100);
      print(std::cout, "\nHell yes a Sword and the Secret Key! Oh no a rock fellt on the dragon...\n");
      print(std::cout, "PRESS [1] to run or [2] to fight\n\x1B[31m$ ");
      std::istream::operator>>(std::cin, &v32);
      if ( v32 == 1 )
      {
        v19 = print(std::cout, "\x1B[31m");
        v20 = print(v19, "HEALTH: ");
        std::ostream::operator<<(v20, 0);
        v8 = "\n"
             "\n"
             "\x1B[96mOh no you tripped and the Dragon killed you...You lost the Game... I wish you good luck with the ne"
             "xt try :) @Expl0it\n";
        goto LABEL_6;
      }
      if ( v32 == 2 )
      {
        MessageBoxW(
          0,
          L"You killed the Dragon and won the game good job, congratulations! But Whats the Secret Key code now?",
          L"Wait what?!?!",
          0x40u);
        system("cls");
        print(std::cout, "Key Code:\n\x1B[31m$ ");
        std::istream::operator>>(std::cin, &v29);
        if ( v29 == 788960 )
          MessageBoxW(0, L"Congratulations you won! You are a good cracker...\n @Expl0it", L"CONGRATULATIONS!!!", 0x40u);
        else
          MessageBoxW(0, L"You lost the game...Try again", L"YOU LOST!", 0x10u);
        return system("pause");
      }
      system("cls");
      print(std::cout, "Wrong enter, try again!\n ");
      v21 = print(std::cout, "\x1B[31m");
      v22 = print(v21, "HEALTH: ");
      std::ostream::operator<<(v22, 100);
      print(std::cout, "\nHell yes a Sword and the Secret Key! Oh no a rock fellt on the dragon...\n");
      print(std::cout, "PRESS [1] to run or [2] to fight\n\x1B[31m$");
      v14 = &v32;
    }
    else
    {
      if ( v31 == 2 )
      {
        system("cls");
        print(std::cout, "Shit the dragon has woken up you are dead...\n\n");
        v23 = print(std::cout, "\x1B[31m");
        v24 = print(v23, "HEALTH: ");
        std::ostream::operator<<(v24, 0);
        v8 = "\n"
             "\n"
             "\x1B[96mOh no the Dragon killed you... You lost the Game... I wish you good luck with the next try :) @Expl0it\n";
        goto LABEL_6;
      }
      system("cls");
      print(std::cout, "Wrong enter, try again!\n ");
      v25 = print(std::cout, "\x1B[31m");
      v26 = print(v25, "HEALTH: ");
      std::ostream::operator<<(v26, 100);
      print(
        std::cout,
        "\n"
        "Shit you stepped right in the arms of the dragon :( oh but what is that? There is a chest next to the dragon. Oh"
        " and there is a Way behind him.");
      print(std::cout, "PRESS [1] to go to the chest or [2] to sneak pass the dragon\n\x1B[31m$ ");
      v14 = &v31;
    }
  }
  else
  {
    system("cls");
    print(std::cout, "\nWrong enter, try again!\n ");
    v27 = print(std::cout, "\x1B[31m");
    v28 = print(v27, "HEALTH: ");
    std::ostream::operator<<(v28, 100);
    print(
      std::cout,
      "\n"
      "You are in the Dungeon and have to choose a way, because they are 2 of these. But be careful you can come across a Dragon\n");
    print(std::cout, "[1] go right\n[2] go left\n\x1B[31m$ ");
    v14 = &v30;
  }
  return std::istream::operator>>(std::cin, v14);
}
```

Vì hàm trong hàm `main` tương ứng với ở đầu chương trình, yêu cầu nhập vào `1` hoặc `2`, để tiếp tục thì ta phải nhập vào `1` và chương trình gọi hàm `Must_call_to_win`, cho nên ta sẽ tiến hành phân tích hàm này
![image](https://user-images.githubusercontent.com/31529599/120671022-2b574480-c4bb-11eb-8234-86f59124ac10.png)


Mặc dù code khá dài nhưng bài này tương đối đơn giản 
![image](https://user-images.githubusercontent.com/31529599/120671360-825d1980-c4bb-11eb-96ec-17b1a78bb983.png)

Ta tìm được chuỗi có chưa `Congratulation` nên ta biết mục đích của chúng ta sẽ in ra chuỗi này

Phân tích ngược lên trên, ta thấy chương trình lần lượt nhận vào `input` và kiểm tra

### Đoạn ngược lên trên đầu tiên, chương trình nhập vào và kiểm tra số đó có bằng `788960` hay không
![image](https://user-images.githubusercontent.com/31529599/120671580-b9cbc600-c4bb-11eb-8027-0adc1087ded8.png)

### Đoạn tiếp theo lên trên, chương trình nhập vào và tương tự kiểm tra bằng nhau với `2`
![image](https://user-images.githubusercontent.com/31529599/120671730-dec03900-c4bb-11eb-8964-c085823bfab7.png)


### Tiếp theo, chương trình nhập vào và kiểm tra với `1`
![image](https://user-images.githubusercontent.com/31529599/120671846-f8fa1700-c4bb-11eb-9997-9f1002b62b96.png)

### Lên trên tiếp ta sẽ gặp một đoạn `else if` so sánh giá trị với `2` cũng là của input đầu tiên trong hàm `Must_call_to_win`
![image](https://user-images.githubusercontent.com/31529599/120673086-111e6600-c4bd-11eb-9b7d-5556efb09747.png)



## Solve
Vậy input nhập vào sẽ là 
1 -> trong main
2 1 2 78896 -> trong Must_call_to_win()


# Chạy và kiểm tra với input vừa tìm được 
![image](https://user-images.githubusercontent.com/31529599/120673902-cc46ff00-c4bd-11eb-9591-ebadbe888c09.png)

![image](https://user-images.githubusercontent.com/31529599/120674066-ee408180-c4bd-11eb-98f0-1d49bd146376.png)

Done !









