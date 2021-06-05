# **Keygen Me Part 1**

## Task

File: Keygenme_Part_One.exe

Chạy thử chương trình:

```bash
└─$ ./Keygenme_Part_One.exe

__    __  ________  __      __   ______   ________  __    __  __       __  ________
|  \  /  \|        \|  \    /  \ /      \ |        \|  \  |  \|  \     /  \|        \
| $$ /  $$| $$$$$$$$ \$$\  /  $$|  $$$$$$\| $$$$$$$$| $$\ | $$| $$\   /  $$| $$$$$$$$
| $$/  $$ | $$__      \$$\/  $$ | $$ __\$$| $$__    | $$$\| $$| $$$\ /  $$$| $$__
| $$  $$  | $$  \      \$$  $$  | $$|    \| $$  \   | $$$$\ $$| $$$$\  $$$$| $$  \
| $$$$$\  | $$$$$       \$$$$   | $$ \$$$$| $$$$$   | $$\$$ $$| $$\$$ $$ $$| $$$$$
| $$ \$$\ | $$_____     | $$    | $$__| $$| $$_____ | $$ \$$$$| $$ \$$$| $$| $$_____
| $$  \$$\| $$     \    | $$     \$$    $$| $$     \| $$  \$$$| $$  \$ | $$| $$     \
 \$$   \$$ \$$$$$$$$     \$$      \$$$$$$  \$$$$$$$$ \$$   \$$ \$$      \$$ \$$$$$$$$
_______    ______   _______  ________         ______   __    __  ________
|       \  /      \ |       \|        \       /      \ |  \  |  \|        \
| $$$$$$$\|  $$$$$$\| $$$$$$$\\$$$$$$$$      |  $$$$$$\| $$\ | $$| $$$$$$$$
| $$__/ $$| $$__| $$| $$__| $$  | $$         | $$  | $$| $$$\| $$| $$__
| $$    $$| $$    $$| $$    $$  | $$         | $$  | $$| $$$$\ $$| $$  \
| $$$$$$$ | $$$$$$$$| $$$$$$$\  | $$         | $$  | $$| $$\$$ $$| $$$$$
| $$      | $$  | $$| $$  | $$  | $$         | $$__/ $$| $$ \$$$$| $$_____
| $$      | $$  | $$| $$  | $$  | $$          \$$    $$| $$  \$$$| $$     \
 \$$       \$$   \$$ \$$   \$$   \$$           \$$$$$$  \$$   \$$ \$$$$$$$$

Level= 1                 For beginners         Coded By : Sir_Zed
Rules: 1) No Patching 2) You have to make a keygen and a tutorial. 3) Self Keygen
If You have any question : radpak333@gmail.com
Good Luck!

Enter Username (Only Letters and numbers): abcde
Enter Serial : abcde
[-]Come on man it's too easy !!!
[+]Try again boy!



Press any key to continue . . .
```

Challenges này yêu cầu chính ta nhập vào đúng `username` và `serial` tương ứng

Chạy lệnh `file` để kiểm tra file 32/64 bit

```bash
 └─$ file Keygenme_Part_One.exe
Keygenme_Part_One.exe: PE32 executable (console) Intel 80386, for MS Windows
```

-> File Windows 32 bits

## Solution

Load file bằng IDA pro 32 bit và tiến hành phân tích

