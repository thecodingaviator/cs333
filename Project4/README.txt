CS333 - Project 4 - README
Parth Parth
03/04/2022

File Structure:
├── Project4
│   ├── README.txt
│   ├── factorial.c
│   ├── python
│   │   ├── task1.py
│   │   ├── task2.py
│   │   └── task3.py
│   ├── quicksort.c
│   └── r
│       ├── task1.R
│       ├── task2.R
│       └── task3.R

Config:
Ubuntu 20.04.3 LTS using WSL on Windows 11 - gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0

Tasks:

C:

    Task 1:
        To implement the comparator, I divided the problem into three parts:
            1. If both the numbers are odd, sort them in ascending order.
            2. If both the numbers are even, sort them in descending order.
            3. If one of the numbers is odd and the other is even, the even
            number comes first.

        Compile:
        gcc -o q quicksort.c

        Run:
        ./q

        Output:
        The sorted array is: 12 10 8 6 4 2 0 1 3 5 7 9 11 13
        
        
    Task 2:

        Compile:
        gcc -o f factorial.c

        Run:
        ./f <number>

        Output:
        parth@DESKTOP-1VEVFJK:~/CS333/Project4$ gcc -o f factorial.c
        parth@DESKTOP-1VEVFJK:~/CS333/Project4$ ./f 12
        479001600
        parth@DESKTOP-1VEVFJK:~/CS333/Project4$ ./f 13
        1932053504
        parth@DESKTOP-1VEVFJK:~/CS333/Project4$ ./f 14
        1278945280
        parth@DESKTOP-1VEVFJK:~/CS333/Project4$ ./f 15
        2004310016

        Explanation:
        12! = 479001600
        13! = 12! *13 which is:
        6227020800      =      101110011001010001100110000000000 which gets 
        truncated to 01110011001010001100110000000000 to fit in 32 bits. In
        base 10, this is: 1932053504 which is exactly what the program is 
        giving us.

        When we calculate 14! now, we are actually doing 1932053504 * 14
        which is: 27048749056 and 11001001100001110110010100000000000 in
        binary. After getting truncated, we get: 01001100001110110010100000000000
        which is 1278945280 in base 10. This is what we get from the program.

        When we calculate 15! now, we are actually doing 1278945280 * 15
        which is: 19184179200 and 10001110111011101110101100000000000 in
        binary. After getting truncated, we get: 01110111011101110101100000000000
        which is 2004310016 in base 10. This is what we get from the program.
