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

    Compile:
    gcc -o task task1f.c my_timing.c -lm -lpthread

    Run:
    ./task <filename>

    Analysis: Performed with medium.bin

      a: 0.001482, 0.002377, 0.000982, 0.001453, 0.001571. Average of middle three: 0.001502s
      b: 0.001300, 0.000932, 0.000935, 0.001021, 0.000952. Average of middle three: 0.000963s
      c: 0.000517, 0.000442, 0.000543, 0.000461, 0.000497. Average of middle three: 0.000491s
      d: 0.000583, 0.000856, 0.000762, 0.000685, 0.000510. Average of middle three: 0.000676s
      e: 0.000703, 0.000917, 0.000583, 0.000377, 0.000797. Average of middle three: 0.000694s
      f: 0.000768, 0.000678, 0.000691, 0.000904, 0.000895. Average of middle three: 0.000784s

      Therefore, the most efficient is strategy c. The average is 0.000491s. This strategy makes
      use of efficieny by having the threads write to separate locations before combining them in
      one place locked by a mutex. This way, the threads can be written to different locations
      without having to wait for each other.
      The most inefficient strategy is strategy a. The average is 0.001502s. This strategy locks
      the global array the most times and is therefore the most expensive.

      We can conclude that mutex locks make the program slower. a is the strategy with the most
      locks while c utilises the least. This is, however, faster than sequential execution
      (strategies e and f). While a mutex should be avoided, it can be used in cases where all
      the threads are doing something for a lot of time and the variable protected by the mutex
      will only be updated in the end. Therefore, it is a good idea to use mutexes in cases where
      the threads are doing something separate for a lot of time.

  2.

    For this C programming task, I have created the colorizer in parallel.
    All files for this task are in the kit folder.
    
    To select the number of threads, use the optional command line argument.
    The default is 4. (Extension 1)

    Compile:
    gcc -o colorize -I. colorize_parallel.c my_timing.c ppmIO.c -lm -lpthread

    Run:
    ./colorize <filename> <number of threads. default = 4>

    Analysis:

    Sequential: 0.026817, 0.023447, 0.026107, 0.025851, 0.024254. Average of middle three: 0.025404s
    Parallel (Threads = 1): 0.026615, 0.034937, 0.023661, 0.029492, 0.039937. Average of middle three: 0.030348s
    Parallel (Threads = 2): 0.012531, 0.016759, 0.024662, 0.013480, 0.012068. Average of middle three: 0.014256s
    Parallel (Threads = 4): 0.008788, 0.010673, 0.009578, 0.006803, 0.010879. Average of middle three: 0.009650s

    Clearly, the more threads involved, the faster the program is. The only case that is not true for is
    when only one thread is being used. That makes sense because in that case it is just a sequential
    program with extra steps.
