CS333 - Project 6 - README
Parth Parth
04/12/2022

File Structure:
├── Project6
│   ├── README.txt
│   ├── linkedlist.h
│   ├── python
│   │   ├── input.txt
│   │   ├── output.txt
│   │   ├── output1.txt
│   │   ├── task1.py
│   │   ├── task2.py
│   │   ├── task2a
│   │   ├── task3.py
│   │   ├── test.txt
│   │   └── testerr.txt
│   ├── task2a.c
│   ├── task2b.c
│   ├── task2c.c
│   ├── test.txt
│   ├── wordCount.c
│   ├── wordCounter.c
│   └── yourLinkedList.c

Config:
Ubuntu 20.04.3 LTS using WSL on Windows 11 - gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0

Tasks:

C:

    Task 1:
        
        For this task, I extended the Linked List from last project to keep track of words and their word count.
        The words have been stored in a struct declared in wordCount.c alongside two comparators for sorting (
        based on frequency and alphabetical order). There is also a function to print the struct.

        Compile:
        gcc -o wordCount wordCounter.c yourLinkedList.c

        Run:
        ./wordCount test.txt

        Output:
        the: 17
        of: 7
        and: 6
        was: 5
        with: 4
        in: 4
        windows: 3
        a: 3
        wings: 2
        up: 2
        portion: 2
        central: 2
        but: 2
        broken: 2
        were: 2
        been: 2
        had: 2
        no: 1
        there: 1
        into: 1


        Extension 1:
        I have made the Word Counter more robust by checking for number of arguments and checking that the file exists.


    Task 2:

        For this task, I used the signal handlers to catch errors using SIGINT, SIGFPE, and SIGSEGV signals and print the error message.

        a.
            Compile:
            gcc -o task2a task2a.c

            Run:
            ./task2a

            Output:
            I'm waiting for you to cntl-C me
            I'm waiting for you to cntl-C me
            I'm waiting for you to cntl-C me
            I'm waiting for you to cntl-C me
            I'm waiting for you to cntl-C me
            I'm waiting for you to cntl-C me
            I'm waiting for you to cntl-C me
            I'm waiting for you to cntl-C me
            I'm waiting for you to cntl-C me
            ^CI'm waiting for you to cntl-C me
            I'm waiting for you to cntl-C me
            Signal called with code: 2
            Interrupt signal. Exiting.

        b.
            Compile:
            gcc -o task2b task2b.c

            Run:
            ./task2b

            Output:
            Signal called with code: 8
            Floating point exception. Exiting

        c.
            Compile:
            gcc -o task2c task2c.c

            Run:
            ./task2c

            Output:
            Signal called with code: 11
            Segmentation fault. Exiting
