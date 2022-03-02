CS333 - Project 3 - README
Parth Parth
02//2022

├── Project3
│   ├── README.txt
│   ├── cstk.c
│   ├── cstk.h
│   ├── cstktest
│   ├── cstktest.c
│   └── python
│       ├── task2.py
│       └── task2_obfuscated.py

Config:
macOS Monterey 12.2.1 - Apple clang version 13.0.0 (clang-1300.0.29.30)

Tasks:

C:

    For this C programming task, I have created the header file for the stack (cstk.h)
    and implemented the methods defined in the header file in C code (cstk.c).

    Compile:
    gcc -o cstktest cstktest.c cstk.c

    Run:
    ./cstktest

    Output:
    The original list: 0 1 2 3 4 5 6 7 8 9 
    The reversed list: 9 8 7 6 5 4 3 2 1 0


    Extensions:

    1. In the cstk.c file's stk_push function, I have added the functionality for the stack 
    to be resized if it is full. When the stack reaches its limit, it expands to twice its 
    size.

    I have implemented the functionality in cstk2.c. For demonstration, I have set the 
    maximum size variable (CSTK_MAX) to 5.

    Compile:
    gcc -o cstktest2 cstktest.c cstk2.c

    Run:
    ./cstktest2

    Output:
    Stack is full so resizing it
    The original list: 0 1 2 3 4 5 6 7 8 9
    The reversed list: 9 8 7 6 5 4 3 2 1 0