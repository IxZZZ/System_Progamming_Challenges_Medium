# **ZED-Crackme**

# Task
File: ZED-Crackme-x64.bin

Chạy thử file:

```bash
└─$ ./ZED-Crackme-x64.bin
Segmentation fault
```
Khi chạy file ta thấy file bị lỗi `segmentation`

Chạy lệnh  `file` để xem file là 32/64 bit

```bash
└─$ file ZED-Crackme-x64.bin
ZED-Crackme-x64.bin: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), statically linked, no section header
```
-> file linux 64 bit

## Solution

Load file bằng IDA pro 64 bit và tiến hành phân tích

