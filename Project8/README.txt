CS333 - Project 8 - README
Parth Parth
05/01/2022

File Structure:


Config:
Ubuntu 20.04.3 LTS using WSL 2 on Windows 11 - gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.1) 

Tasks:

C:
  1.

    All of the programming files for this task are in the c folder.

  2.

    For this C programming task, I have created the colorizer in parallel.
    All files for this task are in the kit folder.
    
    To select the number of threads, use the optional command line argument.
    The default is 4. (Extension 1)

    Compile:
    gcc -o colorize -I. colorize_parallel.c my_timing.c ppmIO.c -lm -lpthread

    Run:
    ./colorize <filename> <number of threads. default = 4>
