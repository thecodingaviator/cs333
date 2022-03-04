CS333 - Project 4 - README
Parth Parth
03/04/2022

Config:
macOS Monterey 12.2.1 - Apple clang version 13.0.0 (clang-1300.0.29.30)

Tasks:

C:

    Task 1:
        To implement the comparator, I divided the problem

        Compile:
        gcc -o q quicksort.c

        Run:
        ./q

        Output:
        
        
    Task 2:
        On running the program, this is what we get:
        parth@Parths-MacBook-Air Project4 % gcc -o f factorial.c
        parth@Parths-MacBook-Air Project4 % ./f 11              
        39916800
        parth@Parths-MacBook-Air Project4 % ./f 12
        479001600
        parth@Parths-MacBook-Air Project4 % ./f 13
        1932053504
        parth@Parths-MacBook-Air Project4 % ./f 14
        1278945280
        parth@Parths-MacBook-Air Project4 % ./f 15
        2004310016

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