pseudocode `main` ( một số tên hàm và tên label đã được đổi tên trong quá trình phân tích để thuận lợi cho việc đọc code):

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int v3; // edi
  int v4; // eax
  char *v5; // esi
  unsigned int v6; // edi
  int v7; // ecx
  char v8; // cl
  int *v9; // esi
  int v10; // eax
  int v11; // eax
  int *v12; // ecx
  size_t v13; // esi
  size_t v14; // edx
  void **v15; // eax
  char *v16; // edi
  size_t v17; // ecx
  void **v18; // eax
  void **v19; // ecx
  size_t v20; // edi
  size_t v21; // edx
  void **v22; // eax
  char *v23; // esi
  void *v24; // ecx
  int v25; // eax
  void *v26; // ecx
  unsigned __int8 v28; // al
  size_t v29; // ecx
  void **v30; // eax
  void *v31; // ecx
  void **v32; // ecx
  char *v33; // edi
  void **v34; // edx
  int v35; // eax
  size_t v36; // esi
  bool v37; // cf
  unsigned __int8 v38; // al
  unsigned __int8 v39; // al
  unsigned __int8 v40; // al
  int v41; // eax
  int v42; // eax
  int v43; // eax
  char *v44; // eax
  _BYTE alphaet_upper[36]; // [esp+Ch] [ebp-424h] BYREF
  int v46; // [esp+30h] [ebp-400h]
  int v47; // [esp+34h] [ebp-3FCh]
  int v48; // [esp+38h] [ebp-3F8h]
  unsigned int v49; // [esp+3Ch] [ebp-3F4h]
  int *v50; // [esp+40h] [ebp-3F0h]
  int v51; // [esp+44h] [ebp-3ECh]
  unsigned int v52; // [esp+48h] [ebp-3E8h]
  void *Src[4]; // [esp+4Ch] [ebp-3E4h] BYREF
  size_t Size[2]; // [esp+5Ch] [ebp-3D4h]
  int v55; // [esp+64h] [ebp-3CCh]
  char v56; // [esp+6Bh] [ebp-3C5h]
  void *v57; // [esp+6Ch] [ebp-3C4h] BYREF
  int v58; // [esp+7Ch] [ebp-3B4h]
  unsigned int v59; // [esp+80h] [ebp-3B0h]
  void *Block[4]; // [esp+84h] [ebp-3ACh] BYREF
  size_t v61[2]; // [esp+94h] [ebp-39Ch]
  char v62[16]; // [esp+9Ch] [ebp-394h] BYREF
  int v63[2]; // [esp+ACh] [ebp-384h] BYREF
  char v64[16]; // [esp+B4h] [ebp-37Ch] BYREF
  int v65; // [esp+C4h] [ebp-36Ch]
  int v66; // [esp+C8h] [ebp-368h]
  char v67[16]; // [esp+CCh] [ebp-364h] BYREF
  int v68; // [esp+DCh] [ebp-354h]
  int v69; // [esp+E0h] [ebp-350h]
  char v70[16]; // [esp+E4h] [ebp-34Ch] BYREF
  int v71; // [esp+F4h] [ebp-33Ch]
  int v72; // [esp+F8h] [ebp-338h]
  char v73[16]; // [esp+FCh] [ebp-334h] BYREF
  int v74; // [esp+10Ch] [ebp-324h]
  int v75; // [esp+110h] [ebp-320h]
  char v76[16]; // [esp+114h] [ebp-31Ch] BYREF
  int v77; // [esp+124h] [ebp-30Ch]
  int v78; // [esp+128h] [ebp-308h]
  char v79[16]; // [esp+12Ch] [ebp-304h] BYREF
  int v80; // [esp+13Ch] [ebp-2F4h]
  int v81; // [esp+140h] [ebp-2F0h]
  char v82[16]; // [esp+144h] [ebp-2ECh] BYREF
  int v83; // [esp+154h] [ebp-2DCh]
  int v84; // [esp+158h] [ebp-2D8h]
  char v85[16]; // [esp+15Ch] [ebp-2D4h] BYREF
  int v86; // [esp+16Ch] [ebp-2C4h]
  int v87; // [esp+170h] [ebp-2C0h]
  char v88[16]; // [esp+174h] [ebp-2BCh] BYREF
  int v89; // [esp+184h] [ebp-2ACh]
  int v90; // [esp+188h] [ebp-2A8h]
  char v91[16]; // [esp+18Ch] [ebp-2A4h] BYREF
  int v92; // [esp+19Ch] [ebp-294h]
  int v93; // [esp+1A0h] [ebp-290h]
  char v94[16]; // [esp+1A4h] [ebp-28Ch] BYREF
  int v95; // [esp+1B4h] [ebp-27Ch]
  int v96; // [esp+1B8h] [ebp-278h]
  char v97[16]; // [esp+1BCh] [ebp-274h] BYREF
  int v98; // [esp+1CCh] [ebp-264h]
  int v99; // [esp+1D0h] [ebp-260h]
  char v100[16]; // [esp+1D4h] [ebp-25Ch] BYREF
  int v101; // [esp+1E4h] [ebp-24Ch]
  int v102; // [esp+1E8h] [ebp-248h]
  char v103[16]; // [esp+1ECh] [ebp-244h] BYREF
  int v104; // [esp+1FCh] [ebp-234h]
  int v105; // [esp+200h] [ebp-230h]
  char v106[16]; // [esp+204h] [ebp-22Ch] BYREF
  int v107; // [esp+214h] [ebp-21Ch]
  int v108; // [esp+218h] [ebp-218h]
  char v109[16]; // [esp+21Ch] [ebp-214h] BYREF
  int v110; // [esp+22Ch] [ebp-204h]
  int v111; // [esp+230h] [ebp-200h]
  char v112[16]; // [esp+234h] [ebp-1FCh] BYREF
  int v113; // [esp+244h] [ebp-1ECh]
  int v114; // [esp+248h] [ebp-1E8h]
  char v115[16]; // [esp+24Ch] [ebp-1E4h] BYREF
  int v116; // [esp+25Ch] [ebp-1D4h]
  int v117; // [esp+260h] [ebp-1D0h]
  char v118[16]; // [esp+264h] [ebp-1CCh] BYREF
  int v119; // [esp+274h] [ebp-1BCh]
  int v120; // [esp+278h] [ebp-1B8h]
  char v121[16]; // [esp+27Ch] [ebp-1B4h] BYREF
  int v122; // [esp+28Ch] [ebp-1A4h]
  int v123; // [esp+290h] [ebp-1A0h]
  char v124[16]; // [esp+294h] [ebp-19Ch] BYREF
  int v125; // [esp+2A4h] [ebp-18Ch]
  int v126; // [esp+2A8h] [ebp-188h]
  char v127[16]; // [esp+2ACh] [ebp-184h] BYREF
  int v128; // [esp+2BCh] [ebp-174h]
  int v129; // [esp+2C0h] [ebp-170h]
  char v130[16]; // [esp+2C4h] [ebp-16Ch] BYREF
  int v131; // [esp+2D4h] [ebp-15Ch]
  int v132; // [esp+2D8h] [ebp-158h]
  char v133[16]; // [esp+2DCh] [ebp-154h] BYREF
  int v134; // [esp+2ECh] [ebp-144h]
  int v135; // [esp+2F0h] [ebp-140h]
  char v136[16]; // [esp+2F4h] [ebp-13Ch] BYREF
  int v137; // [esp+304h] [ebp-12Ch]
  int v138; // [esp+308h] [ebp-128h]
  char v139[16]; // [esp+30Ch] [ebp-124h] BYREF
  int v140; // [esp+31Ch] [ebp-114h]
  int v141; // [esp+320h] [ebp-110h]
  char v142[16]; // [esp+324h] [ebp-10Ch] BYREF
  int v143; // [esp+334h] [ebp-FCh]
  int v144; // [esp+338h] [ebp-F8h]
  char v145[16]; // [esp+33Ch] [ebp-F4h] BYREF
  int v146; // [esp+34Ch] [ebp-E4h]
  int v147; // [esp+350h] [ebp-E0h]
  char v148[16]; // [esp+354h] [ebp-DCh] BYREF
  int v149; // [esp+364h] [ebp-CCh]
  int v150; // [esp+368h] [ebp-C8h]
  char v151[16]; // [esp+36Ch] [ebp-C4h] BYREF
  int v152; // [esp+37Ch] [ebp-B4h]
  int v153; // [esp+380h] [ebp-B0h]
  char v154[16]; // [esp+384h] [ebp-ACh] BYREF
  int v155; // [esp+394h] [ebp-9Ch]
  int v156; // [esp+398h] [ebp-98h]
  char v157[16]; // [esp+39Ch] [ebp-94h] BYREF
  int v158; // [esp+3ACh] [ebp-84h]
  int v159; // [esp+3B0h] [ebp-80h]
  char v160[16]; // [esp+3B4h] [ebp-7Ch] BYREF
  int v161; // [esp+3C4h] [ebp-6Ch]
  int v162; // [esp+3C8h] [ebp-68h]
  char v163[16]; // [esp+3CCh] [ebp-64h] BYREF
  int v164; // [esp+3DCh] [ebp-54h]
  int v165; // [esp+3E0h] [ebp-50h]
  char v166[16]; // [esp+3E4h] [ebp-4Ch] BYREF
  int v167; // [esp+3F4h] [ebp-3Ch]
  int v168; // [esp+3F8h] [ebp-38h]
  char v169[36]; // [esp+3FCh] [ebp-34h] BYREF
  int v170; // [esp+420h] [ebp-10h] BYREF
  int v171; // [esp+42Ch] [ebp-4h]

  v3 = 0;
  v52 = 0;
  v49 = 0;
  SetConsoleTitleW(L"KeyGenMe Part 1 | Sir_Zed");
  v61[0] = 0;
  v61[1] = 15;
  LOBYTE(Block[0]) = 0;
  v171 = 1;
  v58 = 0;
  v59 = 15;
  LOBYTE(v57) = 0;
  qmemcpy(alphaet_upper, "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", sizeof(alphaet_upper));
  v63[0] = 0;
  v63[1] = 15;
  v62[0] = 0;
  sub_AE1E90(v62, ".-", 2u);
  LOBYTE(v171) = 2;
  v65 = 0;
  v66 = 15;
  v64[0] = 0;
  sub_AE1E90(v64, "-...", 4u);
  LOBYTE(v171) = 3;
  v68 = 0;
  v69 = 15;
  v67[0] = 0;
  sub_AE1E90(v67, "-.-.", 4u);
  LOBYTE(v171) = 4;
  v71 = 0;
  v72 = 15;
  v70[0] = 0;
  sub_AE1E90(v70, "-..", 3u);
  LOBYTE(v171) = 5;
  v74 = 0;
  v75 = 15;
  v73[0] = 0;
  sub_AE1E90(v73, ".", 1u);
  LOBYTE(v171) = 6;
  v77 = 0;
  v78 = 15;
  v76[0] = 0;
  sub_AE1E90(v76, "..-.", 4u);
  LOBYTE(v171) = 7;
  v80 = 0;
  v81 = 15;
  v79[0] = 0;
  sub_AE1E90(v79, "--.", 3u);
  LOBYTE(v171) = 8;
  v83 = 0;
  v84 = 15;
  v82[0] = 0;
  sub_AE1E90(v82, "....", 4u);
  LOBYTE(v171) = 9;
  v86 = 0;
  v87 = 15;
  v85[0] = 0;
  sub_AE1E90(v85, "..", 2u);
  LOBYTE(v171) = 10;
  v89 = 0;
  v90 = 15;
  v88[0] = 0;
  sub_AE1E90(v88, ".---", 4u);
  LOBYTE(v171) = 11;
  v92 = 0;
  v93 = 15;
  v91[0] = 0;
  sub_AE1E90(v91, ".-.", 3u);
  LOBYTE(v171) = 12;
  v95 = 0;
  v96 = 15;
  v94[0] = 0;
  sub_AE1E90(v94, ".-..", 4u);
  LOBYTE(v171) = 13;
  v98 = 0;
  v99 = 15;
  v97[0] = 0;
  sub_AE1E90(v97, "--", 2u);
  LOBYTE(v171) = 14;
  v101 = 0;
  v102 = 15;
  v100[0] = 0;
  sub_AE1E90(v100, "-.", 2u);
  LOBYTE(v171) = 15;
  v104 = 0;
  v105 = 15;
  v103[0] = 0;
  sub_AE1E90(v103, "---", 3u);
  LOBYTE(v171) = 16;
  v107 = 0;
  v108 = 15;
  v106[0] = 0;
  sub_AE1E90(v106, ".--.", 4u);
  LOBYTE(v171) = 17;
  v110 = 0;
  v111 = 15;
  v109[0] = 0;
  sub_AE1E90(v109, "--.-", 4u);
  LOBYTE(v171) = 18;
  v113 = 0;
  v114 = 15;
  v112[0] = 0;
  sub_AE1E90(v112, ".-.", 3u);
  LOBYTE(v171) = 19;
  v116 = 0;
  v117 = 15;
  v115[0] = 0;
  sub_AE1E90(v115, "...", 3u);
  LOBYTE(v171) = 20;
  v119 = 0;
  v120 = 15;
  v118[0] = 0;
  sub_AE1E90(v118, "-", 1u);
  LOBYTE(v171) = 21;
  v122 = 0;
  v123 = 15;
  v121[0] = 0;
  sub_AE1E90(v121, "..-", 3u);
  LOBYTE(v171) = 22;
  v125 = 0;
  v126 = 15;
  v124[0] = 0;
  sub_AE1E90(v124, "...-", 4u);
  LOBYTE(v171) = 23;
  v128 = 0;
  v129 = 15;
  v127[0] = 0;
  sub_AE1E90(v127, ".--", 3u);
  LOBYTE(v171) = 24;
  v131 = 0;
  v132 = 15;
  v130[0] = 0;
  sub_AE1E90(v130, "-..-", 4u);
  LOBYTE(v171) = 25;
  v134 = 0;
  v135 = 15;
  v133[0] = 0;
  sub_AE1E90(v133, "-.--", 4u);
  LOBYTE(v171) = 26;
  v137 = 0;
  v138 = 15;
  v136[0] = 0;
  sub_AE1E90(v136, "--..", 4u);
  LOBYTE(v171) = 27;
  v140 = 0;
  v141 = 15;
  v139[0] = 0;
  sub_AE1E90(v139, ".----", 5u);
  LOBYTE(v171) = 28;
  v143 = 0;
  v144 = 15;
  v142[0] = 0;
  sub_AE1E90(v142, "..---", 5u);
  LOBYTE(v171) = 29;
  v146 = 0;
  v147 = 15;
  v145[0] = 0;
  sub_AE1E90(v145, "...--", 5u);
  LOBYTE(v171) = 30;
  v149 = 0;
  v150 = 15;
  v148[0] = 0;
  sub_AE1E90(v148, "....-", 5u);
  LOBYTE(v171) = 31;
  v152 = 0;
  v153 = 15;
  v151[0] = 0;
  sub_AE1E90(v151, ".....", 5u);
  LOBYTE(v171) = 32;
  v155 = 0;
  v156 = 15;
  v154[0] = 0;
  sub_AE1E90(v154, "-....", 5u);
  LOBYTE(v171) = 33;
  v158 = 0;
  v159 = 15;
  v157[0] = 0;
  sub_AE1E90(v157, "--...", 5u);
  LOBYTE(v171) = 34;
  v161 = 0;
  v162 = 15;
  v160[0] = 0;
  sub_AE1E90(v160, "---..", 5u);
  LOBYTE(v171) = 35;
  v164 = 0;
  v165 = 15;
  v163[0] = 0;
  sub_AE1E90(v163, "----.", 5u);
  LOBYTE(v171) = 36;
  v167 = 0;
  v168 = 15;
  v166[0] = 0;
  sub_AE1E90(v166, "-----", 5u);
  LOBYTE(v171) = 37;
  system("color 1");
  v4 = print(
         std::cout,
         "\n"
         "__    __  ________  __      __   ______   ________  __    __  __       __  ________ \n"
         "|  \\  /  \\|        \\|  \\    /  \\ /      \\ |        \\|  \\  |  \\|  \\     /  \\|        \\\n"
         "| $$ /  $$| $$$$$$$$ \\$$\\  /  $$|  $$$$$$\\| $$$$$$$$| $$\\ | $$| $$\\   /  $$| $$$$$$$$\n"
         "| $$/  $$ | $$__      \\$$\\/  $$ | $$ __\\$$| $$__    | $$$\\| $$| $$$\\ /  $$$| $$__    \n"
         "| $$  $$  | $$  \\      \\$$  $$  | $$|    \\| $$  \\   | $$$$\\ $$| $$$$\\  $$$$| $$  \\   \n"
         "| $$$$$\\  | $$$$$       \\$$$$   | $$ \\$$$$| $$$$$   | $$\\$$ $$| $$\\$$ $$ $$| $$$$$   \n"
         "| $$ \\$$\\ | $$_____     | $$    | $$__| $$| $$_____ | $$ \\$$$$| $$ \\$$$| $$| $$_____ \n"
         "| $$  \\$$\\| $$     \\    | $$     \\$$    $$| $$     \\| $$  \\$$$| $$  \\$ | $$| $$     \\\n"
         " \\$$   \\$$ \\$$$$$$$$     \\$$      \\$$$$$$  \\$$$$$$$$ \\$$   \\$$ \\$$      \\$$ \\$$$$$$$$               "
         "                                                                                            \n"
         "_______    ______   _______  ________         ______   __    __  ________           \n"
         "|       \\  /      \\ |       \\|        \\       /      \\ |  \\  |  \\|        \\          \n"
         "| $$$$$$$\\|  $$$$$$\\| $$$$$$$\\\\$$$$$$$$      |  $$$$$$\\| $$\\ | $$| $$$$$$$$          \n"
         "| $$__/ $$| $$__| $$| $$__| $$  | $$         | $$  | $$| $$$\\| $$| $$__              \n"
         "| $$    $$| $$    $$| $$    $$  | $$         | $$  | $$| $$$$\\ $$| $$  \\             \n"
         "| $$$$$$$ | $$$$$$$$| $$$$$$$\\  | $$         | $$  | $$| $$\\$$ $$| $$$$$             \n"
         "| $$      | $$  | $$| $$  | $$  | $$         | $$__/ $$| $$ \\$$$$| $$_____           \n"
         "| $$      | $$  | $$| $$  | $$  | $$          \\$$    $$| $$  \\$$$| $$     \\          \n"
         " \\$$       \\$$   \\$$ \\$$   \\$$   \\$$           \\$$$$$$  \\$$   \\$$ \\$$$$$$$$       \n"
         "   \n"
         "Level= 1                 For beginners         Coded By : Sir_Zed                                              "
         "                     \n"
         "Rules: 1) No Patching 2) You have to make a keygen and a tutorial. 3) Self Keygen\n"
         "If You have any question : radpak333@gmail.com\n"
         "Good Luck!                                                                              \n"
         "\t\t");
  std::ostream::operator<<(v4, sub_AE2390);
  print(std::cout, "Enter Username (Only Letters and numbers): ");
  cin_get_input(std::cin, v169);
  v5 = v169;
  v55 = &v170 < (int *)v169 ? 0 : 36;
  do
  {
    ++v3;
    *v5 = toupper(*v5);
    ++v5;
  }
  while ( v3 != v55 );
  v6 = v52;
  v7 = 0;
  v55 = 0;
  do
  {
    v8 = v169[v7];
    v9 = v63;
    v10 = 0;
    v56 = v8;
    v51 = 0;
    v50 = v63;
    do
    {
      if ( v8 == alphaet_upper[v10] )
      {
        LOBYTE(v171) = 38;
        v11 = *v9 + 1;
        Size[0] = 0;
        Size[1] = 15;
        LOBYTE(Src[0]) = 0;
        v52 = v6 | 1;
        v49 = v6 | 1;
        sub_AE2880(Src, v11);
        v12 = v9 - 4;
        if ( (unsigned int)v9[1] >= 0x10 )
          v12 = (int *)*v12;
        v13 = *v9;
        v14 = Size[0];
        if ( v13 > Size[1] - Size[0] )
        {
          LOBYTE(v48) = 0;
          sub_AE26C0(Src, v13, v48, (int)v12, v13);
        }
        else
        {
          Size[0] += v13;
          v15 = Src;
          if ( Size[1] >= 0x10 )
            v15 = (void **)Src[0];
          v16 = (char *)v15 + v14;
          memmove((char *)v15 + v14, v12, v13);
          v16[v13] = 0;
        }
        v17 = Size[0];
        if ( Size[1] == Size[0] )
        {
          LOBYTE(v47) = 0;
          sub_AE26C0(Src, 1, v47, (int)" ", 1u);
        }
        else
        {
          ++Size[0];
          v18 = Src;
          if ( Size[1] >= 0x10 )
            v18 = (void **)Src[0];
          *(_WORD *)((char *)v18 + v17) = 32;
        }
        v19 = Src;
        if ( Size[1] >= 0x10 )
          v19 = (void **)Src[0];
        v20 = Size[0];
        v21 = v61[0];
        if ( Size[0] > v61[1] - v61[0] )
        {
          LOBYTE(v46) = 0;
          sub_AE26C0(Block, Size[0], v46, (int)v19, Size[0]);
        }
        else
        {
          v61[0] += Size[0];
          v22 = Block;
          if ( v61[1] >= 0x10 )
            v22 = (void **)Block[0];
          v23 = (char *)v22 + v21;
          memmove((char *)v22 + v21, v19, Size[0]);
          v23[v20] = 0;
        }
        LOBYTE(v171) = 37;
        v6 = v52 & 0xFFFFFFFE;
        if ( Size[1] >= 0x10 )
        {
          v24 = Src[0];
          if ( Size[1] + 1 >= 0x1000 )
          {
            v24 = (void *)*((_DWORD *)Src[0] - 1);
            if ( (unsigned int)(Src[0] - v24 - 4) > 0x1F )
              goto LABEL_74;
          }
          sub_AE2D8B(v24);
        }
        v8 = v56;
        v10 = v51;
        v9 = v50;
      }
      ++v10;
      v9 += 6;
      v51 = v10;
      v50 = v9;
    }
    while ( v10 < 36 );
    v7 = v55 + 1;
    v55 = v7;
  }
  while ( v7 < 36 );
  if ( v61[0] )
  {
    print(std::cout, "Enter Serial : ");
    std::istream::ignore(std::cin, 1, 0, -1);
    v28 = std::ios::widen(std::cin + *(_DWORD *)(std::cin + 4), 10);
    get_input_serial(v28);
    Size[0] = 0;
    Size[1] = 15;
    LOBYTE(Src[0]) = 0;
    v29 = v61[0] - 1;
    if ( v61[0] < v61[0] - 1 )
      v29 = v61[0];
    v30 = Block;
    if ( v61[1] >= 0x10 )
      v30 = (void **)Block[0];
    sub_AE1E90(Src, v30, v29);
    if ( v61[1] >= 0x10 )
    {
      v31 = Block[0];
      if ( v61[1] + 1 >= 0x1000 )
      {
        v31 = (void *)*((_DWORD *)Block[0] - 1);
        if ( (unsigned int)(Block[0] - v31 - 4) > 0x1F )
          goto LABEL_74;
      }
      sub_AE2D8B(v31);
    }
    v32 = &v57;
    v33 = (char *)v57;
    v34 = Block;
    if ( v59 >= 0x10 )
      v32 = (void **)v57;
    v35 = _mm_cvtsi128_si32(*(__m128i *)Src);
    *(_OWORD *)Block = *(_OWORD *)Src;
    if ( Size[1] >= 0x10 )
      v34 = (void **)v35;
    *(_QWORD *)v61 = *(_QWORD *)Size;
    if ( Size[0] != v58 )
      goto Wrong_Label;
    v36 = Size[0] - 4;
    if ( Size[0] < 4 )
    {
LABEL_54:
      if ( v36 == -4 )
        goto LABEL_63;
    }
    else
    {
      while ( *v34 == *v32 )
      {
        ++v34;
        ++v32;
        v37 = v36 < 4;
        v36 -= 4;
        if ( v37 )
          goto LABEL_54;
      }
    }
    v37 = *(_BYTE *)v34 < *(_BYTE *)v32;
    if ( *(_BYTE *)v34 != *(_BYTE *)v32
      || v36 != -3
      && ((v38 = *((_BYTE *)v34 + 1), v37 = v38 < *((_BYTE *)v32 + 1), v38 != *((_BYTE *)v32 + 1))
       || v36 != -2
       && ((v39 = *((_BYTE *)v34 + 2), v37 = v39 < *((_BYTE *)v32 + 2), v39 != *((_BYTE *)v32 + 2))
        || v36 != -1 && (v40 = *((_BYTE *)v34 + 3), v37 = v40 < *((_BYTE *)v32 + 3), v40 != *((_BYTE *)v32 + 3)))) )
    {
      v41 = v37 ? -1 : 1;
      goto win_label;
    }
LABEL_63:
    v41 = 0;
win_label:
    if ( !v41 )
    {
      v42 = print(std::cout, "[-]Wow! You're god damn genius!\n[+]Now make a keygen :)");
      std::ostream::operator<<(v42, sub_AE2390);
      system("color 2");
LABEL_67:
      std::ostream::operator<<(std::cout, sub_AE2390);
      std::ostream::operator<<(std::cout, sub_AE2390);
      std::ostream::operator<<(std::cout, sub_AE2390);
      system("pause");
      LOBYTE(v171) = 1;
      `eh vector destructor iterator'(v62, 0x18u, 0x24u, sub_AE1DA0);
      if ( v59 >= 0x10 )
      {
        v44 = v33;
        if ( v59 + 1 >= 0x1000 )
        {
          v33 = (char *)*((_DWORD *)v33 - 1);
          if ( (unsigned int)(v44 - v33 - 4) > 0x1F )
            goto LABEL_74;
        }
        sub_AE2D8B(v33);
      }
      if ( v61[1] < 0x10 )
        return 0;
      v26 = Block[0];
      if ( v61[1] + 1 < 0x1000 )
        goto LABEL_36;
      v26 = (void *)*((_DWORD *)Block[0] - 1);
      if ( (unsigned int)(Block[0] - v26 - 4) <= 0x1F )
        goto LABEL_36;
LABEL_74:
      invalid_parameter_noinfo_noreturn();
    }
Wrong_Label:
    v43 = print(std::cout, "[-]Come on man it's too easy !!!\n[+]Try again boy!");
    std::ostream::operator<<(v43, sub_AE2390);
    system("color 4 ");
    goto LABEL_67;
  }
  v25 = print(std::cout, "[*]Don't cheat u little....\n[+](Only Only ___Letters____ and ____numbers____)");
  std::ostream::operator<<(v25, sub_AE2390);
  LOBYTE(v171) = 1;
  `eh vector destructor iterator'(v62, 0x18u, 0x24u, sub_AE1DA0);
  if ( v61[1] >= 0x10 )
  {
    v26 = Block[0];
    if ( v61[1] + 1 < 0x1000 || (v26 = (void *)*((_DWORD *)Block[0] - 1), (unsigned int)(Block[0] - v26 - 4) <= 0x1F) )
    {
LABEL_36:
      sub_AE2D8B(v26);
      return 0;
    }
    goto LABEL_74;
  }
  return 0;
}
```

Đây là đoạn code mà ta muốn chương trình in ra:
![image](https://user-images.githubusercontent.com/31529599/120786571-9014ac80-c558-11eb-81a4-a0782900730f.png)

Vậy để in ra chuỗi này thì ta phải nhảy tới `LABEL_63` để set `v41=0` sau đó thực hiện câu `if` trong `win_label` và in ra chuỗi

Đoạn code gọi `LABEL_63`:
![image](https://user-images.githubusercontent.com/31529599/120787048-25b03c00-c559-11eb-82e8-33c2b1ac70c5.png)


