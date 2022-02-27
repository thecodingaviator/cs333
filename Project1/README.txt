Parth Parth
CS333 - Project 1
2/15/2022

Directory layout
Project1/
|
|_/README.txt
|_/project1_1.c
|_/project1_2.c
|_/project1_3.c
|_/project1_4.c
|_/project1_5.c


I'm using Windows 11 witht he following gcc:
gcc.exe (x86_64-win32-seh-rev0, Built by MinGW-W64 project) 8.1.0
Copyright (C) 2018 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

All tasks can be compiled with "gcc -o task project1_taskNumber.c" and run with "./task"

Extensions undertaken: Find float to which you can add 1 and get the same number AND make 
the safe/hacked program use command line arguments

1.
a) Little endian
b) The short (789=0x0315) is displayed as 
15
03
This means that the MSB is stored at the largest address and the LSB at the smallest address.

2.
a) Doing it infinitely, it goes on forever until it randomly stops in the 70,000s.
b) Yes. The following is the dump from the terminal. I assigned three 133=0x85 as ints. These
can be found at lines 8 though 16.
0: 08
1: FE
2: 61
3: 00
4: 00
5: 00
6: 00
7: 00
8: 85
9: 00
10: 00
11: 00
12: 85
13: 00
14: 00
15: 00
16: 85
17: 00
18: 00
19: 00
20: 14
21: 00
22: 00
23: 00
24: C0
25: 13
26: B2
27: 00
28: 00
29: 00
30: 00
31: 00
32: C7
33: 13
34: 40
35: 00
36: 00
37: 00
38: 00
39: 00
40: 01
41: 00
42: 00
43: 00
44: 00
45: 00
46: 00
47: 00
48: C0
49: 13
50: B2
51: 00
52: 00
53: 00
54: 00
55: 00
56: 00
57: 00
58: 00
59: 00
60: 00
61: 00
62: 00
63: 00
64: 00
65: 00
66: 00
67: 00
68: 00
69: 00
70: 00
71: 00
72: 00
73: 00
74: 00
75: 00
76: 00
77: 00
78: 00
79: 00
80: 00
81: 00
82: 00
83: 00
84: 00
85: 00
86: 00
87: 00
88: 00
89: 00
90: 00
91: 00
92: 00
93: 00
94: 00
95: 00
96: 00
97: 00
98: 00
99: 00

3. 
From a starting memory usage of 4.1/7.7GB, without free() I reach 7.7GB memory usage in seconds.
With free(), memory usage remains constant.

4.
a) No. The expected size is 5, but sizeof gives 6 for the struct and 8 for the pointer. This is 
because processors read stuff in 4 or 8 bits (x86 vs x64).
b) The only gaps were after the char which is the last field in the struct. The terminal dump is below:
sizeof(struct Test): 6
sizeof(ptr): 8
0: 01
1: 00
2: 01
3: 00
4: 61
5: 00
6: 0A
7: FE

5.
My compiler printed "safe" contrary to what is expected. On printing str2 byte-by-byte, however,
it prints the whole string (in line with what we would expect):

0: A
1: B
2: C
3: D
4: E
5: F
6: G
7: H
8: I
9: J
10: K
11: L
12: M
13: N
14: O
15: P
16: Q
17: R
18: S
19: T
20: U
21: V
22: W
23: X
24: Y
25: Z
26:
safe

Extension 1: Find the floating point number in C to which you can add one and get back the same number.
The number (/one of the numbers that work for this) is 0xFFFFFFE

Extension 2: Make the safe/hacked C program in Part I use a string from the command line.
Caveats: It still has the alphabets from the original assignment and will not resize to account for 
if the newer string is more than 27 characters (sizeof(str1))